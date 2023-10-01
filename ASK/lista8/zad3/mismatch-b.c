/* mismatch-b.c */
#include <stdio.h>
char main; // symbol słaby

void p2(void) { // symbol silny
    printf("0x%x\n", main);
}