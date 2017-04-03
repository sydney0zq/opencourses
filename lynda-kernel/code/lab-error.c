/*
 * lab-error.c
 */



#include <linux/module.h>
#include <linux/sched.h>

int my_init_module(void){
    printk("The module is now load...\n");
    return -1;
}

module_init(my_init_module);

void my_cleanup_module(void){
    printk("The module is now unloaded...\n");
}

module_exit(my_cleanup_module);

