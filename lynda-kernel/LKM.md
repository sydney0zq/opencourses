###What is a LKM(Linux Kernel Modules)?

An object file with a .ko suffix.

Contains code to run in kernel space.

Dynamically adds functionality to the running kernel.

Should be written in C and compiled for a particular kernel version -- not binary compatible with other kernels.


###Advantages

Can be a relatively minimal kernel file.

Add functionality without rebuilding or rebooting.

Allow for only the needed functionality to be loaded.

Live updates.

Accelerated development.


###Kernel Module Installation

Modules are installed into a directory under `/lib/modules` with each installed kernel version having its own directory.

The modules are organized in different subdirectories under the kernel version.

There are also config files.


###Module Files

Each module should have a unique name.

Module files can be in any directory, but the `modprobe` utility is designed to look only under "/lib/modules/`uname -r`".

Only modules built for the kernel version -- and how it was configured -- should be loaded.

Modules run in kernel mode with all privileges.

```
$ cd /lib/modules/`uname -r`/kernel
$ find . -name "*.ko" | wc -l
3050
```


###lsmod

Lists the modules loaded, chronologically.

```
$ lsmod
Module                  Size  Used by
binfmt_misc            16949  1 
dm_mod                 89405  0 
vboxsf                 41462  1 
nfsd                  262938  2 
auth_rpcgss            51209  1 nfsd
oid_registry           12419  1 auth_rpcgss
nfs_acl                12511  1 nfsd
nfs                   192232  0 
...
#0 means this module was not in use
```


###rmmod

This removes the module.

Module may be in use, so may not be able to remove it.

`rmmod -f` may let you remove a module that the kernel thinks is in use.

Often never done -- it is easy to leave the kernel in a fragile condition.


###modinfo

Module info.  Author.  Paramters.  Aliases.  vermagic.  More...


###depmod

Generates module config files for `modprobe`.

Seldom a need to run.


###insmod

Insert a module.

Doesn't return until module initialization function returns.

May fail and an error message may be printed -- `dmesg` -- can show more details.

Must provide path to the module file.


###modprobe

Loads a module and its dependencies.

Uses dependency files under `/lib/modules/VERSION`.

Easier and more convenient than `insmod`.

Can remove modules, too.

Lots of options.

```
[root modules]#cd 3.16.0-4-amd64/
[root 3.16.0-4-amd64]#head modules.dep
kernel/arch/x86/kernel/cpu/mcheck/mce-inject.ko:
kernel/arch/x86/kernel/msr.ko:
kernel/arch/x86/kernel/cpuid.ko:
kernel/arch/x86/kernel/iosf_mbi.ko:
kernel/arch/x86/crypto/glue_helper.ko:
kernel/arch/x86/crypto/aes-x86_64.ko:
kernel/arch/x86/crypto/camellia-x86_64.ko: kernel/crypto/xts.ko kernel/crypto/lrw.ko kernel/crypto/gf128mul.ko kernel/arch/x86/crypto/glue_helper.ko
kernel/arch/x86/crypto/blowfish-x86_64.ko: kernel/crypto/blowfish_common.ko
kernel/arch/x86/crypto/twofish-x86_64.ko: kernel/crypto/twofish_common.ko
kernel/arch/x86/crypto/twofish-x86_64-3way.ko: kernel/arch/x86/crypto/twofish-x86_64.ko kernel/crypto/twofish_common.ko kernel/crypto/xts.ko kernel/crypto/lrw.ko kernel/crypto/gf128mul.ko kernel/arch/x86/crypto/glue_helper.ko

#Just a case
[root kernel]#find . | grep camellia 
./arch/x86/crypto/camellia-aesni-avx-x86_64.ko
./arch/x86/crypto/camellia-x86_64.ko
./arch/x86/crypto/camellia-aesni-avx2.ko
./crypto/camellia_generic.ko

[root kernel]#cd arch/x86/crypto/
[root crypto]#insmod camellia-x86_64.ko 
insmod: ERROR: could not insert module camellia-x86_64.ko: Unknown symbol in module
[root crypto]#dmesg | tail
...
[198325.783578] camellia_x86_64: Unknown symbol xts_crypt (err 0)

[root crypto]#modprobe camellia-x86_64 
[root crypto]#lsmod | head
Module                  Size  Used by
camellia_x86_64        50481  0 
xts                    12679  1 camellia_x86_64
...

[root crypto]#rmmod xts 
rmmod: ERROR: Module xts is in use by: camellia_x86_64
[root crypto]#rmmod camellia_x86_64
[root crypto]#lsmod | head
Module                  Size  Used by
xts                    12679  0 
binfmt_misc            16949  1 
```


###Compiling Modules

`make -C /lib/module/$(uname -r)/build M=$PWD modules`

![](http://okye062gb.bkt.clouddn.com/2017-04-03-091414.jpg)



###Example Module

```
$ vi simplemodule.c
$ echo "obj-m := simplemodule.c" > Makefile
$ make -C /lib/modules/$(uname -r)/build M=$PWD modules
make: Entering directory '/usr/src/linux-headers-3.16.0-4-amd64'
make[1]: Entering directory `/usr/src/linux-headers-3.16.0-4-amd64'
  CC [M]  /media/sf_Public/opencourses/lynda-kernel/code/simplemodule.o
  Building modules, stage 2.
make[3]: Warning: File '/media/sf_Public/opencourses/lynda-kernel/code/simplemodule.o' has modification time 11 s in the future
  MODPOST 1 modules
  CC      /media/sf_Public/opencourses/lynda-kernel/code/simplemodule.mod.o
  LD [M]  /media/sf_Public/opencourses/lynda-kernel/code/simplemodule.ko
make[3]: warning:  Clock skew detected.  Your build may be incomplete.
make: Leaving directory '/usr/src/linux-headers-3.16.0-4-amd64'

[root code]#insmod simplemodule.ko
[root code]#lsmod | head -3
Module                  Size  Used by
simplemodule           12463  0 
[root code]#insmod simplemodule.ko
[root code]#lsmod | head -2
Module                  Size  Used by
simplemodule           12463  0 
[root code]#dmesg | tail -1
[203125.217518] In init module demo
[root code]#rmmod simplemodule 
[root code]#lsmod | head -3
Module                  Size  Used by
binfmt_misc            16949  1 
vboxsf                 41462  1
```

