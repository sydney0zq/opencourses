## Dockerfile syntax

There are a great many more options available to Dockerfiles than I covered in the previous examples, so I'd just like to briefly go through the rest of them here so that you'll know about them when you need them.

We saw the `FROM` statement, which just says, What image do you start running from. This should always be the first expression in your Dockerfile. It's actually okay to put multiples of them in a Dockerfile, it means that the Dockerfile produces more than one image, so they look like `FROM java:8`, build my image.

The ADD Statement, really quite a useful expression. We used it to add a local file, but it can do a whole lot more. It can do a whole lot more than just say `add run.sh` to the image at the location `/run.sh`. You can also add the content from an archive. So if you say `ADD project.tar.gz /install`, it doesn't copy the file tar.gz into that directory. It notices that it's a compressed archive, and it uncompresses all the files in that archive to that directory, so it automatically uncompresses tar files for you.

The ENV statement sets environment variables both for the duration of the Dockerfile, so while your image is building, and those environment variables will still be set in the resulting image.

ENTRYPOINT is much like CMD but it specifies the beginning of the expression to use when starting your container, and lets you tack more on the end, so if your container has an ENTRYPOINT of `ls`, then anything you type when you say Docker RUN my image name would be treated as arguments to the `ls` command.

CMD specifies the whole command to run, and if the person, when they're running the container, types something after Docker RUN image name, that will be run instead of CMD.

ENTRYPOINT gets added to when people add arguments to your container, and CMD gets replaced when people add arguments to your container. You can actually use both of them together. If you have them both, they get strung together, one after the other.

In general, if you're trying to make something that looks like a program, and you want people to not care that it's running inside a Docker container, ENTRYPOINT is for making your containers look like normal programs. CMD is probably what you want to use almost all the time, unless you're trying to do that. CMD and ENTRYPOINT and RUN can take commands to run in two different forms.

The Shell form looks like what you would normally type into a Shell, `nano notes.txt` and will be run in a shell. The Exec form looks like this, ["Bin/nano", "notes.txt"]. Note the comma there, it's important, and this causes nano to be run directly, not surrounded by a call to a Shell such as Bash, so it's slightly more efficient. In general, you can use whichever form looks better to you.

```
The FROM Statement

- Which image to download and start from
- Must be the first command in your Dockerfile


The MAINTAINER Statement

- Defines the author of this Dockerfile
    MAINTAINER Firstname Lastname <email@example.com>


The RUN Statement

- Run the command line, waits for it to finish, and save the result
    RUN unzip install.zip /opt/install/
    RUN echo hello docker


The ADD Statement

- Adds local files
    ADD run.sh /run.sh
- Adds the contents of tar archives
    ADD project.tar.gz /install/
- Works with URLs as well
    ADD https://project.example.com/download/1.0/project.rpm /project/


The ENV Statement

- Set environment variables
- Both during the build and when running the result
    ENV DB_HOST = db.production.example.com
    ENV PORT = 3322


The ENTRYPOINT and CMD Statement

- ENTRYPOINT specifies the start of the command to run
- CMD specifies the whole command to run
- If you have both ENTRYPOINT and CMD, they are combined together
- If your container acts like a command line program, you can use ENTRYPOINT
- If you are unsure, you can use CMD


Shell Form vs. Exec Form

- ENTRYPOINT RUN and CMD can use either form
- Shell form looks like this
    nano notes.txt
- Exec form looks like this
    ["/bin/nano", "notes.txt"]


The EXPOSE Statement

- Maps a port into the container
    EXPOSE 8080


The VOLUME Statement

- Define shared or ephemeral volumes
    VOLUME ["/host/path"  "/container/path"]
    VOLUME ["/shared-data"]
- Avoid defining shared folders in Dockerfiles


The WORKDIR Statement

- Sets the directory the container starts in
    WORKDIR /install/


The USER Statement

- Sets which user the container will run as
    USER zhou
    USER 1000

```

The VOLUME Statement defines shared volumes or ephemeral volumes, depending on whether you have one or two arguments. If you have two arguments, it maps a host path into a container path. If you have one, it creates a volume that can be inherited by later containers. **You should generally in Dockerfiles avoid using shared folders with the host, because it means that this Dockerfile will only work on your computer, and you'll probably want to share it around someday, or at least run it on a different computer.**

The WORKDIR Statement sets the directory both for the remainder of the Dockerfile and for the resulting container when you run it. It's like typing CD at the beginning of every RUN expression after that, so it's a useful expression to know about. 


## Avoid golden images

Here's a couple lessons I've learned from extracting golden images out of enterprises.

Step one, include the installer in your project. Five years from now, the installer for version 0.18 of your project will not still be available. Include it.

If you depend on a piece of software to build your image, check it into your image. It's good for that. Have a canonical build system that builds your images from scratch. That means starting from a base image that has not been touched by anyone in your organization.


Running a Docker file, build it up to the thing that you actual run in production. **Really, really avoid the temptation to log in one day, fix the config file, save the image over the same name, and get it back in production.**

The first time you do that, you no longer have a canonical build, and you have created the golden image. Docker makes it very, very, easy to do that, and very, very difficult to resist.

Use small images. If you start with a very large operating system as the base for your system, that large operating system takes large maintenances, and you're going to be shuffling around a lot of bits back and forth over the network that really aren't being used.

```
Preventing the Golden Image Problem

- Include installers in your project
- Have a canonical build that builds everything completely from scratch
- Use small base images, such as Alpine
- Build images you share publicly from dockerfiles, always
- Don't ever leave passwords in layers; delete files in the same step
```


When you're building images that you're going to share publicly. Say you ship your product as a Docker image, build it from Docker files. Always.

There's nothing like going back to an old version of the software that someone is complaining about bugs and having no idea how it was built or how it got that way.

And just a little note, don't ever leave passwords hidden in the deep layers of your Docker files. It's trivial for someone to dig through and find them.

































