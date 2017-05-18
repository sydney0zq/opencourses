##进程的描述和进程的创建

<http://www.jianshu.com/p/cd6110439786>

Linux提供了两个函数来创建进程。

1. fork()

fork()提供了创建进程的基本操作，可以说它是Linux系统多任务的基础。该函数在/linux-3.18.6/kernel/fork.c


2. exec系列函数

**如果只有fork()，肯定是不完美的，因为fork()只能参数一个父进程的副本。而exec系列函数则可以帮助我们建立一个全新的新进程。**

在Linux系统中，一个进程的PCB是一个C语言的结构体`task_struct`来表示，而多个PCB之间是由一个双向链表组织起来的，在《Understanding the Linux Kernel》中，则是进一步描述这个链表是一个双向循环链表。

在Linux中创建一个新进程的方法是使用fork函数，fork()执行一次但有两个返回值。
在父进程中，返回值是子进程的进程号；在子进程中，返回值为0。因此可通过返回值来判断当前进程是父进程还是子进程。

使用fork函数得到的子进程是父进程的一个复制品，它从父进程处复制了整个进程的地址空间，包括进程上下文，进程堆栈，内存信息，打开的文件描述符，信号控制设定，进程优先级，进程组号，当前工作目录，根目录，资源限制，控制终端等。而子进程所独有的只是它的进程号，资源使用和计时器等。可以看出，**使用fork函数的代价是很大的，它复制了父进程中的代码段，数据段和堆栈段里的大部分内容，使得fork函数的执行速度并不快。**

创建一个进程，至少涉及的函数：

```
sys_clone, do_fork, dup_task_struct, copy_process, copy_thread, ret_from_fork
```


###创建一个新进程在内核中的执行过程

- fork、vfork和clone三个系统调用都可以创建一个新进程，而且都是通过调用`do_fork`来实现进程的创建
- 新的进程是从`ret_from_fork`处开始执行的，在`ret_from_fork`函数中，首先，子进程通过`copy_process`函数和`dup_task_struct`函数复制父进程的状态，并通过`alloc_thread_info`将父进程的堆栈状态压入子进程的堆栈以备返回父进程时候使用，确保了内核进程的执行起点与内核堆栈保持一致，最后，跳转至`sys_call_exit`函数，完成子进程的创建。
- Linux通过复制父进程来创建一个新进程，那么这就给我们理解这一个过程提供一个想象的框架
- 复制一个PCB——`task_struct`: `err = arch_dup_task_struct(tsk, orig);`
- 要给新进程分配一个新的内核堆栈

```
ti = alloc_thread_info_node(tsk, node);
tsk->stack = ti;
setup_thread_stack(tsk, orig); //这里只是复制thread_info，而非复制内核堆栈
```

















