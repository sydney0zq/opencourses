##Images

We've used quite a few images thus far through this course, and now let's spend a little bit of time talking about how to manage and keep track of the images we're working with. So you can list the images that you've already downloaded with the docker images command. It only lists the images you've already downloaded.

**Because these images share a great deal of their underlying data, you don't sum up the sizes here to get the total amount of space the docker's using.** In this case, all of these 122 megabyte images here are actually the same 122 megabytes, with different names on them. Docker is much more space efficient than it would look like just from looking at this list. So don't get scared by that.

```
Listing Images

- `docker images`
- Lists downloaded images

Tagging Images

- Tagging gives images names
- `docker commit` tags images for you
- This is an example of the name structure
    `registry.example.com:port/organization/image-name:version-tag`
- You can leave out the parts you don't need
- `Organization/image-name` is often enough

➜  ~ docker ps -l --format $FORMAT
ID  85d6534fae95
IMAGE   test_image
COMMAND "/bin/bash"
CREATED 7 minutes ago
STATUS  Exited (0) 12 seconds ago
PORTS   
NAMES   practical_almeida
➜  ~ docker commit 85d6534fae95 demo_image:v0.1
sha256:e1712e31297e22dca45a9bd094880ecdc271920a3949b7fe7bdfed3619f9b9af
➜  ~ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
demo_image          v0.1                e1712e31297e        7 minutes ago       134MB
```

Now images can build up very quickly. One time I cleared out all the old images on a server and freed up 500 gigabytes. So if you're not careful, they can build up.

The `docker rmi` command for remove image, takes the image name and the tag and just removes it from your system.



```
Getting Images

- `docker pull`
- Run automatically by `docker run`
- Useful for offline work
- Opposite: `docker push`

Cleaning Up

- Images can accumulate quickly
    `docker rmi image-name:tag`

➜  ~ docker rmi demo_image:v0.1
Untagged: demo_image:v0.1
Deleted: sha256:e1712e31297e22dca45a9bd094880ecdc271920a3949b7fe7bdfed3619f9b9af
```

##Volumes

Let's talking about sharing data between containers and between containers and hosts. Docker offers this feature called volumes. Volumes are sort of like shared folders.

They're virtual disks that you can store data in and share them between the containers and between containers and the host or both.

So they have two main varieties of volumes, these virtual discs, available within Docker. **You've got persistent ones, where you can put data there, and it will be available on the host, and when the container goes away, the data will still be there. And you have ephemeral volumes. These exist as long as the container is using them. But when no container is using them, they evaporate. So they're sort of ephemeral.**

They'll stick around as long as they're being used but they're not permanent. These are not part of images. No part of volumes will be included when you download an image and no part of volumes is gonna be involved if you upload an image. They're for your local data, local to this host.

```
Volumes

- Virutal "discs" to store and share data
- Two main varieties
    Persistent
    Ephemeral
- Not part of images
```

So first let's talk about sharing data between the host and a container. These are kind of like shared folders you're used to when working with virtual machine systems such as Virtualbox.

For these examples, if you're running on a Mac or Windows, we're gonna be talking about sharing data between your Linux host and the containers running in it.

```
Sharing Data with the Host

- "Shared folder" with the host
- Sharing a "single file" into a container
- Note that a file must exist before you start the container, or it will be assumed to be a directory

➜  ~ docker-machine ssh
                        ##         .
                  ## ## ##        ==
               ## ## ## ## ##    ===
           /"""""""""""""""""\___/ ===
      ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
           \______ o           __/
             \    \         __/
              \____\_______/
 _                 _   ____     _            _
| |__   ___   ___ | |_|___ \ __| | ___   ___| | _____ _ __
| '_ \ / _ \ / _ \| __| __) / _` |/ _ \ / __| |/ / _ \ '__|
| |_) | (_) | (_) | |_ / __/ (_| | (_) | (__|   <  __/ |
|_.__/ \___/ \___/ \__|_____\__,_|\___/ \___|_|\_\___|_|
Boot2Docker version 17.05.0-ce, build HEAD : 5ed2840 - Fri May  5 21:04:09 UTC 2017
Docker version 17.05.0-ce, build 89658be
docker@default:~$ mkdir demo
docker@default:~$ docker run -ti -v /home/docker/demo:/shared-folder debian bash
root@6dc7f17e632e:/# ls
bin   dev  home  lib64  mnt  proc  run   **shared-folder**  sys  usr
boot  etc  lib   media  opt  root  sbin  srv        tmp  var
root@6dc7f17e632e:/# cd shared-folder/
root@6dc7f17e632e:/shared-folder# touch DATAFILE
root@6dc7f17e632e:/shared-folder# exit
docker@default:~$ ls demo/
DATAFILE
```

So this data, because it was shared with the host, survived past the container that it was run in. For sharing a single file, it's actually just the same. Just past the path to the file instead of the path to a folder and it shares a file.

Just one little trick is make sure that the file exists before you start the container or Docker will assume that it's going to be a folder and share it as a folder.


Alright, now let's talk about the more interesting case of sharing data between containers. This introduces the new argument to `docker run` called `volumes-from`. These are shared discs that exist only as long as they are being used. And when they're shared between containers, they'll be common for the containers that are using them.

So I'm creating a volume for this container which is not shared with the host. Notice how I didn't run Docker machine - ssh this time. I'm just running this from my Mac.

```
Sharing Data betweeen Containers

- `volumes-from`
- Shared "dics" that exist only as long as they are being used
- Can be shared between containers

#Terminal 1
➜  ~ docker run -ti -v /shared-folder debian bash
root@0fc275e9e8a6:/# echo hello > shared-folder/MYFILE
root@0fc275e9e8a6:/# 

#Terminal 2
➜  ~ docker ps -l --format=$FORMAT
ID  0fc275e9e8a6
IMAGE   debian
COMMAND "bash"
CREATED 20 seconds ago
STATUS  Up 19 seconds
PORTS   
NAMES   quirky_mirzakhani

➜  ~ docker run -ti --volumes-from quirky_mirzakhani debian bash
root@3fb04d6b2406:/# ls shared-folder/
MYFILE
```

**So this file, data file, originated in one container, was inherited by a second container, and then inherited by a third container, even though the machine that created it is gone.**

Now, when I exit both of these containers, this is the important part to understand, right then when I exited the last container using this volume, it went poof!

That's what volumes are for. They are ephemeral. They can be passed from one container to the next, but they are not saved. They will eventually go away.

