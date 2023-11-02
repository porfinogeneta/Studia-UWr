#include <math.h>
#include <stdio.h>

double get(double x) {

    double epsilon = 1e-6;
    double res = 0.0;
    while ((fabs(res - 2023) > epsilon)) {
        res = 0.0;
        res += 4046.0 / (sqrt(pow(x, 14) + 1) + 1);
        printf("Our res estimation %.6lf\n", res);
    }
    return res;
}

int main(void){
    get(0.001);
}
