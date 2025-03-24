// Szymon Mazurek, 338191

#include "traceroute.h"
#include "network_utils.h"
#include "icmp_utils.h"
#include "error_handling.h"

#include <netinet/ip.h>
#include <netinet/ip_icmp.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int run_traceroute(const char *desination_ip){

    int socket_fd = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
    if (socket_fd < 0)
        ERROR("socket error");



    // ustalenie konkretnego ttl
    for (int ttl = 1; ttl <= 30; ttl++){
        if (setsockopt(socket_fd, IPPROTO_IP, IP_TTL, &ttl, sizeof(int)) < 0) {
            ERROR("setsockopt failed to set TTL");
        }

        uint16_t iter_id = ttl;
        uint16_t lower_sending_proc_pid = getpid() & 0xFF;
        uint32_t packet_sent_id = create_composite_id(lower_sending_proc_pid, iter_id);
        
        
        struct timeval sending_times[3];
                

        // WYSYŁANIE PAKIETÓW
        for (int i = 0; i < 3; i++){
            sending_times[i] = send_packet(socket_fd, (char *)desination_ip, iter_id, lower_sending_proc_pid);
        }

        
        
        // ODBIERANIE PAKIETÓW
        char ip_used_table[3][20] = {0};
        memset(ip_used_table, 0, sizeof(ip_used_table));
        int num_received_packages = 0;
        struct timeval receive_times[3];

        num_received_packages = receive_packet(socket_fd, packet_sent_id, receive_times, ip_used_table);
        

        // DRUKOWANIE WYJŚCIA
        // pakiety
        printf("%d. ", ttl);
        if (num_received_packages == 0){
            printf("*");
        }else {
            for (int i = 0; i < 3; i++){
                if (strlen(ip_used_table[i]) > 0)
                    printf("%s ", ip_used_table[i]);
            }
        }
        // czasy pakietów
        if (num_received_packages == 3) {
            double avg = 0;
            for (int t = 0; t < 3; t++){
                double help;
                
                help = (receive_times[t].tv_sec - sending_times[t].tv_sec) * 1000.0;
                help += (receive_times[t].tv_usec - sending_times[t].tv_usec) / 1000.0;
                
                avg += help;
            }
            printf(" %.3f ms", avg / 3.0);

        } else {
            if (num_received_packages > 0)
                printf("???");
        }

        printf("\n");

        // koniec odczytu, jak doszło do końca
        for (int k = 0; k < 3; k++){
            if (strcmp(ip_used_table[k], desination_ip) == 0){
                if (close(socket_fd) < 0) {
                    ERROR("close socket failed");
                }
                return 0;
            }
        }
        
    }
    
    

    if (close(socket_fd) < 0) {
        ERROR("close socket failed");
    }
    
    return 0;

}