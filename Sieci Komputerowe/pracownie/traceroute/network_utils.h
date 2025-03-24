// Szymon Mazurek, 338191

#include <sys/time.h>
#include <stdint.h>
#include <sys/types.h>

struct timeval send_packet(int socket, char ip[], int iter_id, uint16_t lower_pid_bits);

int receive_packet(int socket_fd, uint32_t current_id, 
    struct timeval receive_times[], char received_ip_table[][20]);

int is_valid_ip(const char *ip_str);