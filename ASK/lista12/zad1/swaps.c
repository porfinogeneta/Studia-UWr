#include "stdio.h"

void swap(long *xp, long *yp) {
     *xp = *xp + *yp; /* x+y */
     *yp = *xp - *yp; /* x+y-y = x */
     *xp = *xp - *yp; /* x+y-x = y */
}

// optimised swap
void swap_prim(long *restrict xp, long *restrict yp) {
    *xp = *xp + *yp; /* x+y */
    *yp = *xp - *yp; /* x+y-y = x */
    *xp = *xp - *yp; /* x+y-x = y */
}

//optimized?
void swap2(long *xp, long *yp) {
    long x = *xp, y = *yp;
    x = x + y, y = x - y, x = x - y;
    *xp = x, *yp = y;
}


int main(void){
    long x = 3;
    long y = 3;
    //swap(&x, &x);
    swap_prim(&y, &x);
    //swap2(&x, &x);
    printf("\n%p, %ld\n", &x, x);
}