## 分布式进程

在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。

Python的`multiprocessing`模块不但支持多进程，其中`managers`子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于`managers`模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。

我们先看服务进程，服务进程负责启动`Queue`，把`Queue`注册到网络上，然后往`Queue`里面写入任务：

```python
import random, time, queue
from multiprocessing.managers import BaseManager

# Queue for sending tasks
task_queue = queue.Queue()
# Queue for receiving tasks
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

# Put two Queues on network
QueueManager.register("get_task_queue", callable=lambda: task_queue)
QueueManager.register("get_result_queue", callable=lambda: result_queue)

# Bind port 5000, set passcode 'abc'
manager = QueueManager(address=('', 5000), authkey=b"abc")
# Start queue
manager.start()
# Get queue object from network
task = manager.get_task_queue()
result = manager.get_result_queue()

# Put several tasks into it
for i in range(10):
    n = random.randint(0, 10000)
    print("Put task %d..." % n)
    task.put(n)

# Read result in result queue
print("Try get results...")
for i in range(10):
    r = result.get(timeout=10)
    print("Result: %s" % r)

# Close
manager.shutdown()
print("Master exit...")
```

请注意，当我们在一台机器上写多进程程序时，创建的`Queue`可以直接拿来用，但是，在分布式多进程环境下，添加任务到`Queue`不可以直接对原始的`task_queue`进行操作，那样就绕过了`QueueManager`的封装，必须通过`manager.get_task_queue()`获得的`Queue`接口添加。

然后，在另一台机器上启动任务进程（本机上启动也可以）：

```python
import time, sys, queue
from multiprocessing.managers import BaseManager

# Create similar QueueManager
class QueueManager(BaseManager):
    pass

# We just supply names since we get Queue from internet
QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

# Connect to the server which runs task_master.py
server_addr = "127.0.0.1"
print ("connect to server %s..." % server_addr)
# Auth
m = QueueManager(address=(server_addr, 5000), authkey=b"abc")
# Connect from network
m.connect()
# Get the Queue object
task = m.get_task_queue()
result = m.get_result_queue()

# Get tasks from task queue, and write results to result queue
for i in range(10):
    try:
        n = task.get(timeout=1)
        print("run task %d * %d" % (n, n))
        r = "%d * %d = %d" % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print("task queue is empty...")
# Over
print ("Work exit...")
```

任务进程要通过网络连接到服务进程，所以要指定服务进程的IP。

现在，可以试试分布式进程的工作效果了。先启动`task_master.py`服务进程：

```
>>> (In master window)
Put task 4511...
Put task 8477...
Put task 8092...
Put task 1587...
Put task 664...
Put task 9282...
Put task 5083...
Put task 2409...
Put task 2260...
Put task 2684...
Try get results...
Result: 4511 * 4511 = 20349121
Result: 8477 * 8477 = 71859529
Result: 8092 * 8092 = 65480464
Result: 1587 * 1587 = 2518569
Result: 664 * 664 = 440896
Result: 9282 * 9282 = 86155524
Result: 5083 * 5083 = 25836889
Result: 2409 * 2409 = 5803281
Result: 2260 * 2260 = 5107600
Result: 2684 * 2684 = 7203856
Master exit...
```

这个简单的Master/Worker模型有什么用？其实这就是一个简单但真正的分布式计算，把代码稍加改造，启动多个worker，就可以把任务分布到几台甚至几十台机器上，比如把计算`n*n`的代码换成发送邮件，就实现了邮件队列的异步发送。

Queue对象存储在哪？注意到`task_worker.py`中根本没有创建Queue的代码，所以，Queue对象存储在`task_master.py`进程中：

![](http://okye062gb.bkt.clouddn.com/2017-06-18-130257.jpg)

而`Queue`之所以能通过网络访问，就是通过`QueueManager`实现的。由于`QueueManager`管理的不止一个`Queue`，所以，要给每个`Queue`的网络调用接口起个名字，比如`get_task_queue`。

`authkey`有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰。如果`task_worker.py`的`authkey`和`task_master.py`的`authkey`不一致，肯定连接不上。


### 小结

Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。

注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。

