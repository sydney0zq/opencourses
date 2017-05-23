##Link containers


![](http://okye062gb.bkt.clouddn.com/2017-05-23-025043.jpg)

Now let's talk about getting data between containers.

The first approach is just to go out to the host and then back to the other container, and then that other container can go out to the host and back to the first container. So you can connect two containers together by just exposing a port on each of them, and then having each of them connect to the host on that port, which then gets forwarded into the appropriate container. 

![](http://okye062gb.bkt.clouddn.com/2017-05-23-030724.jpg)

Now a more efficient approach and better in some ways, worse in others, is to link your containers so the data goes directly from the client container to the server container while staying within docker. This has some interesting advantages and a few things you need to watch out for.

First of all, this is generally used with some sort of an orchestration tool to keep track of what's running where. **When you link two containers together, you link all their ports, but only one way. You're connecting from the client to the server, but the server doesn't know when a client connects to it or goes away or whatever, so it's a one-way.**

You should probably use this on services that are really meant to be running on the same machine. So a service and the health check that monitors it, that's a really good example. Those kinda need to be running on the same machine. A service and its database, could be good, but it might not be good depending on your circumstances.

```
Connecting between containers

➜  ~ docker run --rm -ti -p 1234:1234 test_image
root@a6a783e07e2e:/# nc -lp 1234
hold my word    #receive

➜  ~ docker-machine ip
192.168.99.100
➜  ~ docker run -ti --rm test_image bash
hold my word    #send


Connecting Directly between Containers
<Linking Directly>

- Generally used with orchestration
- Links all ports, though only one way
- Only for sevices that cannot ever be run on different machines
- A service and its health check -- good example
- A service and its DB -- not good
- Automatically assigns a hostname
- Note that links can break when containers restart

➜  ~ docker run -ti --rm --name server test_image
root@a4588eb79a13:/# nc -lp 1234
I am client

➜  ~ docker run --rm -ti --link server --name client test_image
root@e347e6d932be:/# nc server 1234
I am client
^C     
root@e347e6d932be:/# cat /etc/hosts
127.0.0.1   localhost
::1 localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
172.17.0.3  server a4588eb79a13 #attention this line
172.17.0.4  e347e6d932be
```


##Dynamic and legacy linking

So now let's talk about how to use links in such a way that they don't break when services come and go and restart, etc.

For this I need to introduce you to a new feature of Docker. **Docker has private networks that you can set up, put containers in, and that will keep track of the names at the network level, so that when containers go away and come back, the name will change for all of the machines in that private network to refer to the new address.**

You have to make these networks in advance. It's not fully automatic, but it's pretty easy. To make these networks, use the command `docker network create` and give your network a name.


```
How to Make Links Not Break

- Docker has private networks
- These have built in nameservers that fix the links
- You must create the networks in advance
- `docker network` create `network-name`

#Terminal 1
➜  ~ docker network create example
d2cf3788e2379868a77e4450ea201393aaa995ad2fc02efb971b4bf3ecba8901
➜  ~ docker run --rm -ti --net=example --name server test_image
root@28cb0ad76e8c:/# nc -lp 1234
now it works
^C
root@28cb0ad76e8c:/# exit
➜  ~ docker run --rm -ti --net=example --name server test_image
root@f387b571a7a1:/# nc -lp 1234

#Terminal 2
➜  ~ docker run --rm -ti --link server --net=example --name client  test_image
root@a77174af2eb6:/# nc server 1234
now it works
root@a77174af2eb6:/# nc server 1234     #reconnect var virtual network
```

Linking through private networks is relatively new to Docker. Before that they had a feature called linking, which was very similar, but it worked by setting environment variables inside the containers. So you'll still see this in a great many tutorials that are end instructions that out there on Docker. When you see it, just note that it's the old system, it still exists, you can still use it.

```
Legacy Linking

- Sets environment variables in the linking container for host and port
- See this in many tutorials and instructions


IP Address Binding in Your Services

- Services that listen "locally" by default are only available in the container
- To allow connections, you need to use the "bind address 0.0.0.0" inside the container
- You should use docker to limit access to only the host
```

Just a little side note about IP addresses and the services you put in containers. **Very often a service is configured to either listen for connections from the local machine or from the Internet. Now when that service gets moved into a container, the local machine for that container's perspective is the inside of that container.** If you wanted to actually be able to receive connections from the same host, but in different containers, you need to change that service to listen for connections from the Internet by setting its bind address to 0.0.0.0. Don't worry about that exposing. You can still use Docker to limit access to only from the same host.

You just have to allow access from outside the container into the container. So an example of this would be when you do docker run, you can say `docker run -p listen` for connections only from the localhost address of the host, 127.0.0.1, and only if it's coming from this host should you forward it on port 1234 into the container on port 1234 using tcp.

So that's how to make private services that are private to a container. This can come up pretty often, so I just felt we should mention it here.

