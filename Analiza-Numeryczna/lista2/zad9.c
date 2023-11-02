#include "math.h"
#include "stdio.h"

double pi_esti_v1(int k){
    double x_prev = 2.0;
    for (int i = 1; i < k; i++){
        double k2 = pow(2.0, i);
        x_prev = k2 * sqrt(2* (1 - sqrt(1 - pow(x_prev/k2, 2.0))));
    }
    return x_prev;
}

double pi_esti_v2(int k){
    double x_prev = 2.0;
    for (int i = 1; i < k; i++){
        double k2 = pow(2.0, i);
        x_prev = x_prev * sqrt(2.0/(1 + sqrt(1.0 - pow(x_prev/k2, 2))));
    }
    return x_prev;
}

int main(void){
    for (int i = 1; i < 100; ++i) {
        printf("%lf\n", pi_esti_v2(i));
    }

}

