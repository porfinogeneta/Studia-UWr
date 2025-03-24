// Szymon Mazurek, 338191

#include "error_handling.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>


// funkcja z wykładu
void ERROR(const char* str)
{
    fprintf(stderr, "%s\n", str);
    exit(EXIT_FAILURE);
}