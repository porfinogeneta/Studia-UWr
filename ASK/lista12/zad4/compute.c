#include "stdio.h"


void compute2(long *a, long *b, long k) {
    long n = 1 << k;
    for (long i = 0; i < n; i++)
        a[i * n] = a[i] = 0;
    for (long i = 1; i < n; i++)
        for (long j = 1; j < n; j++)a[j * n + i] = i * j;
    for (long i = 1; i < n; i++)
        for (long j = 1; j < n; j++)
         b[i * n + j] = a[i * n + j] + a[(i - 1) * n + (j - 1)];
     }

// kompilator średnio sobie poradził - 62 linie kodu assembly
// optymalizacja
// - złączenie dwóch ostanich pętli
// - zamiana środkowych pętli, porządek row-major
// - wyzerowanie pierwszego wiersza i kolumny wewnątrz głównej pętli, usunięcie zerującej pętli
// skorzystanie z raz policzonego iloczynu, bez potrzeby ciągłego sięgania do pamięci
// - 41 linii kodu assembly


void compute2_opt(long *a, long *b, long k) {
    long n = 1 << k;
    a[0]; // to wyzeruje 0 indeks, do którego nie mamy zasięgu
    // pierwszy rząd i pierwsza kolumna to zera
    for (long i = 1; i < n; i++) {
        a[i * n] = a[i] = 0; // reszta iteracji jest taka sama, oprócz elementu na zero
        for (long j = 1; j < n; j++) {
            // mnożenie przemiene + zapełnimy indeksy zatem można odwócić kolejność dostępów do pamięci
            long mul = i * j; // odwołamy się do już raz policzonego iloczynu // rematerialization
            a[i * n + j] = mul;
            b[i * n + j] = mul + ((i - 1) * (j - 1)); // w pamięci pod wcześniejszym adresem był po prostu iloczyn, więc ten iloczyn zapisuję jawnie
        }
    }

}


void printMatrix(long *matrix, long n) {
    for (long i = 0; i < n; i++) {
        for (long j = 0; j < n; j++) {
            printf("%3ld ", matrix[i * n + j]);
        }
        printf("\n");
    }
}

int main(void){

    long a1[16] = {0};
    long b1[16] = {0};
    printf("Test 1:\n");
    compute2(a1, b1, 2);
    printf("Matrix A:\n");
    printMatrix(a1, 4);
    printf("Matrix B:\n");
    printMatrix(b1, 4);
    printf("\n");

    long a2[16] = {0};
    long b2[16] = {0};
    printf("Test 1:\n");
    compute2_opt(a2, b2, 2);
    printf("Matrix A opt:\n");
    printMatrix(a2, 4);
    printf("Matrix B opt:\n");
    printMatrix(b2, 4);
    printf("\n");


    return 0;
}