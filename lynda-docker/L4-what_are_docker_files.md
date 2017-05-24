## What are docker files?

So far, we have made a couple of Docker images by hand and run things on them to make containers. Now, let's explore building images with code. That's where Dockerfiles come in.

Dockerfiles are small programs designed to describe how to build a Docker image. You run these programs with docker build command, so it's docker build and `-t` stands for tag, and that just says, "When you've finished building this thing, tag it with this name so that it's easy to find afterward."

When it finishes running your Dockerfile, the resulting image will be on your computer in the local Docker registry ready to be run with `docker run`.

**So each step produces a new image. It's got a series of steps. Start with one image, make a container out of it, run something in it, make a new image. The previous image is unchanged; it just says start from that, make a new one with some changes in it.**

```
What is a dockerfile?

- This is a small "program" to create an image
- You run this program with
    `docker build -t name-of-result .`
- When it finishes, the result will be in your local docker registry
```

**The state is not carried forward from line to line. If you start a program on one line, it runs only for the duration of that line. So as a result, if part of your build process is download a large file, do something with it and delete it, if you do that all in one line, then the resulting image will have only the result of that.**

**If you download it on one line, it will get saved into an image. The next line will have that image saved there, and the space occupied by your big downloaded file will be carried all the way through, and your Dockerfile can get pretty big. Be careful about having operations on large files span lines in Dockerfiles.**

<https://docs.docker.com/engine/reference/builder/>

```
Producing the Next Image with Each Step

- Each line takes the image from the previous line and make another image
- The previous image is unchanged
- It does not edit the state from the previous line
- You don't want large files to span lines or your image will be huge
```

So each step of running a Dockerfile is cached. I mentioned that the later steps don't modify the previous step. **That means that the next time you run your build, if nothing changed, it doesn't have to rerun that step.** So Docker can skip line that weren't changed since the last time you built this Dockerfile.

So if the first line in your Dockerfile is "download this big file and save the latest copy," and then 20 minutes later you run that again, the file will have already been downloaded, so it won't run that line, and it won't spend the time to go download that huge file again.

This can save huge amounts of time. You do have to be aware of it, though, because if you wanted it to re-download the latest version of that large file, you'll have to explicitly make it do so.

Just a little tip: put the parts of your code that you change the most at the end of your Dockerfile. That way the parts before them don't need to be redone every time you change that part.

```
Caching with Each Step

- This is important, watch the build output for "using cache"
- Docker skips lines that have not changed since the last build
- If you first line is "download lastest file", it may not always run
- The caching saves huge amounts of time
- The parts that change the most belong at the end of the Dockerfile
```


One part I just can't emphasize too much is that Dockerfiles are not shell scripts. They were designed with a syntax that looks like shell scripts because that helps them be familiar to people, and it makes them a little easier to learn, but Dockerfiles are not shell scripts.

Processes you start on one line will not be running on the next line. You run them, they run for the duration of that container, then that container gets shut down, saved into an image and you have a fresh start on the next line.

So you can't treat it like a shell script and say start a program on one line, then send a message to that program on the next line. The program won't be running. If you need to have one program start and then another program start, those two operations need to be on the same line so that they run in the same container.

Environment variables do persist across lines if you use the ENV command to set them. Just remember that each line in a Dockerfile is its own call to docker run, and then its own call to docker command. That will help keep in mind the differences between Dockerfiles and shell scripts.


```
Not Shell Scripts

- Dockerfiles look like shell scripts
- Dockerfiles are not shell scripts
- Processes you start on one line will not be running on the next line
- Environment variables you set will be set on the next line
    If you use the ENV command, remember that each line is its own call to `docker run`
```


## Building dockerfiles

```
The Most Basic Dockerfile

- Put this in a file named Dockerfile:
    FROM busybox
    RUN echo "building simple docker image."
    CMD echo "Hello Container"


➜  demo cat Dockerfile 
FROM busybox
RUN echo "---Building simple docker image..."
CMD echo "---hello container"
➜  demo docker build -t hello .
Sending build context to Docker daemon  2.048kB
Step 1/3 : FROM busybox
latest: Pulling from library/busybox
1cae461a1479: Pull complete 
Digest: sha256:c79345819a6882c31b41bc771d9a94fc52872fa651b36771fbe0c8461d7ee558
Status: Downloaded newer image for busybox:latest
 ---> c75bebcdd211          #Create the image we started with
Step 2/3 : RUN echo "---Building simple docker image..."    #Start from c75bebcdd211
 ---> Running in 14ea635b2906
---Building simple docker image...
 ---> 92768d4d6d78
Removing intermediate container 14ea635b2906
Step 3/3 : CMD echo "---hello container"
 ---> Running in c58c1b6facfc
 ---> 2403709e1b75
#That resulted in the container called dd715 c58c1b, which then was committed to produce the image 2403709.
Removing intermediate container c58c1b6facfc
Successfully built 2403709e1b75
Successfully tagged hello:latest

➜  demo docker run --rm hello 
---hello container
```



```
Installing a Program with Docker Build

- Put this in a Dockerfile
    FROM debian:sid
    RUN apt-get -y update
    RUN apt-get install nano
    CMD "nano" "/tmp/notes"

➜  demo cat Dockerfile 
FROM debian
RUN apt-get -y update
RUN apt-get install nano
CMD ["/bin/nano", "/tmp/notes"]

➜  demo docker build -t example/nanoer .
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM debian
 ---> 3e83c23dba6a
Step 2/4 : RUN apt-get -y update
 ---> Running in 26e0751713e7
Get:1 http://security.debian.org jessie/updates InRelease [63.1 kB]
...
Fetched 9954 kB in 36s (271 kB/s)
Reading package lists...
 ---> 7b0336749e4f
Removing intermediate container 26e0751713e7
Step 3/4 : RUN apt-get install nano
 ---> Running in 66991b2476e8
 ...
Reading package lists...
update-alternatives: using /bin/nano to provide /usr/bin/pico (pico) in auto mode
 ---> 2c85eff53c57
Removing intermediate container 66991b2476e8
Step 4/4 : CMD /bin/nano /tmp/notes
 ---> Running in 5ca7a19f07e4
 ---> b4b0c57c10d6
Removing intermediate container 5ca7a19f07e4
Successfully built b4b0c57c10d6
Successfully tagged example/nanoer:latest

➜  demo docker run --rm -ti example/nanoer
➜  demo         #When I quit nano, I quit the container
```



```
Adding a File through Docker Build

- Put this in a Dockerfile:
    FROM example/nanoer
    ADD notes.txt   /notes.txt
    CMD "nano" "/notes.txt"

➜  demo cat Dockerfile 
FROM example/nanoer
ADD notes.txt /notes.txt    #需要在当前目录下面新建一个notes.txt
CMD ["/bin/nano", "/notes.txt"]
➜  demo docker run -ti --rm example/notes
```

