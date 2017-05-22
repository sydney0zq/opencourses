##The Docker Flow Images to containers

Now that we've got Docker installed, and talked a little bit about what Docker is, let's talk about what Docker does. 

**The Docker Flow, the fundamental concept, in Docker, it all begins with an image. An image is every file that makes up just enough of the operating system to do what you need to do. Traditionally you'd install a whole operating system with everything for each application you do.**

With Docker you pair it way down so that you have a little container with just enough of the operating system to do what you need to do, and you can have lots and lots of these efficiently on a computer.

So let's take a look at Docker images. Amazingly, creatively, the command to look at your Docker images is `docker images`. 

```
➜  ~ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
debian              latest              3e83c23dba6a        13 days ago         124MB
```

The repository for the image is where it came from; Tag is the version of it, in this case it's tagged latest, and then there's image ID which is the internal Docker representation of this image.

So you could always refer to this image by the combination of it's name and it's tag, debian:latest, in any Docker command, or you can refer to it by its number. It's useful to be able to refer to them by number because sometimes they don't have a name, they don't have to but if they do have a name it's a little more convenient to use it.

Now what good is an image if not to do something with it?

The `docker run` command takes an image and turns it into a living running container with a process in it.

![](http://okye062gb.bkt.clouddn.com/2017-05-22-093017.jpg)

So let's take a look at running an image to make a container. So now that I've got my image, I want to actually run something in it, so I'm gonna use `docker run -ti debian`. `ti` stands for terminal interactive, it just causes it to have a full terminal within the image so that you can run the shell and get things like tab completion and formatting to work correctly.

When you're running commands by typing on a keyboard inside an image, this is a very useful flag to put in, most of the other times you don't need it. And then we in a debian environment. 

So our container, the running container has an ID, which is different than the image ID that was used to run it from, these are not the same thing. Images have one set of IDs, containers have their own sets of IDs, they don't overlap, and there's no place in Docker where you can interchange image and container IDs, at least not that I know of.

When you're inside a container you start from an image, and that image is fixed, it doesn't change.

当我们在一个image中建立了一个文件, 再退出或者从别的terminal登录, 这个文件消失。

Files go into containers, but that doesn't put them back into the image that the container came from. They stay in that container.


## The docker flow containers to images

**So we can see we went from an image to a running container, when we ran that container again, we got the same thing we got the first time, and that's the whole point of images is they are fixed points where you know everything's good and you can always start from there.**

Now when you've got a running container, you make changes to that container, you put files there. It's very useful when you want to be able to actually save those.

The next step in the docker flow is a stopped container. So the container that's running, it's alive, it has a process in it. When that process exits, the container's still there, so that file I created a moment ago, when I exited that container, it's still there. I can go back and find it, it didn't get deleted, it's just that it's currently in a stopped container.

![](http://okye062gb.bkt.clouddn.com/2017-05-22-095249.jpg)

So I can look at the most recently exited container with the `docker ps` command. Just like I do when I want to look at the running containers except stopped containers don't show up by default.

To see stopped containers, I can specify the `-a` argument to see all containers, a for all, and if I just want to see the last container to exit, I can do `docker ps -l`.

```
➜  ~ docker ps -a --format $FORMAT

ID  06da598ba364
IMAGE   debian:latest
COMMAND "bash"
CREATED 15 minutes ago
STATUS  Exited (0) 12 minutes ago
PORTS   
NAMES   tender_ride


ID  61d297ec4366
IMAGE   debian
COMMAND "/bin/bash"
CREATED 24 minutes ago
STATUS  Exited (127) 14 minutes ago
PORTS   
NAMES   suspicious_darwin


ID  ae8497e70d20
IMAGE   debian
COMMAND "/bin/bash"
CREATED 24 minutes ago
STATUS  Exited (0) 23 minutes ago
PORTS   
NAMES   focused_bell


ID  ca27e4224243
IMAGE   debian
COMMAND "/bin/bash"
CREATED About an hour ago
STATUS  Exited (127) 45 minutes ago
PORTS   
NAMES   modest_swirles
```

Looking at these exit codes can be good clue as to why a container died, if you expected a container to be running and you find it to be stopped for some reason, this can often give you a clue, right?

Alright now say I've got a stopped container that has a file in it I want to use for the future. I started from a base image, I installed my own software, I've got a container that has my software installed on it.
The next step is the `docker commit` command.

**That takes containers and makes images out of them.** It doesn't delete the container, the container is still there, now we have an image with the same content that was in that container. So `docker run` and `docker commit` **are complementary to each other**, `docker run` takes images to containers and `docker commit` takes containers back to new images. It doesn't overwrite the image that the container was made from. So now we can make a new image.

![](http://okye062gb.bkt.clouddn.com/2017-05-22-095911.jpg)

```
➜  ~ docker run -ti debian bash   
root@86af2226bbad:/# touch MY_FILE_HERE
root@86af2226bbad:/# ls
MY_FILE_HERE  bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@86af2226bbad:/# exit
➜  ~ docker ps -l --format $FORMAT

ID  86af2226bbad
IMAGE   debian
COMMAND "bash"
CREATED About a minute ago
STATUS  Exited (0) 21 seconds ago
PORTS   
NAMES   jolly_franklin

➜  ~ docker commit 86af2226bbad
sha256:9f88fc73f1c7673fe6368be6d65571fd7010a75657b9d5b040f1b520664524ef
```

I just got an image ID(sha256) out of it. Looks very different from a container ID. Now I have made a new image. The original ubuntu image is unchanged, I have a new image and it just has a big number not very convenient. So the last step in the docker flow is the tag command to give images names.

```
➜  ~ docker tag sha256:9f88fc73f1c7673fe6368be6d65571fd7010a75657b9d5b040f1b520664524ef test_image
➜  ~ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
test_image          latest              4f47361274fc        About a minute ago   124MB
<none>              <none>              9f88fc73f1c7        11 minutes ago       124MB
debian              latest              3e83c23dba6a        13 days ago          124MB
➜  ~ docker run -ti test_image bash
➜  ~ docker commit jolly_franklin(这里是images里面的NAMES字段) test_image_2
➜  ~ docker run -ti test_image_2
```

And it has my important file in it, committing images and then tagging them is such as common pattern that it's actually built right into the docker commit command. So you can skip the steps about copying the image name over to a docker tag command and just run docker commit.

The name of the container, it's nice human readable name and then you can as the next argument, say the name you'd like it to be tagged as. This is the format you should probably use in all of your day to day life, there's no reason to go through the extra step of doing a commit then running docker tag, but it is very important to understand that that's what's happening under the hood.


## Run processes in containers

Now that we've got the docker flow in mind, let's talk about running things in docker because that's what it's all about.

**So, to start off, we have the most important command, `docker run`. It starts a container by giving an image name and a process to run in that container.**

There is a main process to a container. When that process exits, the container is done. The container is not done until that process exits. **If you start other processes in the container later, the container still exits when that main process finishes.** So docker containers have one main process, and they can have names. You don't give it a name, it'll make one up.

```
Running Things in Docker
`docker run`

- Containers have a main process
- The container stops when that process stops
- Containers have names
```

**`docker run --rm` is a very common command, lots of people us it all the time when you just wanna run something in your container, but you don't wanna keep the container afterwards.** That says delete this container when it exits. Otherwise we have to do extra stuff. This saves a step.

```
➜  ~ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
test_image          latest              6616faa93427        7 minutes ago       124MB
➜  ~ docker run --rm -ti test_image sleep 5
➜  ~ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
test_image          latest              6616faa93427        8 minutes ago       124MB

➜  ~ docker run -ti test_image bash -c "sleep 2; echo all done" 
all done
```

Now let's talk about leaving things running in a container. Docker has the idea of detached containers. You can start a container running and just let it go. But this time I'm going to put in a `-d` for detach.

So that's gonna start this thing running, and leave it running in the background. It prints out an identifier, by which you can go and find it. You don't have to use that identifier. You can also see it by running the `docker ps` command.

```
➜  ~ docker run -d -ti test_image bash
a79cdefb42c1be0b04a5ed62e1f2a019374abf7db23c6705584ca161897b0c2f
➜  ~ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
a79cdefb42c1        test_image          "bash"              8 minutes ago       Up 14 seconds                           wonderful_galileo
➜  ~ docker attach wonderful_galileo
root@a79cdefb42c1:/# 
```

If you hit control P, control Q, it exits you out of the container by detaching you from it, but leaves it running, so that you can attach back again and pick up where you left off. 

```
Leaving Things Running in a Container
`docker attach`
➜  ~ docker ps
➜  ~ docker attach *container_name*

Running More Things in a container
`docker exec`
- Start another process in an existing container
- Great for debugging and DB administration
- Cannot add ports, volumes, and so on
```

Now let's say you wanna run more things in a container. You started a container, it's got something running, and you want to add another process to a running container. This is really good for debugging. Your container is acting up, you just want to jump in there, figure out why.

You just start a process in it. you can't use it add more ports, or volumes, or any of the other stuff that you can do with docker run.

```
#Terminal 1
root@a79cdefb42c1:/#

#Terminal 2
➜  ~ docker exec -ti wonderful_galileo bash
```

Now, when the original container exits, which I'll do by pressing control D over here, **my attached process that I had exec in there with, that died with the original container.**























