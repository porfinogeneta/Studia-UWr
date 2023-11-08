#include "stdio.h"
#include "math.h"

// dla funckji 3(x-1)^3
void olver_method1(double xn, double xn_prev,  int n){
    double xn_next = xn - 3.0*(xn - 1.0) - 1.0/9.0*(xn - 1.0);
    if (n == 2){
        printf("%lf\n", xn_prev);
        printf("%lf\n", xn);
        printf("%lf\n", xn_next);
    }else {
        olver_method1(xn_next, xn, ++n);
    }
}

// dla funkcji -2(x-2)^2
void olver_method2(double xn, double xn_prev,  int n){
    double xn_next = xn - 0.5*(xn - 2.0) + (0.125 * xn - 2.0);
    if (n == 2){
        printf("%lf\n", xn_prev);
        printf("%lf\n", xn);
        printf("%lf\n", xn_next);
    }else {
        olver_method1(xn_next, xn, ++n);
    }
}

// dla funkcji (x-2)(x-3) = x^2 - 5x + 6
void olver_method3(double xn, double xn_prev,  int n){
    double xn_next = xn + ((-(xn*xn) + 5*xn - 6.0)/(2*xn - 5.0)) - (((xn-2.0)*(xn-2.0)*(xn-3.0)*(xn-3.0))/ pow(2.0*xn - 5.0, 3.0)) ;
    if (n == 2){
        printf("%lf\n", xn_prev);
        printf("%lf\n", xn);
        printf("%lf\n", xn_next);
    }else {
        olver_method1(xn_next, xn, ++n);
    }
}

double count_congruence(double xn_next, double xn, double xn_prev, double alpha){
    double En_next = fabs(xn_next - alpha);
    double En = fabs(xn - alpha);
    double En_prev = fabs(xn_prev - alpha);
    return (log(En_next/En)) / (log(En / En_prev));

}




int main(void){
    printf("Olver method for 3(x-1)^3, and x0 = -1.6\n");
    olver_method1(-1.6, -1.6, 0);
    printf("Congruence is: %lf", count_congruence(25.462826, -10.587654, 6.48888, 1.0));

    printf("Olver method for -2(x-2)^2, and x0 = 5\n");
    olver_method2(5.0, 5.0, 0);
    printf("Congruence is: %lf", count_congruence(6.013889, -1.375000, 2.125000, 1.0));

    printf("Olver method for -2(x-2)^2, and x0 = 5\n");
    olver_method3(-10.0, -10.0, 0);
    printf("Congruence is: %lf", count_congruence(-13.272853, 7.760825, -2.202496, 3.0));
    return 0;
}

