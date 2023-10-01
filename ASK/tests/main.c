#include <stdio.h>
#include <stdint-gcc.h>

uint64_t swap(uint64_t x){
    x = (x >> 32) | (x << 32);
    x = ((x & 0xffff0000ffff0000) >> 16) | ((x & 0x0000ffff0000ffff) << 16);
    x = ((x & 0xff00ff00ff00ff00) >> 8)  | ((x & 0x00ff00ff00ff00ff) << 8);
    x = ((x & 0xf0f0f0f0f0f0f0f0) >> 4)  | ((x & 0x0f0f0f0f0f0f0f0f) << 4);
    x = ((x & 0xcccccccccccccccc) >> 2)  | ((x & 0x3333333333333333) << 2);
    x = ((x & 0xaaaaaaaaaaaaaaaa) >> 1)  | ((x & 0x5555555555555555) << 1);
    return x;
}


// value-range 0 to 2016 fits in a 16-bit integer, so masking wider than that can be deferred
//inline
unsigned weighted_sum(uint64_t n)
{
    // 0101 0101 0101 0101 0101...
    // 0b11001010
    uint64_t ones = (n >> 1) & 0x5555555555555555;   // 0xaa>>1
    uint64_t pairs = n - ones;  // standard popcount within pairs, not weighted

    uint64_t weighted_pairs = ((ones + (ones>>2)) & 0x3333333333333333)
                              + ((pairs >> 2) & 0x3333333333333333) * 2;   // 0..6 range within 4-bit nibbles
    // aka  (pairs>>1) & (0x3333333333333333<<1).  But x86-64 can efficiently use LEA to shift-and-add in one insn so it's better to shift to match the same mask.
    uint64_t quads = (pairs & 0x3333333333333333) + ((pairs >> 2) & 0x3333333333333333);   // standard popcount within each nibble, 0..4

    // reduce weighted pairs (0xaa and 0xcc masks) and add __popcnt64(n & 0xF0F0F0F0F0F0F0F0) << 2)
    // resulting in 8 buckets of weighted sums, each a byte wide
    uint64_t weighted_quads = ((weighted_pairs + (weighted_pairs >> 4)) & 0x0F0F0F0F0F0F0F0F)
                              + (4*((quads >> 4) & 0x0F0F0F0F0F0F0F0F));  // 0 to 2*6 + 4*4 = 28 value-range
    // need some masking before adding.  4*quads can be up to 16 so can't use (quads >> (4-2)) & 0x0F0F0F0F0F0F0F0F
    uint64_t octs = (quads + (quads >> 4)) & 0x0F0F0F0F0F0F0F0F;  //  0..8   quad fields don't have their high bit set, so we can defer masking until after adding without overflow into next field

    // two separate sums of 8-bit groups, one of the first 3 weights
    unsigned sum_weighted_quads = (weighted_quads * 0x0101010101010101uLL)>>(64-8); // barely fits in 1 byte: max val 28 * 8 = 224
    // the second applying the last 3 relative weights to the flat sums
    unsigned sum_octweights = (octs * 0x0001020304050607uLL) >> (64-8);  // separate weight for each byte group, with <<3 factored out so the max sum is also 224 = 32*(1<<0 + 1<<1 + 1<<2)
    return sum_weighted_quads + 8 * sum_octweights; // apply the <<3 factored out of byte weights
}

void print_binary(uint64_t number) {
    for (int i = sizeof(number) * 8 - 1; i >= 0; i--) {
        putchar('0' + ((number >> i) & 1));
    }
    printf("\n");
}

uint64_t addsb_iter(uint64_t x, uint64_t y){
    uint64_t xsigns = x & 0x8080808080808080; //bierzemy znaki poszczególnych bajtów
    uint64_t ysigns = y & 0x8080808080808080; // znowu znaki naszych liczb
    uint64_t sum = (x^xsigns) + (y^ysigns); //dodajemy liczby ale bez bitów znaku w każdym bajcie
    sum ^= xsigns ^ ysigns; // dbamy o właściwy znak naszej wyliczonej sumy
    uint64_t sumsigns = sum & 0x8080808080808080; // bierzemy znak naszej sumy
    // saturacja w górę, jeśli a i b były dodatnie, ale rezultat jest ujemny
    // to ~(xsigns|ysigns) obliczy się do 1 jeśli sumsigns także jest 1, sat będzie miał wtedy maski równe 1, wpp bedzie 0 i nic to nie zmieni
    uint64_t sat = sumsigns & ~(xsigns|ysigns);
    // mając odpowiednie nasycenie chcemy ograniczyć wynik do 127
    // przesuwamy o 7 w prawo, wtedy w każdej grupie 8 bitów będziemy mieli, jak był overflow zapalony bit
    // mnożymy przez 127, żeby w każdym bajcie gdzie był overflow znalazło się 127
    // or nam po prostu zapisze wynik tej saturacji w sum
    sum |= (sat>>7)*127; // tam gdzie były overflowy, tam się teraz znajdą same 1 (grupach 1 bajtowych) (przesunięci logiczne na liczbie bez znaku)
    sum &= ~sat; // sat zawiera teraz 1 tylko w przypadku, gdy nie było w danym miejscu overflowa, zapisujemy nasz wynik na sumie
    // mamy jeszcze drugą opcję tj. gdy dodawane liczby były ujemne a wynik był dodatni, overflow dla ujemnych
    sat = (xsigns&ysigns) & ~sumsigns; //obie x i y miały ujemne zapalone, natomiast suma miała zgaszone, dostajemy 1 miejsca underflow'ów
    sum &= ~((sat>>7)*127); //wszędzie gdzie były underflowy są teraz zera
    sum |= sat;
    return sum;


}


uint64_t add(uint64_t a, uint64_t b) {
    uint64_t asigns = a & 0x8080808080808080;
    uint64_t bsigns = b & 0x8080808080808080;
    uint64_t sum = (a^asigns) + (b^bsigns);
    // fix up 8 bit wrapped sums
    sum ^= asigns ^ bsigns;
    uint64_t sumsigns = sum & 0x8080808080808080;
    // we saturate high when a and b were positive, but the result is negative
    uint64_t sat = sumsigns & ~(asigns|bsigns);
    sum |= (sat>>7)*127;
    sum &= ~sat;
    // we saturate negative when a and b were negative, but the result is positive
    sat = (asigns&bsigns) & ~sumsigns;
    sum &= ~((sat>>7)*127);
    sum |= sat;
    return sum;
}



int main() {
//    print_binary(0x0102040810204080);
//    uint64_t r = swap(0x0102040810204080);
//    print_binary(r);
//    print_binary(0x0102040810204080);
//    printf("%lu \n", addsb_iter(-60, -80));
    uint32_t test_number = 0b11001010;
    uint32_t result = weighted_sum(test_number);
    printf("The weighted bit sum of %u is %u\n", test_number, result);
    return 0;
}
