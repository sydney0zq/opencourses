##Basic

<https://blog.ansheng.me/article/python-full-stack-way-basics/>

Python唯一的缺点就是他的性能，它达不到像C和C++这种编译性语言运行的那么快，但是我们通常都不需要考虑这个问题，因为有PYPY，它的运行速度比默认的Cpython要快很多。

###Python实现方式

Python身为一门编程语言，但是他是有多种实现方式的，这里的实现指的是符合Python语言规范的Python解释程序以及标准库等。

Python的实现方式主要分为三大类:

- Cpython
- Jpython
- IronPython


####CPython

Cpython是默认的Python解释器，这个名字根据它是可移植的ANSI C语言代码编写而成的这事实而来的。

当执行Python执行代码的时候，会启用一个Python解释器，将源码(.py)文件读取到内存当中，然后编译成字节码(.pyc)文件，最后交给Python的虚拟机(PVM)逐行解释并执行其内容，然后释放内存，退出程序。

![](http://okye062gb.bkt.clouddn.com/2017-05-04-UNADJUSTEDNONRAW_thumb_d09.jpg)

当第二次在执行当前程序的时候，会先在当前目录下寻找有没有同名的pyc文件，如果找到了，则直接进行运行，否则重复上面的工作。

pyc文件的目的其实就是为了实现代码的重用，为什么这么说呢？因为Python认为只要是import导入过来的文件，就是可以被重用的，那么他就会将这个文件编译成pyc文件。

python会在每次载入模块之前都会先检查一下py文件和pyc文件的最后修改日期，如果不一致则重新生成一份pyc文件，否则就直接读取运行。


####Jython

Jython是个Python的一种实现方式，Jython编译Python代码为Java字节码，然后由JVM（Java虚拟机）执行，这意味着此时Python程序与Java程序没有区别，只是源代码不一样。此外，它能够导入和使用任何Java类像Python模块。


####IronPython

IronPython是Python的C#实现，并且它将Python代码编译成C#中间代码（与Jython类似），然后运行，它与.NET语言的互操作性也非常好。


####指定字符编码

python制定字符编码的方式有多种，而编码格式是要写在解释器的下面的，常用的如下面三种:

```
# _*_ coding:utf-8 _*_
# -*- coding:utf-8 -*-
# coding:utf-8
```

####变量

在Python中变量是如何工作的？

1. 变量在他第一次赋值时创建;
2. 变量在表达式中使用时将被替换它们所定义的值;
3. 变量在表达式中使用时必须已经被赋值，否则会报`name 'xxx' is not defined`;
4. 变量像对象一样不需要在一开始进行声明;


==================


Exercise: 用户登陆

需求：写一个脚本，用户执行脚本的时候输入用户名和密码，如果用户米或者密码连续三次输入错误则退出，如果输入正确则显示登陆成功，然后退出。

![](http://okye062gb.bkt.clouddn.com/2017-05-04-053809.jpg)

