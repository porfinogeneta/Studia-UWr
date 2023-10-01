#include <stddef.h>

__attribute__(())
    static size_t my_strlen(const char *s);

static size_t my_strlen(const char *s){
    size_t len = 0;
    while (*s++ != '\0'){
        len++;
    }
    return len;
}

const char *my_index(const char *s, char v) {
    for (size_t i = 0; i < my_strlen(s); i++)
        if (s[i] == v)
            return &s[i];
    return 0;
}
// po zastosowaniu atrybutu pure wynik działania funkcji my_strlen jest wrzucany do rejestru i wykorzystywany
int main(void){
    return 0;
}

//leaf
//
//    Calls to external functions with this attribute must return to the current compilation unit only by return or by exception handling. In particular, a leaf function is not allowed to invoke callback functions passed to it from the current compilation unit, directly call functions exported by the unit, or longjmp into the unit. Leaf functions might still call functions from other compilation units and thus they are not necessarily leaf in the sense that they contain no function calls at all.

// bez pure
// funkcja my_strlen zostanie wywołana tyle razy, jaki jest (indeks + 1) litery 'v' w słowie 's'
// będzie tak, ponieważ kompilator nie wie czy długość słowa 's' się nie zmieni, bo jest to jakiś dostęp do pamięci,
// o której on nic nie wie

//atrybut pure
//jeżeli funkcja jest wielokrotnie wywoływana, z tymi samymi argumentami i ma atrubut 'pure' to będzie
// wywołana tylko raz

//The pure attribute prohibits a function from modifying the state of the program that is observable
// by means other than inspecting the function’s return value. However, functions declared with the
// pure attribute can safely read any non-volatile objects, and modify the value of objects in a way
// that does not affect their return value or the observable state of the program.

// charakterytyka czystych funkcji
// jeżeli są wielokrotnie wywoływane, z tymi samymi argumentami, ich pierwsze wywołanie może być zapisane w zmiennej
// nie mogą modyfikować danych, na których operują, tylko zwracać wartość
// może czytać non-volatile memory, nawet jeżli ona ulegnie zmianie
// nie może mieć żadnych obserwowalnych efektów ubocznych























// z godbolta, wynika że w przypdaku wykonania inliningu
//
//my_strlen:
//push    rbp
//mov     rbp, rsp
//mov     QWORD PTR [rbp-24], rdi
//        mov     QWORD PTR [rbp-8], 0
//jmp     .L2
//.L3:
//add     QWORD PTR [rbp-8], 1
//.L2:
//mov     rax, QWORD PTR [rbp-24]
//lea     rdx, [rax+1]
//mov     QWORD PTR [rbp-24], rdx
//        movzx   eax, BYTE PTR [rax]
//test    al, al
//jne     .L3
//        mov     rax, QWORD PTR [rbp-8]
//pop     rbp
//ret
//        my_index:
//push    rbp
//mov     rbp, rsp
//sub     rsp, 32
//mov     QWORD PTR [rbp-24], rdi
//        mov     eax, esi
//        mov     BYTE PTR [rbp-28], al
//mov     QWORD PTR [rbp-8], 0
//jmp     .L6
//.L9:
//mov     rdx, QWORD PTR [rbp-24]
//mov     rax, QWORD PTR [rbp-8]
//add     rax, rdx
//movzx   eax, BYTE PTR [rax]
//cmp     BYTE PTR [rbp-28], al
//        jne     .L7
//        mov     rdx, QWORD PTR [rbp-24]
//mov     rax, QWORD PTR [rbp-8]
//add     rax, rdx
//jmp     .L8
//.L7:
//add     QWORD PTR [rbp-8], 1
//.L6:
//mov     rax, QWORD PTR [rbp-24]
//mov     rdi, rax
//call    my_strlen
//cmp     QWORD PTR [rbp-8], rax
//        jb      .L9
//        mov     eax, 0
//.L8:
//leave
//        ret

