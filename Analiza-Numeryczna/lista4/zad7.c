#include "stdio.h"
#include "math.h"

double newton(double x_0, int steps){
    double x_n = x_0;
    double x_n1 = 0;
    double a = 5.0;
    for (int i = 0; i < steps; i++){
        x_n1 = 1.5*x_n - ((0.5 * a) * pow(x_n, 3.0));
        x_n = x_n1;
        if ((int)((1.0 / sqrt(5.0)) * 1000) == (int)(x_n * 1000)){
            break;
        }
    }
    return x_n;
}

double newton_recu(double yn, double m, int steps, int approximation){
    // nasza docelowa wartość
    int d = (int)((0.5*yn + m/(2.0*yn)) * approximation);
    // czy to co nam wyszło w poprzedniej iteracji się zgadza z właściwym wynikiem
    if ((int)(yn * approximation) == d) {
        printf("Done in %d steps\n", steps);
        return yn;
    }
        // przekroczyliśmy górny limit kroków
    else if (steps > 1000){
        printf("Approximation has not been achieved!\n");
        return yn;
    }
    else {
        // obliczenie kolejnego kroku ze wzoru
        return newton_recu(0.5*yn + m/(2.0*yn), m,  steps + 1, approximation);
    }
}

double count_sqrta(double y0, double m, int c){
    // parzysty wykładnik
    if (c % 2 == 0){
        // obliczenie wyniku to wyznaczenie y_n+1 i pomnożenie przez 2^k
        return newton_recu(y0, m, 0, 1e3) * (pow(2.0, (c/2.0)));
    }
    // nieparzysty wykładnik
    else {
        return newton_recu( y0, 2.0*m, 0, 1e3) * (pow(2.0, (c-1.0)/2.0));
    }
}

int main(void){
    printf("Counting for m=0.5 c=5\n");
    // y0 e (sqrt(2/3 * 0.5), sqrt(2m)) = (0.577350 1)
    // we begin with 0.45
    for (int i = 0; i < 10; ++i) {
        printf("y0 is %lf\n", 0.45 + i*0.05);
//        printf("Square root of m is: %lf\n", sqrt(0.5));
        printf("%lf\n", count_sqrta(0.45 + i*0.05, 0.5, 4));
    }
    printf("============================\n\n");
    printf("Counting for m=0.5 c=8\n");
    // y0 e (sqrt(2/3 * 0.5), sqrt(2m)) = (0.577350 1)
    // we begin with 0.45
    for (int i = 0; i < 15; ++i) {
        printf("y0 is %lf\n", 0.45 + i*0.05);
//        printf("Square root of 2m is: %lf\n", sqrt(1.0));
        printf("%lf\n", count_sqrta(0.45 + i*0.05, 0.5, 8));
    }

    return 0;
}

