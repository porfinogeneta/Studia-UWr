#include <math.h>
#include <stdio.h>

double countln(void) {
    double acc = 0.0;
    double k = 1.0;
    double epsilon =0.5e-6;

    while (fabs(acc - log(2.0)) > epsilon) {
        acc += pow(-1, k-1.0) * (1.0/k);
        k++;
    }
    printf("ln(2) estimate: %.6lf for k = %.0lf\n", acc, k);
    return k;
}


int main(void){
    countln();
}