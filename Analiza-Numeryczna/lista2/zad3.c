#include <stdio.h>

void getbits(int j, int i){
    for (; j >= 0; j--){
        int bit = (i >> j) & 1;
        printf("%d", bit);
    }
    printf("$|");
}

int main() {
    for (int i = 16; i <= 31; i++) {
        printf("|$0.01");
        getbits(2, i);
        // 2^0
        printf("$0.");
        getbits(4, i);
        // 2^1
        printf("$1.");
        getbits(3, i);
        printf("\n");
    }
    return 0;
}
