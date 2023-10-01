#include "stdio.h"
//eliminacji wspólnych podwyrażeń (ang. common
//subexpression elimination) - policzenie tylko raz powtarzalnych zmiennych w programie
// i wykorzystywanie ich później

//(i-1)*n + j -> włożyć do stałej

long neigh(long a[], long n, long i, long j) {
    long ul = a[(i-1)*n + (j-1)]; // notacja (i-1)*n przejście do kolejnego wiersza
    long ur = a[(i-1)*n + (j+1)];
    long dl = a[(i+1)*n - (j-1)];
    long dr = a[(i+1)*n - (j+1)];
    return ul + ur + dl + dr;
}

// policzone tylko raz:
//
// (j-1) + (i-1)*n
// (i-1)*n + (j+1)
// (i+1)n - (j-1)
// (i+1)*n - (j+1)

// 14 instrukcji assembly
// zastąpienie działań na liczbach przez po prostu wyliczenie indeksu i jego poprawianie
long my_neigh_opy(long a[], long n, long i, long j){
    long idx = (i-1)*n + (j-1); // idx = ni - n + j - 1
    long res = a[idx]; // ul
    // teraz chcemy uzyskać // (i-1)*n + (j+1) = ni -n + j +1 // trzeba do idx + 2
    idx+=2; //  ni -n + j +1
    res += a[idx]; // ur
    // teraz do uzyskania jest // (i+1)*n - (j-1) = ni + n -j +1 // idx + 2n - 2j
    idx += n*2;
    idx -= j*2; // idx = ni + n -j +1
    res += a[idx]; // dl
    //teraz do uzyskania jest // (i+1)*n - (j+1) = ni + n -j - 1 // idx -= 2
    idx -= 2;
    return (res +a[idx]); // dr
}

//                rdi       rsi    rdx      rcx
long neigh_opt(long a[], long n, long i, long j){
    i--; // (i-1)   //rdx
    long j1 = j-1; // (j-1) //r8
    j++; // (j+1) rcx
    i *= n; // (i-1)*n
    n += n; //rsi // n = 2n
    n += i; //rdx n= 2n+i
    long a1 = j1 + i; // (j-1) + (i-1)*n    r9
    i += j; // (i-1)*n + (j+1)  rdx
    long res = a[i]; // ur
    i = n; //
    n -= j; // n = 2n+i - (j+1)
    res += a[a1]; // ul
    i -= j1; // i = n - (j-1)
    res += a[i];
    res += a[n];
    return res;
}

int main(void){

    long arr[] = {
            1, 2, 3,
            4, 5, 6,
            7, 8, 9
    }; // 3x3 matrix

    long n = 3;

    // Test case 1: Get neighbors of element at position (1, 1)
    long result1 = neigh(arr, n, 1, 1);
    long resultT = my_neigh_opy(arr, n, 1, 1);
    printf("Case 1: Expected result: 16, Actual result: %ld\n", result1);
    printf("Case 1: Expected result: 16, Actual result: %ld\n", resultT);

    return 0;
}
