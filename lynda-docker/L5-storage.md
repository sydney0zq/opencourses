## Storage

Now let's talk briefly about how Docker accomplishes the idea of images and containers. How does it do the storage behind them keeping them isolated, letting them be stacked on top of each other?

All of that stuff requires a little bit of an introduction to the layers of the Unix file systems method. So at the very lowest level, you have actual things. Stuff that stores bits, hard drives, thumb drives, network storage devices.

The kernel manages these. On top of those, it forms them into logical groups, so you can say these four groups form a RAID array, or these two drives should be treated as one drive, or this one drive should be treated as 432 drives, so it has a layer that lets it sort of partition up drives arbitrarily into groups and then partition those groups up.

Docker makes extensive use of this capability. On top of that, we have filesystems. That determines which bits on the drive are part of which part of which file, so the fourth byte in the file foo.txt would be at a particular spot on a particular drive, and it's up to the kernel with the filesystems to keep track of where that spot actually is.

Now on top of all that, **you can take programs, and programs can pretend to be filesystems.** We call this FUSE filesystems.

```
Unix Storage in Brief

- Acutal stroage device
- Logical storage devices
- Filesysystems
- FUSE filesystem and network Filesysystems
```


COW is an acronym in this case for copy on write. So we start with our base image. This is a cow. He has no spots. Now, I want to write some spots for this cow. 

Let's give him some dark spots. You know, good traditional cow spots. Instead of writing directly onto the cow, 'cause someone else might be working with this cow, there might be another container running off of this image right now. 

I don't want to just reach in and write some spots onto that image because someone else is probably using it, so I write my spots onto a separate layer right next to it, and then when I start my container, layer the spots over the cow and give that to the container, so the container sees the image of a cow with spots even though the cow image still exists without his spots, and others that are still using the spotless cow image can continue to do so, but I want these dark spots.

#pic 1

You know, **somebody else really has a more artistic perspective, and they'd like a cow with light spots, so they're going to start with the same image, literally the same image, not a copy of the image, but the same one, and they're going to make their own layer, but with their own interpretation of what cow spots should look like, so they make their own filesystem layer and layer it over that image, and here we have a cow with different colored spots, so it's called copy on write when I would write to this cow instead of writing directly to the cow, I write to my own layer, which gets layered on top of the cow.**

#pic 2

When I want to look at the cow, I just look at the whole thing. I only copy the pieces that I write. I read from the original and copy when you write. Copy on write. So to get a little bigger perspective, we have the original image of the cow, unchanged, just one of them. I'm going to draw him down here. We have the resulting images of that cow.

Each one has a different set of spots layered on top of it, so we have a total of one, two, three images here, and two combinations of the way they're layered. Docker has many different actual internal mechanisms that it uses for managing the COW layers, the copy on write filesystem layers, and these depend a lot on what's available on the system it's running on.

Sometimes it uses Btrfs, sometimes it uses LVM, the logical volume manager, sometimes it uses the overlay filesystem. There are many ways. It doesn't really matter as long as it can accomplish layering on its own sort.

You don't have to worry about the format of a COW on one machine, a copy on write filesystem, if you want to import that image to another one because what it does it that it takes each layer, **splits out the layers, and makes them into normal gzip files and ships them over the network to you separately, and the receiving end of that network connection, the place you're actually running the Docker server, receives all of those layers separately,** and then puts them together using the filesystems that are available on that computer, so this is how COWs can move easily between computers, so the containers are independent of their storage engine.

I can send images between machines pretty much freely. There is one little bit depending on the storage layer that's in use on a particular machine. It is possible in some cases to run out of layers. Some of the storage engines have a limited number of layers and others don't.

If you make a very deeply nested image on a machine that allows a great number of layers, and then you package it up and try to download it on a machine that uses a storage engine with less layers, you can run out of layers. This is worth being vaguely aware of. It doesn't come up very often, and it's good to be able to recognize it when it does.

#pic 3


```
Moving Cows

- The contents of layers are moved between containers in gzuo files
- Containers are indenpendent of the storage engine
- Any container can be loaded (almost) everywhere
- It is possible to run out of layers on some of the storage engines
```


Another part of images and storage in Docker is how we do volumes and shared folders with the host. These are not actually magic. They're built right in to the Linux file system, so the Linux file system starts with an assumed root directory called slash. 

```
Volumes and Bind Mounting

- The Linux VFS
- Mounting devices on the VFS
- Mounting directories on the VFS
- Getting the mount order correct
- Mounting volumes -- always mounts the host's filesystem over the guest

docker@default:~/demo/work$ touch a b c d e f
docker@default:~/demo/work$ ls
a  b  c  d  e  f
docker@default:~/demo/work$ cd ..
docker@default:~/demo$ mkdir other-work
docker@default:~/demo$ cd other-work/
docker@default:~/demo/other-work$ touch other-a other-b other-c other-d
docker@default:~/demo/other-work$ ls
other-a  other-b  other-c  other-d
docker@default:~/demo$ sudo mount -o bind other-work work
docker@default:~/demo$ cd work/
docker@default:~/demo/work$ ls
other-a  other-b  other-c  other-d
docker@default:~/demo$ sudo umount work

#I didn't delete them, I didn't copy over them, they're still there. There's just another directory mounted on top of them right now.
```

Everything is exactly the way it was. I just had temporarily put one filesytem layer over another, and then I pulled it off, revealing the original.

This is how Docker does the shared folders between a container and the host, so there's an important side effect of this, which is you have to get the mount order correct. If you want to mount a folder and then a particular file within that folder, you have to it in that order. If you mount the file so it bind mounts that file right onto that position, and then you mount a folder on top of it, the file will be underneath the folder and will be hidden, so it's important to get the order of the `-v` for volume arguments to Docker correct.

Another bit is mounting volumes always mounts the host's filesystem over the guest. Docker doesn't give you a way of saying mount this guest file system into the host, preserving what was on the guest. It always chooses to mount the host filesystem over the guest filesystem.

