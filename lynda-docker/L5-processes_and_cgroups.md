## Primer on Linux Processes

So in Docker, your container starts with one process, the init process. That process can divide into other processes and do any number of things. Often, it starts with a shell, and that shell splits off and runs commands and runs other processes. When that init process exits, your container just vanishes.

Any other processes that were in it at the time that the init process exits get shuts down unceremoniously. The container is done.

All right, now over here I'm gonna look up the process id of the init process in that container using the docker inspect command. `docker inspect` is an incredibly powerful tool for scripting all your interactions with Docker.

You can use it to examine just about any aspect of a Docker container programmatically using this jQuery-like syntax here.

```
Primer on Linux Processes

- Processes come from other processes -- parent-child relationship
- When a child process exits, it returns an exit code to its parent
- Process 0 is special; called init, the process that starts the rest
- In docker, your container starts with an init process and vanishes when that process exits
- `init` cleans up abandoned processes

➜  sydney docker run -ti --rm --name hello debian bash
root@6bad6f6ef248:/# 
➜  sydney docker inspect --format '{{.State.Pid}}' hello
28559
➜  sydney docker-machine ssh
docker@default:~$ sudo kill 28559

# Back
root@6bad6f6ef248:/# exit
```

One other job the init process does is if other processes in the system become abandoned by being detached from the place where they started, then they suddenly become owned by the init process and it gets notified of their exiting.

If you have situations where you have containers that appear to be un-exitable, where you hit Control + C or you send them kill signals and they just don't exit, that's one area to pursue in debugging.



Process isolation, another thing Docker does is keep your containers from messing with each other. It uses a feature of the Linux Kernel called cgroups, control groups, and this lets all of the processes in this group become their own isolated place. They have their own process IDs, they don't see any processes that are not in the group, and they have absolutely no way to interact with processes outside their groups.

So it's used to partition your system into sets of processes that can see each other. Any process that is started within this group, the children of that process stay within that group.

This fact that the processes have no way to identify any process outside their group really strongly enforces the isolation of Docker containers. So containers, they can't even see processes in other groups.

```
Process Isolation

- The process that starts a container is contained in a cgroup
- Docker uses cgroups to partition the processes into control groups
- Any processes it starts stay in that group
- Communicaiton between processes is limited to preocesses in this group
- Containers cannot see processes in other cgroups
- It's hard to mess with a process without access to `/proc`

# The docker server
docker@default:~$ ls /proc
#Many processes

root@01ff233fb8f2:/# ls /proc
#Only two processes

# Those two processes are one, the init process, the shell, and the second one is the ls process itself that is running while it's printing these out. The important part to take away is it's very hard to mess with the process if you can't get to its /proc entry. This provides pretty strong isolation and security between containers.
```


All right, another feature and a very important job of Docker is to control access to the limited resources on the machine.

That's the amount of time the CPU can spend doing things and the amount of memory that can be allocated between containers. These limitations are inherited, and this is very important.

If a container is given a certain amount of memory and CPU time, no matter how many processes it starts, the sum total of all those processes can't exceed the quota that was given to the initial process.

```
Resource Limiting

- Scheduling CPU time
- Memory allocation limits
- Inherited limitations and quotas
- Cannot escape your limits by starting more processes
```

