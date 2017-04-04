###Commands for HW info

lshw and lspci, lsusb and lsbk, lscpu and lsdev.


###Cmds for HW Control and Config

hdparm

Write to `proc`, `dev`, or `sys` files

inb and outb

setpci


###System Calls

System calls are function implemented by the kernel and meant to be called from user space.

There are about 300.

> See /usr/src/linux-headers-3.16.0-4-common/`include/uapi/asm-generic/unistd.h`

They are documented in man section 2. And **they are called through the standard library.(e.g., libc)**

```
$ man 2 read
```


###System Call Mechanics

Standard library uses architecture-dependent means to invoke the system call mechanism.

Suitably sized parameters are usually put in registers.

The kernel is invoked, determines which system call, and calls it.


###System Call Return

If an error, system calls return a negative value to the library.

On error, the library sets "errno" to abs(return value), and return -1.

When no error, library usually does not set errno and returns the value it obtained from the kernel.



###printk

`printk()` is the kernel's function for code to print messages. It's like C's `printf()`.

It is sent to RAM buffer and the system console.

Important enough ones are shown on the console.

Logging daemon may send to file or elsewhere.


###Display Kernel Messages

`dmesg` showsa **RAM buffer messages** from kernel.

Log file(e.g., `/var/log/messages`) has kernel messages and more.

`tail -f /var/log/messages` can be handy.

----------------


###Virtual Filesystems

The `proc` and `sysfs` filesystems are virtual filesystems.

Their contents are not stored on disk.

Each file and directory entry has an associated function in the kernel that produces the contents on demand.

Ramfs filesystems store their content in RAM, virtual filesystems generate its content on demand.


###/proc

The `proc` filesystem is mounted on `/proc` at boot.

`proc` gets its name from 'process'.

`proc` contains lots of process info and lots more.

Kernel tunable variables are an important part of `proc`.

Each process has a directory named with its PID.

It has info on memory, program, files and lots more.

There are hundreds of files and directories per process.

Threads have entries under the directory "task". Notice when you look at the files, you get just a snapshot.


###/sys

The `sysfs` filesystem is mounted on `/sys` at boot.

`sysfs` is for "kernel object" info.

In particular, it is hardware info(e.g., PCI device info).


###Device files

Character and block drivers use drive files.

Device files have a major number, minor number, and type(c or b). Major number determines which driver to use.

The kernel maintains a relationship between the three characteristics and what driver to call.

The driver can implement different functions for different mior numbers.


###Drivers and Device Files

A character driver, for example, can implemnt `open()`, `read()`, `write()` and `ioctl()`.

A process opens a device file and then can read, write etc, with the file descriptor. The kernel arranges to have the driver's function to be called.

`echo hi > /dev/null` would open, and then write.

The driver can implement different functions for different minor numbers.

```
$ ls -l /dev/null
crw-rw-rw- 1 root root 1, 3 Mar 30 20:58 /dev/null

$ ls -l /dev/zero
crw-rw-rw- 1 root root 1, 5 Mar 30 20:58 /dev/zero

`1, 3`: 1 is the major number while 3 is the minor.
```

