#include "stdio.h"
#include "math.h"

double bisec(double a, double b, double epsilon){
    double mid = (a+b)/2.0;
    while (fabs(a - b) > epsilon) {
        mid = (a+b)/2.0;
        double av = pow(a, 4.0) - log(a + 4.0);
        double mva = pow(mid, 4.0) - log(mid + 4.0);
        // mamy inny znak w środku i 'na lewo', zacieśniamy przedział
        if (av * mva < 0){
            b = mid;
        }else {
            a = mid;
        }
    }
    return mid;
}


int main(void){
    printf("Przedział (-1.2;-0.8): %lf\n", bisec(-1.2, -0.8, 1e-8));
    printf("Przedział (1.0;1.2): %lf\n", bisec(1.0, 1.2, 1e-8));
    return 0;
}

