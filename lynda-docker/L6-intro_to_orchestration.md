## Orchestration Building Systems with Docker

Now let's briefly touch on how large systems are being built using Docker today. So just to start with, one container is about as useful as one hand clapping. It's cool, it's philosophically neat, maybe you can get something out of it, but most people want more.

There are many options out there for orchestrating large systems of Docker containers. We're just going to touch on a few, and give you a place to start.


```
One Container = One Hand Clapping

- Many orchestrating systems for Docker
- Start containers -- and restart them if they fail
- Service discovery -- allow them to find each other
- Resource allocation -- match containers to computers
```

Orchestration systems, start your containers, keep them running, and restart them if they fail. They allow the containers to find each other. If a container gets restarted, all the machines that were connecting to it need to be able to find its replacement. So service discovery is a big part of any Docker orchestration system.

And making sure that the containers are running in a place where the resources exist for them to actually do their job. Is the storage they need available at that location? Is there enough RAM, is there enough CPU? Is that machine being taken
offline for maintenance? Does this container need to be moved somewhere else?


So the easiest to get started with, and the simplest, is Docker Compose. For single machine coordination, this is the de facto standard. In fact, you already have it on your computer. It's designed for testing, development, staging, generally working on projects that have more than one container, but not for serving them in large scale systems, and not for things that's scaled dynamically.

What it does, is it brings up all your containers and volumes, et cetera, with one command. You just run Docker Compose up, and it starts all your containers. And the great feature is that it's already included in Docker Tool Box, which you already have it installed.

```
Docker Compose

- Single machine corrdination
- Designed for testing and development
- Brings up all your connections, volumes, networks, etc., with one command
- Included in docker-toolbox
- Get started at https://docs.docker.com/compose/
```






```
Kubernetes

- Containers run programs
- Pods group containers together
- Services make pods available to others
- Labels are used for very advanced service discovery


Advantages of Kubernetes

- Make scripting large operations possible with the `kubectl` command
- Very flexible overlay networking
- Runs equally well on your hardware or a cloud provider
- Built-in service discovery
- Get started at https://kubernetes.io


EC2 Container Service(ECS)

- Task definitions
    Define a set of containers that always run together
- Tasks
    Acutally makes a container run right now
- Services and exposes it to the Net
    Ensures that a task is running all the time


Advantages of ECS

- Connects load balancers (ELBs) to services
- Can create your own host instances in AWS
- Make your instances start the agent and join the cluster
- Pass the docker control socket into the agent
- Provides docker repos -- and it's easy to run your own repo
- Note that containers (tasks) can be part of CloudFormation stacks
- Get started at https://aws.amazon.com/ecs/
```


Now for larger systems, there are many choices. I'm going to touch on a couple of them here and talk about how to compare them. Kubernetes brings a couple of ideas that are fairly common, to all of the orchestration systems but expressed differently everywhere.

It has containers, which run programs. Those are containers in the way that we usually think of them. Pods are groups of containers that are intended to be run together always on the same system.

So pods give you approximately as much as Docker Compose, but it's dynamically distributed, Kubernetes finds a place to run it, and it provides orchestration and service discovery and all the other stuff around these pods. Kubernetes has the idea of services, which make pods discoverable by others, accessible to others.

If a connection to a pod, that's part of a service, gets restarted somewhere, then that service will redirect the traffic to the new instance. Kubernetes has an amazingly
powerful system of labels for describing every aspect of your system. So you can say, my service needs to connect to an instance of version 5.2 running on this hardware, and I need an instance that is in the same data center as this other service, it's very extensive.

The kubectl command makes scripting large operations in Kubernetes, if not easy, possible to the extent that other systems don't. It gives you sort of a one command interface to do almost everything with Kubernetes. And it provides a very flexible system of overlay networking to allow your containers to find each other and connect to each other, regardless of how things move around throughout your infrastructure.

Kubernetes runs equally well on your own hardware or on a cloud provider or even across both of these. It's overlay networking system is quite well suited to a wide variety of deployment scenarios. And it has service discovery built in.


Another great option is the Amazon EC2 Container Service, or ECS. This service uses an analogous vocabulary, but with a slight different twist to each part. Task definitions provide all the information required to start a container and a set of containers that are designed to run together. It's somewhat analogous to a pod, a little bit, in Kubernetes it's all the information required for services that will run together on the same machine. It doesn't actually run anything, creating a task definition just defines a task that will run.

When a task definition is actually run, it's called a task, and that's a bunch of containers that are running right now, shared together on a single host. Services take tasks, expose them to the net as a whole, and ensure that they stay up all the time. So you'd create a service that has 14 copies of a particular task, and it will ensure that that many copies is running all the time, even if it has to split it across several hosts. 

ECS has a bunch of advantages too, it ties into the existing Amazon infrastructure very well. So Amazon load balancers tie into ECS services to make your traffic available to the internet using the existing systems.

You create your own instances in AWS, you have lots of control over that. And once you've got your instances running, you run an agent on them and cause them to join the cluster. This is kind of cool, because you take the Docker Control Socket, pass it to the agent that you run in Docker, and that allows the agent to control the host that it's running on.

It's kind of a neat system that makes running EC2 clusters very convenient from an operational perspective. ECS provides a set of docker repos built in. So you don't have to run your own repo, ECS has them built in and they're made available to the machines on ECS. It's perfectly easy to run your own repo along with ECS, you don't have to use the built in one if you already have your own. Containers and tasks can be part of CloudFormation stacks, which makes deployment along with other resources in AWS, very, very easy.

So if you have containers that need to access to queues, and they need access to EC2 volumes, you can deploy all of this in one go and have it be cleaned up together when the service ends.

