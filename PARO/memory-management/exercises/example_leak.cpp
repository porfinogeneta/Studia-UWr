#include <iostream>

int main(int ac, char* argv[])
{
    // error z testów
    // HEAP SUMMARY:
    //1: ==82494==     in use at exit: 4 bytes in 1 blocks
    //1: ==82494==   total heap usage: 3 allocs, 2 frees, 76,804 bytes allocated
    //1: ==82494==
    //1: ==82494== 4 bytes in 1 blocks are definitely lost in loss record 1 of 1
    //1: ==82494==    at 0x4849013: operator new(unsigned long) (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
    //1: ==82494==    by 0x109225: main (example_leak.cpp:5)
    //1: ==82494==
   // LEAK SUMMARY:
    //1: ==82494==    definitely lost: 4 bytes in 1 blocks
    //1: ==82494==    indirectly lost: 0 bytes in 0 blocks
    // odpowiedź testów po zmianie
    // HEAP SUMMARY:
    //1: ==82593==     in use at exit: 0 bytes in 0 blocks
    //1: ==82593==   total heap usage: 3 allocs, 3 frees, 76,804 bytes allocated
    //1: ==82593==
    //1: ==82593== All heap blocks were freed -- no leaks are possible

    int* leak = new int(14);

    std::cout << "[" << leak << "] => " << *leak << std::endl;
    delete leak;

    return 0;
}
