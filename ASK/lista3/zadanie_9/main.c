#include <stdio.h>
#include "limits.h"

// zad 8


// zad 9
__int32_t float2int(__int32_t f){
    __int32_t s = f >> 31; // bit znaku
    __int32_t e = ((f >> 23) & 255) - 127;
    __uint32_t m =  (f << 8) | 0x80000000;

    //same jedynki
    if (e == 128){
        return 0x80000000;
    }
    // jak wykładnik jest ujemny, to zaokrąglam do 0
    if (e <= 0){
        return 0;
    }
    // e > 0
    else{
        // chcemy po prostu to wymnożyć
        if (s == 0){
            return (int) m * e;
        }
        return (int)  (m * -e);
    }
}

// oblicza długość prefixu z s, który jest wspólny z d
long puzzle(char *s, char *d){
    char *result = s;
    while (1){
        char t1 = *result; // t1 przechowuje literę z s
        char *t2 = result + 1; // t2 przechowuje wskaźnik na s+1
        char *t3 = d; // t3 przechowuje wskaźnik na d
        char t4; // t4 przechowuje literę z d
        do {

            t4 = *t3;
            t3 += 1; // przesuwamy się na d o 1 literę
            if (t4 == 0){ // gdy słowo d dobiegnie końca
                return (long)(result - s); // zwracamy różnicę we skaźnikach
            }

        }while(t4 != t1); // dopóki litery się różnią
        result = t2; // update wskaźnika, t2 było przesuwane o 1
    }

}

int hashfn(char *str) {
    // A simple example hashing function implementation
    return 0;
}

int main() {
//    printf("Hello, World!\n");
//    double a = INT_MAX;
//    double b = INT_MAX;
//    double c = INT_MAX-256;
//
//    double w = (a * b) *c;
//    double w2 = a*(b * c);
//
//    printf("%lf oraz %lf\n", w, w2);
//
//    printf("%d", float2int(2141801045));

    struct A {
        __int8_t  a;
        void   *b;
        __int8_t  c;
        __int16_t d;
    };
    struct B {
        double b;
        void *c;
         __int16_t a;

    };

    struct node {
        char id[2];
        int (*hashfn)(char *);
        short flags;
        union {
            struct {
                short n_key;
                int n_data[2];
                unsigned char n_type;
                 } s;
             unsigned l_value[2];
             } u;
         } node;

    struct nodeopt {
        union {
            struct {
                short n_key;
                int n_data[2];
                unsigned char n_type;
            } s;
            unsigned l_value[2];
        } u;
        int (*hashfn)(char *);
        char id[2];
        short flags;

    } nodeopt;

    union {
        struct {
            short n_key;
            int n_data[2];
            unsigned char n_type;
        } s;
        unsigned l_value[2];
    } u;



    printf("Struct A: %zu\n", (sizeof(struct A) ));
    printf("Struct B:  %zu\n", (sizeof(struct B) ));

    struct A adresy = {0, NULL, 0, 0};
    printf("%ld\n", (void *)&adresy.a - (void *)&adresy);
    printf("%ld\n", (void *)&adresy.b - (void *)&adresy);
    printf("%ld\n", (void *)&adresy.c - (void *)&adresy);
    printf("%ld\n", (void *)&adresy.d - (void *)&adresy);
    float test = (float ) 0x3f800000;
    printf("%f\n", test);
    int n_data[2];
    int *hashfn = hashfn;
    printf("%lu", sizeof( u ));

    return 0;
}
