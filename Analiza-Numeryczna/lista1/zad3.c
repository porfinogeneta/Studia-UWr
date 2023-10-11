#include <math.h>
#include <stdio.h>

float  f2s(float  x){
    return (14*(1 - (cosf(17*x))))/ (powf(x, 2));
}

double f2d(double x){
    return (14*(1 - (cos(17*x))))/ (pow(x, 2));
}


int main(void){
    for (int i = 11; i <= 20; i++){
        printf("Single precision %f \n", f2s(powf(10, (-1 * i))));
    }
    for (int i = 11; i <= 20; i++){
        printf("Double precision %lf \n", f2d(pow(10, (-1 * i))));
    }
}
