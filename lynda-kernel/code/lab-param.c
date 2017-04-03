#include <linux/module.h>
#include <linux/sched.h>
#include <linux/kernel.h>

//Use
//insmod lab-param.ko number=1234 word="me"


MODULE_AUTHOR("Sydney Zhou");
MODULE_DESCRIPTION("A very simple loadable module");

static int number = 24061;
static char * word = "strawberry";
module_param (number, int, S_IRUGO);
module_param (word, charp, S_IRUGO);

MODULE_PARM_DESC (number, "A sample integer modifiable paramter");
MODULE_PARM_DESC (word, "A sample string modifiable paramter");

int my_init_module(void){
    printk("number = %d word = %s\n", number, word);
    return 0;
}

module_init(my_init_module);

void my_cleanup_module(void){
    printk("The module is now unloaded...\n");
}

module_exit(my_cleanup_module);


