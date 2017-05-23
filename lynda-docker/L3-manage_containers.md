##Manage containers

Looking at the container output, of a container that's already finished, is something that can be very frustrating.

You start up a container, it didn't work, you want to find out what went wrong. The `docker logs` command is key for this. Docker keeps the output of the container available, it keeps it around as long as you keep the container around, and you can use `docker logs container_name`, to look at what the output was.


```
Looking at Container Output
`docker logs`

- Keep the output of containers
- View with `docker logs container_name`
- Don't let the output get too large


➜  ~ docker run --name test -d debian bash -c "lose /etc/passwd"
8e675fac331a2e321b280d5634796c21c18c8c6c80feba0dd8543da182d0d851
➜  ~ docker logs test
bash: lose: command not found
```

And, then I go fix it. Don't let the output of your docker containers get really really huge.

This is one of those side effects of convenience, it's very convenient being able to go back and look at it. And, if you're writing tons and tons of data to the output of the process in your docker container, you can really bog down docker to the point where your whole system becomes unresponsive.


```
Stopping and Removing Containers

- Killing and removing containers
    `docker kill container_name`    #make it stop
    `docker rm container_name`      #make it be gone


#Terminal 1
➜  ~ docker run -ti debian
root@73b8f3c9d327:/#

#Terminal 2
➜  ~ docker ps --format $FORMAT
ID  73b8f3c9d327
IMAGE   debian
COMMAND "/bin/bash"
CREATED 8 minutes ago
STATUS  Up 22 seconds
PORTS   
NAMES   distracted_ride

➜  ~ docker kill distracted_ride
distracted_ride
➜  ~ docker ps -l --format $FORMAT
ID  73b8f3c9d327
IMAGE   debian
COMMAND "/bin/bash"
CREATED 8 minutes ago
STATUS  Exited (137) 15 seconds ago
PORTS   
NAMES   distracted_ride

#When you're using containers with fixed names, 
#if you later want to start another container with the same name, 
#you'll very often get an error saying, "That container already exists,
#you can't use that name."
#And it's cause you need to go through an rm to remove the old container. Stopped containers still exist until you explicitly remove them.

➜  ~ docker rm distracted_ride
distracted_ride
```

<hr>

One of the big features of docker is the ability to enforce limits on how many resources a container is gonna use. You can limit it to a fixed amount of memory, you can say docker run dash dash memory maximum allowed memory and that prevents runaway containers from clobbering the rest of the system.

You can equally limit the CPU time, you can limit **relative**, you can say give this container half of the total CPU time and the other one the other half so that if one's not busy the other can use more CPU. But, then it will enforce that they have equal access.

You can also give them hard limits. Say, this container only gets to use 10 percent of the CPU total ever, even if 90 percent of the CPU time is idle.

Most of the orchestration systems, that are covered in a later chapter, generally require you to state the limits of a particular task or container.

Now, a few lessons from my bad experiences and my good.
Lesson One, **don't let your containers fetch their dependencies when they start**. If you're using things like node.js and you have your node starts up, and then when the container starts it fetches its dependencies. Then, someday somebody's gonna remove some library out from the node repos, and all of a sudden all your containers just stop throughout your whole system. Fetch, make your containers include their dependencies inside the container themselves. Saves a lot of pain.

Also, from a sort of different perspective, little security hat here. **Don't leave important things in unnamed stopped containers.** Don't do a week's worth of work and just leave it sitting in a stopped container on your laptop. Because, you'll inevitably come along and say, "My disk is full, ah, I gotta clean up some stopped containers." and then delete the seemingly unimportant container, and then your important stuff is gone. So, be careful what you leave sitting around in unnamed containers.

```
Resource Constraints

- Memory limits
    `docker run --memory maximum-allowed-memory image-name command`
- CPU limits
    `docker run --cpu-shares` relative to other containers
    `docker run --cpu-quota` to limit it in general
- Orchestration
    Generally requires resource limiting

Lessons from the Field

- Don't let your containers fetch dependencies when they start
- Don't leave important things in unamed stopped containers
```


## Network between containers

Now that we've learned how to stop and start containers and clean up after ourselves, let's go on to making containers talk to each other. This is kind of where Docker gets exciting.

So let's talk networking. Docker provides a private network for use by the containers on your system. In fact, you can have several private networks so you can split things up nicely. **You can group your containers into these private networks where all of your stuff related to one thing is in one private network and an unrelated service doesn't have to worry about interfering with that or being snooped upon.**

You explicitly set, when you run Docker, who can talk to whom and on what ports, and this is done by explicitly exposing ports and linking containers.

Also, when you've exposed ports and containers and all of that, Docker has a good mechanism for helping these containers find each other and make the connection. So how to expose a particular port so that connections can come into your container. **So you can explicitly specify the port on the inside of the container that can be explicitly exposed to a particular port on the outside of the container.**

```
Private Container Networking

- Programs in containers are isolated from the Internet by default
- You can group your containers into "private" networks
- You explicitly choose who can connect to whom
- This is done by "exposing" ports and "linking" containers
- Docker helps you find other exposed ports with Compose services
```

And this is the new part. I have a -p, which stands for port, that says I would like to expose port `45678` on the inside of the container to the outside of the container as port `45678`.

So this says I want the program listening on port `45678` inside the container to be reachable from outside the container by just going to that host on port `45678`, and then it'll get forwarded into the container and the connection will be made.

I'm also going to forward another port, port `45679`. And I'm going to keep the port the same for this one, too, so that these two ports just forward right into the container.


`netcat -lp` stands for listen port, and I'm going to have it listen on port 45678, that first port we forwarded into this container. And so that will just listen on that port, and when everyone connects, it's going to print it out. I'm going to take that output and pipe it using the pipe operator into another copy of `netcat`, and this other copy of netcat is going to listen on port 45679, which is that second port we've forwarded into the container.

So you see I've got, data's going to come in on one port, get forwarded to a process, and go out on the other port. So we're making ourselves a little relay.

![](http://okye062gb.bkt.clouddn.com/2017-05-23-015827.jpg)

```
Exposing a Specific Port

- Explicitly specifies the port inside the container and outside
- Expose as many ports as you want
- Require coordination between containers
- Make it easy to find the exposed ports

➜  ~ docker run --rm -ti -p 45678:45678 -p 45679:45679 --name echo-server debian bash
root@a089ea2b2611:/#
```

Docker has a nice command that makes it easy to find exposed ports. So you can expose ports dynamically. That way you don't have to worry about conflicts in advance and not being able to run a container 'cause some other container's using that port.

So you fix the port inside the container. The program inside the container always listens on the same port, but from the outside of the container, it just gets whatever port is next available. It's always guaranteed to get at least one port.

I'm going to change it so that instead of specifying both the inside and the outside port, I'm going to specify only the inside port and let the outside port be chosen dynamically.


```
Exposing Ports Dynamically

- The port inside the container is fixed
- The port on the host is chosen from the unused ports
- This allows many containers running programs with fixed ports
- This often is used with a service discovery program

#Terminal 1
➜  ~ docker run --rm -ti -p 45678 -p 45679 --name echo-server debian bash
root@3144f8031fd8:/# 

#Terminal 2
➜  ~ docker port echo-server
45679/tcp -> 0.0.0.0:32768
45678/tcp -> 0.0.0.0:32769


Exposing UDP Ports

- `docker run -p outside-port:inside-port/protocol(tcp/udp)
- `docker run -p 1234:1234/udp``
```

