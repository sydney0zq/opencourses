###Linux Kernel Fundamentals: Chapter 1, Surveying the Linux Kernel

1. What kernel version is your Linux system running?

```
$ uname -r
3.16.0-4-amd64
```


2. What is the size of the kernel  le that corresponds to the kernel your system is running?

```
$ ls -l /boot/vmlinuz-3.16.0-4-amd64
-rw-r--r-- 1 root root 3128784 Mar  8 07:58 /boot/vmlinuz-3.16.0-4-amd64
```


3. How much RAM is available to your running kernel? Note: It may or may not be the amount of physical RAM on your system.

```
$ head /proc/meminfo
MemTotal:         506136 kB
MemFree:           33440 kB
MemAvailable:     440040 kB
Buffers:          122648 kB
Cached:           229600 kB
SwapCached:         3516 kB
Active:           244632 kB
Inactive:         134364 kB
Active(anon):      13572 kB
Inactive(anon):    14316 kB

$ free
total       used       free     shared    buffers     cached
Mem:        506136     472860      33276       1140     122656     229620
-/+ buffers/cache:     120584     385552
Swap:       392188      79832     312356
```


4. The command `strace` will display the system calls that a process makes as it runs. Using the man command, determine what option for `strace` will show a summary, with a count, of the number of times a process called each system call. Using that option, what system call is called the most by the command `date`?

```
$ man strace        #to find out `count` parameter
$ strace -c date
Mon Apr  3 13:55:08 CST 2017
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
  0.00    0.000000           0         3           read
  0.00    0.000000           0         1           write
  0.00    0.000000           0         4           open
  0.00    0.000000           0         6           close
  0.00    0.000000           0         6           fstat
  0.00    0.000000           0         1           lseek
  0.00    0.000000           0        11           mmap
  0.00    0.000000           0         4           mprotect
  0.00    0.000000           0         3           munmap
  0.00    0.000000           0         3           brk
  0.00    0.000000           0         3         3 access
  0.00    0.000000           0         1           execve
  0.00    0.000000           0         1           arch_prctl
------ ----------- ----------- --------- --------- ----------------
100.00    0.000000                    47         3 total
```


5. Can you determine, using strace, what system call is used to change the directory?

```
$ strace cd /tmp
...(A bunch output)
$ which cd
/usr/bin/cd
$ file /usr/bin/cd
/usr/bin/cd: POSIX shell script, ASCII text executable
$ cat /usr/bin/cd
#!/bin/sh
builtin cd "$@"
```


6. Run a sleep 100 with & (to put it in the background). What  les does its process have open?

```
$ sleep 100 &
$ jobs
[1]+  Running                 sleep 100 &  (wd: /dev)
$ jobs -p
20323
$ cd /proc/20323/fd
fd/     fdinfo/ 
$ cd /proc/20323/fd
fd/     fdinfo/ 
$ cd /proc/20323/fd/
$ ll
total 0
dr-x------ 2 root root  0 Apr  3 14:04 .
dr-xr-xr-x 9 root root  0 Apr  3 14:04 ..
lrwx------ 1 root root 64 Apr  3 14:05 0 -> /dev/pts/1
lrwx------ 1 root root 64 Apr  3 14:05 1 -> /dev/pts/1
lrwx------ 1 root root 64 Apr  3 14:05 2 -> /dev/pts/1
$ tty
/dev/pts/1
```


7. Does your system have a PCI Ethernet device?

```
$ lspci | grep -i ethernet
00:03.0 Ethernet controller: Intel Corporation 82540EM Gigabit Ethernet Controller (rev 02)
```


8. Is the kernel variable `ip_forward` (under /proc/sys/...) set to 1 or 0 on your system?

```
$ cd /proc
$ find . -name ip_forward
./sys/net/ipv4/ip_forward
$ cat /proc/sys/net/ipv4/ip_forward
0
$ sysctl -a | grep ip_forward
net.ipv4.ip_forward = 0
net.ipv4.ip_forward_use_pmtu = 0
```


9. According to `/sys/block`, do you have a block device (disk) sda? If so, do you have device files for partitions of sda? How many? Using strace, does the command `fdisk -l` (run it as root), open any files under `/sys/dev/block`?

```
$ cd /sys/block/
$ ls
sda  sr0
$ ll
total 0
drwxr-xr-x  2 root root 0 Mar 30 20:58 .
dr-xr-xr-x 13 root root 0 Apr  3 13:28 ..
lrwxrwxrwx  1 root root 0 Mar 30 20:58 sda -> ../devices/pci0000:00/0000:00:0d.0/ata3/host2/target2:00:0/2:0:0:0/block/sda
lrwxrwxrwx  1 root root 0 Apr  3 14:13 sr0 -> ../devices/pci0000:00/0000:00:0d.0/ata4/host3/target3:00:0/3:0:0:0/block/sr0

$ cd sda/
$ ls
alignment_offset  device             events_poll_msecs  power      ro    size       trace
bdi               discard_alignment  ext_range          queue      sda1  slaves     uevent
capability        events             holders            range      sda2  stat
dev               events_async       inflight           removable  sda5  subsystem

> Standard error does not go into pipe
$ strace fdisk -l  |& grep /sys/block
open("/sys/block/sr0/dev", O_RDONLY|O_CLOEXEC) = 4
open("/sys/block/sda/dev", O_RDONLY|O_CLOEXEC) = 4
open("/sys/block/sda1/dev", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
open("/sys/block/sda2/dev", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
open("/sys/block/sda5/dev", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
$ strace fdisk -l  |& grep /proc
open("/proc/partitions", O_RDONLY)      = 3
$ cat /proc/partitions 
major minor  #blocks  name
11       0      58016 sr0
8        0    8388608 sda
8        1    7993344 sda1
8        2          1 sda2
8        5     392192 sda5
```


10. Using dmesg and grep, do you see the kernel reporting the kernel command line? If not, can you determine if the boot messages from the kernel were lost? Does your system have a log file that recorded the boot messages? You can grep for `BOOT_IMAGE` under /var/log to look.

```
$ dmesg | grep -i command
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-3.16.0-4-amd64 root=UUID=15bc3ed6-563f-478c-aca7-1b884c6c69a0 ro initrd=/install/initrd.gz quiet
[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-3.16.0-4-amd64 root=UUID=15bc3ed6-563f-478c-aca7-1b884c6c69a0 ro initrd=/install/initrd.gz quiet

$ cd /var/log
$ grep -r "Command line" * 
```


11. What other device files are character devices and share the same major number with /dev/null?

```
$ cd /dev
$ ls -l  | grep ^c | grep " 1,"
crw-rw-rw- 1 root    root      1,   7 Mar 30 20:58 full
crw-r--r-- 1 root    root      1,  11 Mar 30 20:58 kmsg
crw-r----- 1 root    kmem      1,   1 Mar 30 20:58 mem
crw-rw-rw- 1 root    root      1,   3 Mar 30 20:58 null
crw-r----- 1 root    kmem      1,   4 Mar 30 20:58 port
crw-rw-rw- 1 root    root      1,   8 Mar 30 20:58 random
crw-rw-rw- 1 root    root      1,   9 Mar 30 20:58 urandom
crw-rw-rw- 1 root    root      1,   5 Mar 30 20:58 zero

# The major number is all 1, so they use the same driver but not same behavior.
```


