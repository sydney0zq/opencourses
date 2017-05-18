/*
 * fork.c
 */

//#include "fork.h"

#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main(int argc, char ** argv)
{
    int pid;
    /* Fork another process */
    pid = fork();
    if (pid < 0){
        /* error occured */
        fprintf(stderr, "Fork Failed...");
        exit(-1);
    }else if (pid == 0){
        /* child process */
        printf("This is Child Process...\n");
/* You should NOTICE that 
 * `else if` and `else` will both be executed 
 * in two threads. 
 * Which means that fork will return value to each of them. */
    }else{
        /* parent process */
        printf("This is Parent Process\n");
        /* parent will wait for the child to complete */
        wait(NULL);
        printf("Child Complete...\n");
    }

    return 0;
}

