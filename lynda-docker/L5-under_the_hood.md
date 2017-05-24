## The program docker

And now a little interlude to talk about what kernels do. Kernels are either, part of a corn, a respectable military rank, or, the core of every computer you interact with, depending on your perspective.

So a kernel runs directly on the hardware, and it has a bunch of jobs, most of which are pretty simple, and very important. It receives messages from the hardware, a new disk has been attached, a network packet arrived, everything that goes on electrically, bubbles up to the kernel and gets dealt with.

It starts and it schedules programs, it says what's allowed to run, what's when, and it lets your computer do all the things you're asking it to do at the same time. It controls and it organizes the storage devices on the computer.

It passes messages between programs, when two programs on the
computer want to communicate, or two programs on different computers want to communicate over a network, they ask the kernel to pass a message. The kernel passes the message, gets it ready, sends it over to the kernel on the other computer, which receives the message, gets it ready for the program, and sends it to the program over there.

It allocates resources, memory, time to actually do work on a CPU, how much network bandwidth to give to who, all of that stuff is managed by the kernel. And Docker is a program which manages the kernel.

So Docker is, well three things. It's a program written in Go, Go is a nice upcoming systems language, and its job is to manage several features of the kernel, and use these features to build the concept of containers and images.

So Docker primarily uses cgroups, or control groups, to group processes together, and give them the idea of being contained within their own little world, that's what keeps one container from interfering with another.

It uses namespaces, which is a feature of the Linux kernel which allows it to split the networking stack, so you have one set of addresses for one container, another set of addresses for another container, and other addresses for things that are not in containers at all.

It uses copy-on-write file systems and various other approaches to build the idea of images, to say you have this image, it doesn't change, but you can run stuff on top of it.

And, people have been doing this for years. Honestly, almost none of what Docker does is truly new, they took things that people were working very hard to do, and they made it easy, approachable, and they created a language around it for people to talk about it. And they made these things popular. So what Docker really does is make scripting distributed systems easy, and that's why it's taking off the way it is.

These things that used to be the realm of very large enterprises with enormous budgets, are now easily done on anyone's computer, of course, you have to have a fairly peculiar definition of the word easy.

So, Docker is divided into two programs, it's, the client, and the server. These two programs communicate over a socket, that can be a network socket, where the client is running on one computer, and the server is running on a computer somewhere on a cloud provider across the world, or they can be running directly on the same hardware, or they can be running on the same hardware, with the server in a virtual machine, which is the common case for people doing this course. 
In that case, the client communicates over a network, and sends messages to the Docker server to say, make a container, start a container, stop a container, that kind of stuff. When the client and server are running on the same computer, they can connect through a special file called a socket, and, since they can communicate through a file, and Docker can efficiently share files between hosts and containers, it means you can run the client, inside Docker itself.

```
What Kernel Do

- Respond to message from the hardware
- Start and schedule program
- Control and organize storage
- Pass messages between programs
- Allocate resources, memory, CPU, network and so on
- Create containers by Docker configuring the kernel


What Docker Does

- Program written in Go -- an upcoming systems language
- Manages kernel features
    Uses "cgroups" to contain processes
    Uses "namespaces to contain networks
    Uses "copy-on-write" filesystems to build images
- Used for years Docker
```

**So the traditional Docker scenario, with a single host, you have Docker the program, connects to the socket, sends commands to Docker the program, which is the server side, and that creates containers, or deletes containers, all the rest.**

But it's pretty easy to run the client inside one of the containers, and share the socket into that container, which allows the same messages to go through the same socket, get to the server running on the host, and do everything that it would do normally.

```
What Docker Really Does

- Make scripting distributed systems "easy"
    For a very peculiar definition of "easy"

The Docker Control Socket

- Docker is two programs: a client and a server
- The server receives commands over a socket(either over a network or through a "file")
- The client can even run inside docker itself
```

Running Docker Locally

![](http://okye062gb.bkt.clouddn.com/2017-05-24-143542.jpg)

Running the Client Inside Docker

![](http://okye062gb.bkt.clouddn.com/2017-05-24-145837.jpg)


```
➜  sydney docker-machine ssh
docker@default:~$ ls -l /var/run/docker.sock 
srw-rw----    1 root     docker           0 May 22 08:57 /var/run/docker.sock
# So it just looks like any other file, it's just a file and if you write commands into this file in the appropriate format, then the Docker server will do things.

# Now that we took a look at that socket, we don't actually have to be on the Docker host to do any of these further steps.
# Docker's an image provided by Docker the company, through Docker the registry, to allow you to run Docker in Docker. So, and we're gonna tell that container that we would like to run a shell.

➜  sydney docker run -ti -v /var/run/docker.sock:/var/run/docker.sock docker sh 
/ # uname -r
4.4.66-boot2docker
/ # docker run -ti debian bash
root@d4c63d974c18:/# 
```

So now I have created a container, using a client that was running in a container. This is not Docker in Docker, there's still just one server, I'm just creating more containers using a client that happens to be in a Docker container. The important part to understand here is that the client can be running just about anywhere, and if it can connect to the server, it can do anything that Docker can do otherwise.

This is one of the real key ideas that makes Docker work and has contributed to its growing popularity.


## Networking and namespaces

One of the main things Docker does is manage your networking for you to create containers.

Let's take a little brief look at some of the things Docker does for you. First of all, networking is divided into many layers. The bottom layer is how machines that are near each other or containers that are near each other actually talk directly to each other. We call this the Ethernet layer.

It moves little frames of data in a local area.

Above that, you have the Internet Protocol layer, or IP, and that's how data moves between networks and between systems in different parts of the world. Routing is how packets get into and out of networks.

Docker takes care of setting up that for you too. And ports. When we talk about ports throughout this course, we're talking about specific programs running on a specific computer, actually listening to traffic. So Docker uses bridges to create virtual networks inside your computer.

When you create a private network in Docker, it creates a bridge. These function like software switches. It's equivalent to having a little blue box on your desk and plugging a bunch of different wires into it, except it's all within your computer and you're plugging containers into it with virtual network wires.

So these are used to control the Ethernet layer, containers that actually talk directly to each other.


```
Networking in Brief

- Ethernet: moves "frames" on a wire(or WIFI)
- IP layer: moves packets on a local network
- Routing: forwards packets between networks
- Ports: address particular programs on a computer


Bridging

- Docker uses bridges to create virtual networks in your computer
- These are software switches
- They control the Ethernet layer
- You can turn off this protection with 
    `docker run --net=host options image-name command`

➜  sydney docker run --rm -ti --net=host debian bash
root@default:/# apt-get update && apt install bridge-utils
root@default:/# brctl show
bridge name bridge id       STP enabled interfaces
br-d2cf3788e237     8000.02426c2a8e72   no      
docker0     8000.02425fc89fb8   no

# Another terminal
➜  sydney docker network create my-new-network
12673434badd55d336587ccda9360f0bbb4592d73ab8e98732df9ffb638e14c0

root@default:/# brctl show
bridge name bridge id       STP enabled interfaces
br-12673434badd     8000.0242c8293383   no      
br-d2cf3788e237     8000.02426c2a8e72   no      
docker0     8000.02425fc89fb8   no
```

And we can this system has a couple of bridges on it. One called docker0, which is the virtual network used by all machines in Docker that don't have their own network.

If I go over to this other terminal, and create a new network, `docker network create my-new-network`. So Docker created the network there, and if I look at the bridges on here, I can see that a new network just showed up. 

So Docker isn't magically moving packets between containers. It's creating bridges by running commands to configure your system. And in that demo, I turned off the isolation that prevents containers from messing with the host's network by passing the `--net` equals host option.


So the next layer up is how Docker moves packets between networks and between containers and the internet. It uses the built-in firewall features of the Linux kernel, namely the IP tables command, to create firewall rules that control when packets get sent between the bridges, and thus become available to the containers that are attached to those bridges.

This whole system is commonly referred to as NAT, or Network Address Translation. That means when a packet is on its way out towards the internet, you change the source address so it'll come back to you. And then when it's on the way back in, you change the destination address so it looks like it came directly from the machine you were connecting to.


```
Routing

- Creates "firewall" rules to move packets between networks
- NAT
- Change the source address on the way out
- change the destination address on the way back in
- `sudo iptables -n -L -t nat`
- "Exposing" a port -- really "port forwarding"

➜  sydney docker-machine ssh
docker@default:~$ sudo iptables -n -L -t nat
Chain PREROUTING (policy ACCEPT)
target     prot opt source               destination         
DOCKER     all  --  0.0.0.0/0            0.0.0.0/0            ADDRTYPE match dst-type LOCAL

Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
DOCKER     all  --  0.0.0.0/0           !127.0.0.0/8          ADDRTYPE match dst-type LOCAL

Chain POSTROUTING (policy ACCEPT)
target     prot opt source               destination         
MASQUERADE  all  --  172.19.0.0/16        0.0.0.0/0           
MASQUERADE  all  --  172.18.0.0/16        0.0.0.0/0           
MASQUERADE  all  --  172.17.0.0/16        0.0.0.0/0           

Chain DOCKER (2 references)
target     prot opt source               destination         
RETURN     all  --  0.0.0.0/0            0.0.0.0/0           
RETURN     all  --  0.0.0.0/0            0.0.0.0/0           
RETURN     all  --  0.0.0.0/0            0.0.0.0/0   

# Terminal 2
➜  sydney docker run -ti -p 8080:8080 debian bash 
root@48fc7b10a14f:/# 

docker@default:~$ sudo iptables -n -L -t nat
Chain PREROUTING (policy ACCEPT)
target     prot opt source               destination         
DOCKER     all  --  0.0.0.0/0            0.0.0.0/0            ADDRTYPE match dst-type LOCAL

Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
DOCKER     all  --  0.0.0.0/0           !127.0.0.0/8          ADDRTYPE match dst-type LOCAL

Chain POSTROUTING (policy ACCEPT)
target     prot opt source               destination         
MASQUERADE  all  --  172.19.0.0/16        0.0.0.0/0           
MASQUERADE  all  --  172.18.0.0/16        0.0.0.0/0           
MASQUERADE  all  --  172.17.0.0/16        0.0.0.0/0           
MASQUERADE  tcp  --  172.17.0.2           172.17.0.2           tcp dpt:8080

Chain DOCKER (2 references)
target     prot opt source               destination         
RETURN     all  --  0.0.0.0/0            0.0.0.0/0           
RETURN     all  --  0.0.0.0/0            0.0.0.0/0           
RETURN     all  --  0.0.0.0/0            0.0.0.0/0           
DNAT       tcp  --  0.0.0.0/0            0.0.0.0/0            tcp dpt:8080 to:172.17.0.2:8080
```

Namespaces are a feature in the Linux kernel that allows you to provide complete network isolation to different processes in the system. So it enforces the rule that you're not allowed to mess with the networking of other processes.

Processes running in containers are attached to virtual network devices. And those virtual network devices are attached to bridges, which lets them talk to any other containers attached to the same bridges. This is how it creates the virtual networking.

But each container has its own copy of all of the Linux networking stack. All of the different pieces that make up the networking are isolated to each container, so that they can't do things like reach in and reconfigure other containers.

Namespaces enforce the rules of Docker and keep containers safe from each other.

```
Namespaces

- They allow processes to be attached to private network segments
- These private networks are bridged into a shared network with the rest of the containers
- Containers have virtual network "cards"
- Containers get their own copy of the networking stack
```

