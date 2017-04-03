/*
 * lib.c
 */
#include <linux/module.h>
#include <linux/sched.h>
#include <linux/kernel.h>

int my_init_module(void){
    printk("The module is now loaded...\n");
    return 0;
}

module_init(my_init_module);

void my_cleanup_module(void){
    printk("The module is now unloaded...\n");
}

module_exit(my_cleanup_module);


