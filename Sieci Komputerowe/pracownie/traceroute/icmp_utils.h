// Szymon Mazurek, 338191


#include <netinet/ip.h>
#include <netinet/ip_icmp.h>
#include <sys/types.h>
#include <stdint.h>


u_int16_t compute_icmp_checksum(const void *buff, int length);

void print_as_bytes(unsigned char* buff, ssize_t length);

uint32_t create_composite_id(uint16_t sending_proc_pid, uint16_t iteration_id);

uint16_t extract_process_id(uint32_t composite_id);

uint16_t extract_packet_id(uint32_t composite_id);

int is_valid_ip(const char *ip_str);