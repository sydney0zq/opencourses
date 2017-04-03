all: lab.c lab-error.c lab-doc.c lab-param.c
	make -C /lib/modules/`uname -r`/build M=$(PWD) modules

clean:
	make -C /lib/modules/`uname -r`/build M=$(PWD) clean

obj-m := lab.o lab-error.o lab-doc.o lab-param.o
