#include <math.h>
#include <stdio.h>
#include <stdlib.h>

double* integral(double n){
    double acc = log(2024.0/2023.0);
    double* res = (double*)malloc((n+1) * sizeof(double ));
    res[0] = acc;
    for (double i = 1.0; i <= n; i++){
        res[(int) i] = 1.0/i - 2023.0*acc;
        acc = res[(int) i];
    }
    return res;
}

int main(void){
    double n = 20.0;
    double* pres = integral(n);
    for (int i = 1; i <= n; i++){
        printf("Result of integral number: %d is: %lf\n", i, pres[i]);
    }
}

