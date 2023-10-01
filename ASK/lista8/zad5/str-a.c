/* str-a.c */
 #include <stdio.h>
// gcc -g  str-a.c str-b.c  -g umożliwia debugowanie
//  gdb ./a.out
// break str-a.c:7 // breakpoint
// run
char *somestr(void);

int main(void) {
    char *s = somestr();
    s[5] = '\0'; //próbujemy coś zapisać w sekcji .rodata, to podowuje error
    puts(s);
    return 0;
}