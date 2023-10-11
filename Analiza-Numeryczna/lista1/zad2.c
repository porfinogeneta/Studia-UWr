#include <math.h>
#include <stdio.h>

double f1(double x){
    return 4046*(sqrt(pow(x, 14) + 1) - 1)/ pow(x, 14);
}

int main(void){
    printf("%lf", f1(0.001));
}
