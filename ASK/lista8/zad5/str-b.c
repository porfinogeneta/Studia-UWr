/* str-b.c */
// to idzie do .text
//char *somestr(void) {
//     return "Hello, world!";//to ląduje w sekcji .rodata
//}



// poprawiona wersja
// teraz nie będzie już błędów, ponieważ zmienna zaalokowana została w innej sekcji, z możliwością edytowania

char *somestr(void) {
     static char str[] = "Hello, world!"; // teraz zmienna jest przechowywana w sekcji .data
     return str;
}