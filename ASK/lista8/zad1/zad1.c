
//  D na stosie, jest to podpięcie do stdio.h - U jak undefined
extern int printf(const char *, ...);//E
//  D gdzieś na stosie, - U
extern long buf[]; //E
// D .data     R .data
long *bufp0 = &buf[0]; //[G]
// D .bss - normalnie byłaby .data ale domyślnie wartość niezadeklarowana to 0, czyli wpisuje się do .bss
static double sum = 0.0; //[L]
//     D   .text
static void incr() { // [L]
//    D   .bss
    static int count = 0;
    count++;
 }

//     D .text
 void addf(void) { //[G]
//      R
     sum += 3.14;
//     R           R        R
     printf("sum = %f\n", sum);
     }
//    D .text
void swap(int i) { //[G]
//      R
     incr();
//   linker nic nie wie o temp
    long temp = *bufp0; // R
//     R       R
     *bufp0 = buf[i];
//     R       R
     buf[i] = temp;
}
