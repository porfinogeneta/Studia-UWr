#include <stdio.h>
#include <math.h>

void countf_normal(double a, double b, double c) {
    double x1 = (-b + sqrt(pow(b, 2.0) - 4 * a * c)) / (2.0 * a);
    double x2 = (-b - sqrt(pow(b, 2.0) - 4 * a * c)) / (2.0 * a);

    printf("Normal function: \n");
    printf("Parameters a: %lf, b: %lf, c: %lf\n", a, b, c);
    printf("x1: %lf, x2: %lf\n", x1, x2);
    printf("Apply x1 and x2:\n");
    printf("result f(x1): %lf\n", pow(x1, 2.0) * a + b * x1 + c);
    printf("result f(x2): %lf\n\n", pow(x2, 2.0) * a + b * x2 + c);
}

void countf_better(double a, double b, double c) {
    double x1 = (-b + sqrt(pow(b, 2.0) - 4 * a * c)) / (2.0 * a);
    double x2 = (-b - sqrt(pow(b, 2.0) - 4 * a * c)) / (2.0 * a);

    if (b > 0) {
        x1 = 2.0 * c / (-b - sqrt(pow(b, 2.0) - 4.0 * a * c));
    } else if (b < 0) {
        x2 = 2.0 * c / (-b + sqrt(pow(b, 2.0) - 4.0 * a * c));
    }

    printf("Better function: \n");
    printf("Parameters a: %lf, b: %lf, c: %lf\n", a, b, c);
    printf("x1: %lf, x2: %lf\n", x1, x2);
    printf("result f(x1): %lf\n", pow(x1, 2.0) * a + b * x1 + c);
    printf("result f(x2): %lf\n\n", pow(x2, 2.0) * a + b * x2 + c);
}

int main(void) {
    double a = 0.25;
    double b = 1e6; // b^2 >> 4ac i b > 0
    double c = 0.25;

    countf_normal(a, b, c);
    countf_better(a, b, c);

    a = 0.25;
    b = -1e6; // b^2 >> 4ac b i < 0
    c = 0.25;
    countf_normal(a, b, c);
    countf_better(a, b, c);

    return 0;
}
