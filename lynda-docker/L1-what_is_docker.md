###What is does?

**Docker carves up a running Linux system into small containers that run your code,** each of which is its own sealed little world with its own programs and its own everything all isolated from anything.

These containers are designed to be portable so they can be shipped from one place to another. And Docker does the work of getting these containers to and from your systems.

Docker also builds these containers for you and it's a social platform to help you find and share containers with others who may have already built very similar work that you can build on top of and let's get it up front that Docker is not virtual machines.


**There's only a single operating system running. That operating system is just carved up into isolated little spaces.**


```
What Docker Does?

- Carves up a computer into sealed containers that run your code
- Gets the code to and from your computers
- Builds these containers for you
- Is a social platform for you to find and share containers, which are different from virtual machines
```


<hr>


**A container is a self-contained sealed unit of software. It has everything in it that is needed to run that code.** Batteries included, operating system included. It has all of the code, all of the configs, contains all the processes within that container, it has all of the networking to allow these containers to talk to the other containers they're supposed to be able to talk to and nothing else. It has all the dependencies that your system needs bundled up in that container and it even includes just enough of the operating system to run your code.

So the way it works, **it takes all the services that make up a Linux server, networking, storage, code, interprocess communication, the whole works and it makes a copy of that in the Linux kernel for each container.**

So each container has its own little world that it can't see out of and other containers can't see in. You might have one container on a system running Red Hat Linux serving a database through a virtual network to another container running Ubuntu Linux running a web server that talks to that database and that web server might also be talking to a caching server that runs in a SUSE Linux-based container.

![](http://okye062gb.bkt.clouddn.com/2017-05-22-053450.jpg)

The important part to understand is it doesn't matter which Linux each container is running on, it just has to be a Linux and Docker is the program which manages all of this, sets it up, monitors it, and tears it down when it's no longer needed.


```
What is a Container?

- A self-contained sealed unit of software
- Contains everything required to run the code
- Includes batteries and operating system

A container includes:
- Code
- Configs
- Processes
- Networking
- Dependencies
- Operating system
```


<hr>


Docker is a client program named Docker. It's a command you type at the terminal. It's also a server program that listens for messages from that command and manages a running Linux system.

Docker has a program, which builds containers from code. It takes your code along with its dependencies and bundles it up and then seals it into a container and it's a service that distributes these containers across the Internet and makes it so you can find others' work and the right people can find your work.

It is also a company that makes all of these.


```
About Docker

- A client program named Docker
- A server program that manages a Linux system
- A program that builds containers from code
- A service that distributes containers
- A company that makes containers
```

