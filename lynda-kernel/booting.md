##Understand the booting

###GRUB's Role

GRUB comes after POST, and the BIOS.

GRUB is installed in a special place on disk.

GRUB loads the kernel, initial root filesystem, set up the kernel command line, and then transfers control to the kernel.

GRUB can be interrupted, and you can interact with it.


###GRUB's Flexibility

GRUB is built with support for filesystem. Therefore, GRUB can find files, like kernel files, by name.

GRUB can do file name completion.

GRUB has lots of utilities(do `man -k grub`).


---------------

##Configure GRUB

###GRUB configuration

GRUB 1 had a config file, `grub.conf`, that one edited to add, remove, or modify kernel boot choices.

GRUB 2 is signigicantly more sophisticated.

`/etc/grub.d`

`/etc/default/grub`


###New GRUB Entries

Edit or add a config file in `/etc/grub.d`. Normally, edit `40_custom`

Run `grub2-mkconfig` to generate a new config file.


###GRUB Interactive

Normally pauses before launching Linux.

Interrupt GRUB by hitting a key(e.g., down arrow).

Temporarily edit GRUB configuration.

Continue with boot with your change - `b` or `C-x` as indicated.


###GRUB Passes Parameters

The kernel processes command-line arguments.

Unrecoginzed ones are ignored.

User space may look at the kernel command-line args, too.

You can use `dmesg` or `/proc/cmdline` to see.


###Kernel Parameters

In the kernel source tree, it is `Documentation/kernel-parameters.txt`.

About 500 are documented there.

Many are registered with `__setup()` in source.


---------------


##Process 1 & Startup Services

###The Initial Root Filesystem

Linux systems frequently start up by mounting a filesystem from RAM. The filesystem that contains "/" is called the root file system.

This initial RAM disk or RAM filesystem(initrd) is used to provide drivers and support for mounting the system's real root file system.

The `initrd` has an `init` that the kernel runs first.


###The First Process(from Disk)

When the `init` from the `initrd` terminates, the Linux kernel starts init again; this time from the real filesystem, which is commonly on disk.

Historically that program was called "init". Now, `init` maybe a link to `systemd`.

This process is responsible for starting up system services such as daemons like a web server.


###System Services

For older Linux systems, there were runlevel scripts to start up services. There were under `/etc/rc.d`.

`systemd` service files are under the `/etc/systemd/system`.

These services are user-space services and not features of the kernel.


###The initrd/initramfs File

An `initrd/initramfs` in `/boot` for each kernel.

A gzipped CPIO archive when `initramfs`; a gzipped filesystem image(e.g., ext2) when an `initrd`.

Name it something`.gz`, unzip it, and `cpio` extract it; `be very careful` and use `--no-absolute-filenames` or `gunzip` and mount for `initrd`.


###Distribution Versions

Distribution and releases vary widely in the contents of their initrd/initramfs images.

You can start with the init program.

Booting with `rdinit=/bin/sh` will start with a shell in the initramfs. `init=/bin/bash` will complete the initramfs and then start with a shell on the disk.


###Customizing initrd/initramfs

Unpack the image.

Make modifications, repack, replace version in `/boot`(after making a copy of the original just in case), and reboot.

Need to be on the system console.

```
$ cp /boot/initrd.img-3.16.0-4-amd64 /tmp/initdir/i.gz
$ gunzip i.gz
$ $ file i
i: ASCII cpio archive (SVR4 with no CRC)

$ cpio -i --no-absolute-filenames < i
90248 blocks
$ ls
bin  conf  etc  i  init  lib  lib64  run  sbin  scripts
```






