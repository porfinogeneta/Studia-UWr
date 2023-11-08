#include "stdio.h"
#include "math.h"



int main(void){
    // ciąg rosyjski
    double Er0 = 0.763907023;
    double Er1 = 0.543852762;
    double Er2 = 0.196247370;
    double Er3 = 0.009220859;

    // ciąg amerykański
    double Ea0 = 0.605426053;
    double Ea1 = 0.055322784;
    double Ea2 = 0.004819076;
    double Ea3 = 0.000399783;


    printf("Er3/Er2 %lf\n", Er3 / Er2);
    printf("Er2/Er1 %lf\n", Er2 / Er1);
    printf("log(Er3/Er2)/log(Er2/Er1) %lf\n", (log(Er3 / Er2)) / (log(Er2 / Er1)));

    printf("=======================================\n");

    printf("Ea3/Ea2 %lf\n", Ea3 / Ea2);
    printf("Ea2/Ea1 %lf\n", Ea2 / Ea1);
    printf("log(Ea3/Ea2)/log(Ea2/Ea1) %lf\n", (log(Ea3 / Ea2)) / (log(Ea2 / Ea1)));
    return 0;
}

