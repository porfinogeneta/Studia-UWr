#include <math.h>
#include <stdio.h>

double seq(int n){
    if (n == 0){
        return 1.0;
    } else if (n == 1){
        return -(1.0/9.0);
    }else {
        return (80.0/9.0)*seq(n-1) + seq(n-2);
    }
}

double seqc(int n){
    double acc = 1.0;
    for (int i = 1; i <= n; i++){
        acc *= -(1.0/9.0);
    }
    return acc;
}


int main(void){
    for (int i = 2; i <= 50; i++){
        printf("Double precision seq index: %d value: %lf \n", i, seq(i));
    }
    for (int i = 2; i <= 50; i++){
        printf("Double precision given formula: %d value: %lf \n", i, seqc(i));
    }
}