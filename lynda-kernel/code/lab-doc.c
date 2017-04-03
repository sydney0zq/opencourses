/*
 * lib.c
 */
#include <linux/module.h>
#include <linux/sched.h>
#include <linux/kernel.h>

MODULE_AUTHOR("Sydney Zhou");
MODULE_DESCRIPTION("A very simple loadable module");
//Use $ modinfo -a ./lab-doc.ko
//$ modinfo -d ./lab-doc.ko

int my_init_module(void){
    printk("The module is now loaded...\n");
    return 0;
}

module_init(my_init_module);

void my_cleanup_module(void){
    printk("The module is now unloaded...\n");
}

module_exit(my_cleanup_module);


