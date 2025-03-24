// Szymon Mazurek, 338191

#include "icmp_utils.h"
#include "error_handling.h"
#include <assert.h>
#include <stdio.h>
#include <arpa/inet.h>


// kod z wykładu
u_int16_t compute_icmp_checksum(const void *buff, int length)
{
    const u_int16_t* ptr = buff;
    u_int32_t sum = 0;
    assert (length % 2 == 0);
    for (; length > 0; length -= 2)
        sum += *ptr++;
    sum = (sum >> 16U) + (sum & 0xffffU);
    return (u_int16_t)(~(sum + (sum >> 16U)));
}

void print_as_bytes (unsigned char* buff, ssize_t length)
{
    for (ssize_t i = 0; i < length; i++, buff++)
        printf("%.2x ", *buff);
}

uint32_t create_composite_id(uint16_t sending_proc_pid, uint16_t iteration_id){
    // tworzenie id z dolnego bajtu PID i dolnego bajtu ttl
    uint32_t composite_id = ((uint32_t)sending_proc_pid) << 16;
    composite_id |= ((uint32_t)iteration_id & 0xFF);
    return composite_id;
}

uint16_t extract_process_id(uint32_t composite_id) {
    // dolne bity z pid przetrzymywane były na 16 wyższych bitach
    return (uint16_t)(composite_id >> 16);
}


uint16_t extract_packet_id(uint32_t composite_id) {
    // pobierz dolny bajt z id, czyli indeks iteracji ttl
    return (uint16_t)(composite_id & 0x00FF);
}


// zwraca 1, jak ip jest prawidłowe
int is_valid_ip(const char *ip_str) {
    struct sockaddr_in sa;
    int result;
    result = inet_pton(AF_INET, ip_str, &(sa.sin_addr));
    return result;
}


