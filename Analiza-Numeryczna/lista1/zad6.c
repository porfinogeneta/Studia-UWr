#include <math.h>
#include <stdio.h>
#include <stdlib.h>
//3,141592 <- tyle ma wyjść
//3.141590 <- 4 poza, 500 tys, działania na double
//3.141588 <- dla 4 poza, 250 tys. działania na double
//3.141588 <- dla 4 w, 250 tys, działania na double
//3.141590 <- dla 4 w 500tys, działania na double
//3.141592 <- dla 4 w dla 4mln, działania na double
//3.141592 <- dla 4 w ,dla 2mln, działania na double
//3.141592 <- dla 4 poza, dla 2 mln, działania na double
//3.141593 <- dla 4 poza, dla 2mln - 1, działania na double
double  pi_seq(int a){
    double acc = 0.0;
    for (int i = 0; i < a; i++){
        acc += (pow((-1.0), i)/(2.0*i + 1.0));
    }
    return 4*acc;
}

double get(void) {
    double acc = 0.0;
    double k = 0.0;
    double epsilon = 1e-6;

    while (fabs(acc - M_PI) > epsilon) {
        acc += 4.0 * (pow(-1, k) / (2.0 * k + 1.0));
        k++;
    }
    printf("Pi estimate: %.6lf for k = %.0lf\n", acc, k);
    return k;
}

void get_pi(FILE *file){
    double pi = 3.141593;
    double acc = 0.0;
    double k = 0.0;
    while (k < 2000000){
        acc += 4.0*(pow(-1, k)/(2.0*k + 1.0));
        k++;
        fprintf(file, "Pi estimate: %.6lf for k = %.0lf\n", acc, k);
    }
}

void get_pif(FILE *file){
    float pi = 3.141593;
    float acc = 0;
    float k = 0;
    while (k < 2000000){
        acc += 4.0*(powf(-1, k)/(2.0*k + 1.0));
        k++;
        fprintf(file, "Pi estimate: %.6f for k = %.0f\n", acc, k);
    }
}

int main(void){
    get();
}