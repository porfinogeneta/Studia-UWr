#include "stdio.h"
#include "sys/types.h"

int main(){

    pid_t pid;

    for (int i = 0; i < 3; ++i){
        if (pid = fork() == 0){
            printf("hey process started, current i: %d\n", i);
        }
    }


    return 0;
}