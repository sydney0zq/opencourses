Python 初学者对装饰器的理解存在困扰，我认为本质上是对 Python 函数理解不到位，Python 函数不同于其他编程语言，它可以作为第一类对象使用，这是关键。因为装饰器本质上还是函数，所以我们从函数开始说起

### 函数定义

先从一个最简单函数定义开始：

```
def foo(num):
    return num + 1
```

上面定义了一个函数，名字叫`foo`，也可以把 `foo` 可理解为变量名，该变量指向一个函数对象

![](http://okye062gb.bkt.clouddn.com/2017-06-19-134738.png)

调用函数只需要给函数名加上括号并传递必要的参数（如果函数定义的时候有参数的话）

```
value = foo(3)
print(value) # 4
```

变量名 `foo` 现在指向 `<function foo at 0x1030060c8>` 函数对象，但它也可以指向另外一个函数。

```
def bar():
    print("bar")
foo = bar
foo() # bar
```

![](http://okye062gb.bkt.clouddn.com/2017-06-19-134739.png)

### 函数作为返回值

在 Python 中，一切皆为对象，函数也不例外，它可以像整数一样作为其它函数的返回值，例如：

```
def foo():
    return 1

def bar():
    return foo

print(bar()) # <function foo at 0x10a2f4140>

print(bar()()) # 1 
# 等价于
print(foo()) # 1
```

调用函数 bar() 的返回值是一个函数对象 <function foo at 0x10a2f4140>，因为返回值是函数，所以我们可以继续对返回值进行调用（记住：调用函数就是在函数名后面加`()`）调用`bar()()`相当于调用 `foo()`，因为 变量 foo 指向的对象与 bar() 的返回值是同一个对象。

![](http://okye062gb.bkt.clouddn.com/2017-06-19-134740.png)

### 函数作为参数

函数还可以像整数一样作为函数的参数，例如：

```hljs
def foo(num):
    return num + 1

def bar(fun):
    return fun(3)

value = bar(foo)
print(value)  # 4
```

函数 `bar` 接收一个参数，这个参数是一个可被调用的函数对象，把函数 `foo` 传递到 `bar` 中去时，foo 和 fun 两个变量名指向的都是同一个函数对象，所以调用 fun(3) 相当于调用 foo(3)。

![](http://okye062gb.bkt.clouddn.com/2017-06-19-134741.png)

### 函数嵌套

函数不仅可以作为参数和返回值，函数还可以定义在另一个函数中，作为嵌套函数存在，例如：

```hljs
def outer():
    x = 1
    def inner():
        print(x)
    inner()

outer() # 1
```

`inner`做为嵌套函数，它可以访问外部函数的变量，调用 outer 函数时，发生了 3 件事：

1.  给 变量 `x` 赋值为 1
2.  定义嵌套函数 `inner`，此时并不会执行 inner 中的代码，因为该函数还没被调用，直到第 3 步
3.  调用 inner 函数，执行 inner 中的代码逻辑。

### 闭包

再来看一个例子：

```hljs
def outer(x):
    def inner():
        print(x)

    return inner
closure = outer(1)
closure() # 1
```

同样是嵌套函数，只是稍改动一下，把局部变量 x 作为参数了传递进来，嵌套函数不再直接在函数里被调用，而是作为返回值返回，这里的 closure 就是一个闭包，本质上它还是函数，闭包是引用了自由变量(x)的函数(inner)。

### 装饰器

继续往下看：

```hljs
def foo():
    print("foo")
```

上面这个函数这可能是史上最简单的业务代码了，虽然没什么用，但是能说明问题就行。现在，有一个新的需求，需要在执行该函数时加上日志：

```hljs
def foo():
    print("记录日志开始")
    print("foo")
    print("记录日志结束")
```

功能实现，唯一的问题就是它需要侵入到原来的代码里面，把日志逻辑加上去，如果还有好几十个这样的函数要加日志，也必须这样做，显然，这样的代码一点都不 Pythonic。那么有没有可能在不修改业务代码的提前下，实现日志功能呢？答案就是装饰器。

```hljs
def outer(func):
    def inner():
        print("记录日志开始")
        func() # 业务函数
        print("记录日志结束")
    return inner

def foo():
    print("foo")

foo = outer(foo) 
foo()
```

我没有修改 foo 函数里面的任何逻辑，只是给 foo 变量重新赋值了，指向了一个新的函数对象。最后调用 foo()，不仅能打印日志，业务逻辑也执行完了。现在来分析一下它的执行流程。

这里的 outer 函数其实就是一个装饰器，装饰器是一个带有函数作为参数并返回一个新函数的闭包，本质上装饰器也是函数。outer 函数的返回值是 inner 函数，在 inner 函数中，除了执行日志操作，还有业务代码，该函数重新赋值给 foo 变量后，调用 foo() 就相当于调用 inner()

foo 重新赋值前：

![](http://okye062gb.bkt.clouddn.com/2017-06-19-134743.png)

重新赋值后，foo = outer(foo)

![](http://okye062gb.bkt.clouddn.com/2017-06-19-134745.png)

另外，Python 为装饰器提供了语法糖 **@**，它用在函数的定义处：

```hljs
@outer
def foo():
    print("foo")

foo()
```

这样就省去了手动给`foo`重新赋值的步骤。

到这里不知你对装饰器理解了没有？当然，装饰器还可以更加复杂，比如可以接受参数的装饰器，基于类的装饰器等等。
