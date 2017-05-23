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





























