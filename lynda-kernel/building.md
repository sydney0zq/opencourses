###Make a Kernel

Kernel Makefile supports `-j` option to make.

Made using make bzImage
    Or make uImage, make vmlinux

Image is bootloader dependent.

vmlinux is part of bootable image.
    Contains symbols.
    Large.


###make modules

Builds `.ko`'s for all the items selected as modules.

May be > 1000 modules.

Usually takes quite a bit longer than building a kernel.


###`make modules_install`

This copies modules and calls `depmod` to generate config files.

Default is to put under `lib/modules/KERNEL_VERSION`.


###make install

Install bzImage into `/boot`, renaming it vmlinuz-VERSION.

Should update grub config.

Should create an initramfs/initrd image.


###make clean

Removes generated files, like kernel and object files.

Can use `M=$PWD` and `-C` option to make to clean in a subdirectory.

Doesn't remove `.config`.

Be aware - `make mrproper` removes `.config`.


###Cross-Compilation

Need a cross-compiler installed.
    export CROSS_COMPILE=arm-linux-gnuabi-

make ARCH=arm uImage

> I should learn kernel from book, not such videos.


