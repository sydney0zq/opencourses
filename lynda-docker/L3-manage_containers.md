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

