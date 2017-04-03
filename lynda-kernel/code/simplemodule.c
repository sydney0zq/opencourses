/*
 * module.c
 */

#include <linux/init.h>
#include <linux/module.h>
#include <linux/sched.h>

int init_sample(void){
    printk("In init module demo\n");
    return 0;
}

void cleanup_simple(void){
    printk("In cleanup module simple\n");
}

module_init(init_sample);
module_exit(cleanup_simple);

