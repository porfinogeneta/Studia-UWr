#include "stdio.h"
#include "math.h"

void bisec(double a, double b, int steps){


    for (int i = 0; i < steps; i++){
        double en_approxi =  (pow(2.0, -1.0-i))*(1.0 - 0.0);
        double mid = (a+b)/2.0;
        double va = a - 0.49;
        double vmid = mid - 0.49;
        if (va * vmid < 0){
            b = mid;
        }else {
            a = mid;
        }
        // błąd w n-tym kroku to różnica między znalezionym MZ a faktyczną jego wartością, ZF zero function - miejsce zerowe
        printf("|en| = %lf | ZF = %lf | error: %lf| in step %d\n",en_approxi, mid, fabs(0.49 - mid), i);
    }
}


int main(void){
    bisec(0.0, 1.0, 5);
    return 0;
}
