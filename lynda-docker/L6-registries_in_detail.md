## Registries in detail

As we start exploring building larger systems with Docker, one of the first questions that often comes up is, where's my data? Is it safe? Many companies choose to run their own Docker registry, so they can know that their data is safe and somewhere they can protect it.

So, it's just a program. You can run it anywhere you run other programs using existing infrastructure. It stores layers, images, keeps track of them, stores the tags, generally the metadata around the images, along with the images.

And it's just a service that listens on port 5000 for instructions like, push this image, pull that image, load this image from a disk, or search for images containing these key words. It also keeps track of who's allowed to log in, provided you've configured that. There are a couple of popular choices.

There's an official Docker registry produced by Docker, the company. And the popular maven caching repo, Nexus, also happens to provide in the newest versions, a Docker repo built in.

So there's a good chance you already have a Docker registry running in your organization, and nobody's using it. Now since the registry is just a program designed to provide a network service, why not go ahead and run it in Docker? So Docker makes installing network services pretty easy, that's what it's for.



```
What is a Docker Registry?

- Is a program
- Store layers and images
- Listen on (usually) port 5000
- Maintains an index and searches tags
- Authorizes and authenticates connections(sometimes)


Popular Docker Registry Programs

- The official Python Docker Registry
- Nexus


Running the Docker Registry in Docker

- Docker makes installing network service(reasonably) easy
- The registry is a Docker service


Saving and Loading Containers

- `docker save`
- `docker load`
- Migrating between storage types
- Shipping images on disks(or never underestimate the bandwidth of a thumb drive in a jetliner)

`docker save -o my-images.tar.gz debian busybox ubuntu`
`docker load -i my-images.tar.gz`
```
