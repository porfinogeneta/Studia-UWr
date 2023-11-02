#include <stdio.h>
#include <math.h>

double fa(double x){
    return 1.0 / (pow(x, 3.0) + sqrt(pow(x, 6.0) + pow(2023.0, 2.0)));
}

double fafixed(double x){
    return (sqrt(pow(x, 6.0) + pow(2023.0, 2.0)) - pow(x, 3.0)) / pow(2023.0, 2.0);
}

// ===================================
double fb(double x){
    return log2(x) - 2;
}

double fbfixed(double x){
    return log2(x/4.0);
}

// ==============================
double fc(double x){
    return (atan(x) - x) / pow(x, 3.0);
}
double fcfixed(double x){
    return -1.0/3.0 + pow(x, 2.0)/5.0 - pow(x, 4.0)/7.0 + pow(x, 6.0)/9.0 - pow(x, 8.0)/11.0 + pow(x, 10.0)/13.0;
}

int main(void) {
    printf("Result (a) not fixed: %.20lf\n", fa(-1e6));
    printf("Result (a) fixed:     %.20lf\n", fafixed(-1e6));

    printf("============================================\n");
    printf("Result (b) not fixed: %.20lf\n", fb(3.999999999999999));
    printf("Result (b) fixed:     %.20lf\n", fbfixed(3.999999999999999));

    printf("============================================\n");
    // tu już tracimy cyfry znaczące, jest już zaokrąglone pod koniec
    printf("Result (c) not fixed: %.20lf\n", fc(0.00000001));
    printf("Result (c) fixed:     %.20lf\n", fcfixed(0.00000001));

    return 0;
}
