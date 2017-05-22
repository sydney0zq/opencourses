##Installing Docker

Docker's main job is to manage a Linux server and start containers on it.

When you're running on a Mac or Windows, most people use a Linux Virtual Machine, running on their computer for this purpose. Docker Toolbox, which we'll be installing shortly, has some great tools for managing this process. If you happen to have an old version of Boot2Docker installed, you may need remove it first if you encounter problems.


```
Installation

- Docker needs a Linux server to manage
- Many people use a virtual machine on their laptop
- Docker Toolbox helps run this Linux virtual machine
- If you have Boot2Docker installed, you must remove it first
```

<hr>


And now a brief overview of the installation process. We start with Your Computer. This is the thing you're physically typing on.

On that, Docker Toolbox will install a program called Docker that lets you manager Docker Virtual Machines and do everything else that Docker does.

It also installs a program named VirtualBox for managing virtual machines. If you happen to have VirtualBox already installed, Docker Toolbox will use it. In the rare event that you have a very old version of VirtualBox installed and you run into problems, you may need to uninstall that before you start the installation, only if you have problems.

Docker Toolbox will install a program called **Docker Machine**, and Docker Machine manages a Linux Virtual Machine on your computer.

**Inside that Linux Virtual Machine is the server side of the Docker program. So when you type Docker at your Command Prompt, it will send that command into the Linux Virtual Machine over the network and to the Docker server running there.**

![](http://okye062gb.bkt.clouddn.com/2017-05-22-083905.jpg)

Now let's take a brief look at how to use Docker. First run **Docker Quickstart Terminal. This will cause Docker machine to start up your Docker machine if it's not already running and bring up a terminal configured to connect to your virtual machine**. It prints up there the IP Address of the machine it's currently connecting to.

So after you start Docker Quickstart Terminal, you can just run Docker commands. 

`docker run hello-world.`

Docker Toolbox also installed Docker Machine, which has several useful commands for managing your Linux Virtual Machine. Some of these are used more often than others.

You definitely need know about `docker-machine start`, which starts your machine, and docker-machine stop, which kills it.

Also, `docker-machine ip` prints out the IP address of the machine that it's currently connected to, and `docker-machine ssh` connects to that machine and gives you a command prompt.

Another useful command to know about is `docker-machine scp` for copying files into and out of your virtual machine and docker-machine upgrade, which will install the latest version of Docker into your virtual machine.

When in doubt, if you run into problems following along with this course, try `docker-machine upgrade` and `docker-machine restart` to get things back on track.


## Install docker on Mac

1. Go to <https://www.docker.com/products/docker-toolbox> to download
2. Open `docker Quickstart Terminal` to start(It takes time)
3. Try `docker info` and `docker run -ti debian`
4. So we can get a debian running(Amazing)


## Install docker on Windows

1. Go to <https://www.docker.com/products/docker-toolbox> to download
2. Make sure your `virtualization` is enabled (check Task Manager-CPU)
3. Open `docker Quickstart Terminal` to start(It takes time)
4. Run `docker run --net=host -ti debian bash` 


## Install docker on Linux

Installing Docker directly on a Linux machine is slightly easier than installing it on a Mac or Windows because there's no need to set up virtual machines to run the server side of it.

Just search on Internet for answer.

