#include <stddef.h>
#include "stdio.h"

void foobar(long a[], size_t n, long y, long z) {
     for (int i = 0; i < n; i++) {
         long x = y - z; // niezmiennik
         long j = 7 * i; // zmienna indukcyjna // osłabienie operacji, zamiana mnożenia na dodawanie
         a[i] = j + x * x; // osłabienie tej operacji, przez wykonanie mnożenia na początku
         }
     }
     //niezmiennik n

// przed pętlą lądują obliczenia związane ze stałymi, bo nie ma na nie wpływu aktualny indeks iteracji
// osłabioniu uległa instrukcja przypisania do x, teraz nie trzeba już tworzyć nowej zmiennej,
// osłabioniu uległo także dodawanie stałej do kwadratu x (x*x) + j, dzięki czemu możemy tę operację zapisać w jednej instrukcji
void foobar_opt(long a[], size_t n, long y, long z){
    y = y - z;
    y *= y;
    int i = 0;
    while (i < n){
        a[i] = y;
        i++;
        y += 7;
    }
}


int main(void){

    long test[5] = {1, 2, 3, 4, 5};
    long test1[5] = {1, 2, 3, 4, 5};

    foobar(test, 5, 2, 3);

    foobar_opt(test1, 5, 2, 3);
    for (int i = 0; i < 5; ++i) {
        printf("normal: %ld ", test[i]);
        printf("opt: %ld ", test1[i]);
        printf("\n");
    }

    return 0;
}