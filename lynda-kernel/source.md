##Linux Kernel Source Code

###Version Info

```
VERSION = 3
PATCHLEVEL = 10
SUBLEVEL = 0
EXTRAVERSION = 
NAME = My Name
```


###Output of `make help`

Cleaning tagets:
    clean: Remove most generated files but keep the config
    mrproper: Remove most generated files + config + various backup files
    distclean: mrproper + remove editor backup and patch files


Configuration targets:
    xconfig: Update current config utilising a QT based front-end
    gconfig: Update current config utilising a GTK based front-end
    menuconfig: Update current config utilising a menu based program
    config: Update current config utilising a line-oriented progtam
    ...


Other generic targets:
    all: 
        Build all targets marked with [*]
        * vmlinux
        Build the bare kernel
        * modules
        Build all modules

    modules_install:
        Install all modules to 
        INSTALL_MOD_PATH(default: /)
        ...


Architecture specific targets(x86):
    \* bzImage
    Compressed kernel image(arch/x86/boot/bzImage)
    \* install
    Install kernel using ~/bin/installkernel or (distribution)/sbin/insatllkernel or install to $(INSTALL_PATH) adn run lilo
    ...


###The Source Code

Changes rapidly -- approximately 10k lines per day.

Will not always find all answers in the documentation, web source.

Use the source to your kernel.

Documentation is in the source tree.


###Documentation Subdirectory

Lots of files from code authors.

Some lengthy documents.

`grep -rl` in documentation.



###include

Kernel code must be compiled using an include directory that corrsponds to the kernel version adn configuration that the code will be used with.

Kernel code does not use file from `/usr/include`.

Some file in `/usr/include`, such as some needed by `glibc`, are derived from kernel include files, though.


###fs

Linux has a wide variety of filesystems:

- Virutal (proc and sysfs)
- On-disk (ext{2,3,4}, btrfs and xfs)
- Network (nfs)
- compatible (ntfs, fat and hfs)


###arch

Linux has been ported to many computer architectures.

The linux kernel code is written to be portable.


###security

`security.c` provides the fundamental hooks that SELinux and apparmor and other security systems use.

`security.c` essentially provides a hook into all system calls so that extra checks can be made.

The kernel portion of SELinux and apparmor are also in the security directory.

