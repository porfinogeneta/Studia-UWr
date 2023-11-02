#include "stdio.h"
#include "math.h"

// be
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

double newtonrecu(double xn, double a, int steps, int approximation){
    // sprawdzamy czy wartości zaczęły się powtarzać
    int d = (int)((1.5*xn - ((0.5 * a) * pow(xn, 3.0))) * approximation);
    // czy to co nam wyszło w poprzedniej iteracji się powtarza, oznaza to prawidłowy wynik końcowy
    if ((int)(xn * approximation) == d)
    {
        printf("Approximation %lf ; done in  %d steps\n", xn, steps);
        return xn;
    }
    // przekroczyliśmy górny limit kroków
    else if (steps > 1000){
        printf("Approximation has not been achieved!\n");
        return xn;
    }
    else {
        // obliczenie kolejnego kroku
        return newtonrecu(1.5*xn - ((0.5 * a) * pow(xn, 3.0)), a,  steps + 1, approximation);
    }
}

int main(void){
    // we count for a = 3
    printf("We count for a=5\n");
    printf("The result should be: %lf\n", sqrt(1.0/5.0));
    // x0 e (sqrt(1/3a), sqrt(5/3a)) = (0.258198, 0.577350)
    for (int i = 0; i < 10; ++i) {
        printf("x0 is %lf\n", 0.20 + i*0.04);
        printf("%lf\n", newtonrecu(0.20 + i*0.04, 5.0, 0, 1e4));
    }
    printf("===============================\n");
    printf("We count for a=50\n");
    printf("The result should be: %lf\n", sqrt(1.0/50.0));
    // x0 e (sqrt(1/3a), sqrt(5/3a)) = (0.081649, 0.182574)
    for (int i = 0; i < 10; ++i) {
        printf("x0 is %lf\n", 0.07 + i*0.013);
        printf("%lf\n", newtonrecu(0.07 + i*0.013, 50.0, 0, 1e4));
    }
    return 0;
}

