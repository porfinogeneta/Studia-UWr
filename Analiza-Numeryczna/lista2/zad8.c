#include <math.h>
#include <stdio.h>

double factorial(double n){
    double c, fact = 1;

    for (c = 1; c <= n; c++){
        fact = fact * c;
    }
    return fact;
}

double lim(double x) {
    return (14 *
                  (pow(17.0, 2) * (pow(x, 2)) / factorial(2) -
                   (pow(17.0, 4) * (pow(x, 4)) / factorial(4)) +
                   (pow(17.0, 8) * (pow(x, 8)) / factorial(8))))
            / pow(x, 2);
}

int main(void){
    for (int i = 11; i <= 20; i++){
        printf("Double precision %lf \n", lim(pow(10, (-1 * i))));
    }
}
