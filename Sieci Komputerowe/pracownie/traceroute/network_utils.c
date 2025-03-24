// Szymon Mazurek, 338191

#include "network_utils.h"
#include "icmp_utils.h"
#include "error_handling.h"

#include <netinet/ip.h>
#include <netinet/ip_icmp.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <poll.h>


struct timeval send_packet(int socket, char ip[], int iter_id, uint16_t lower_pid_bits){

    // zapisanie kiedy pakiet został wysłany
    struct timeval sending_time;
    if (gettimeofday(&sending_time, NULL) < 0) {
        ERROR("gettimeofday error");
    }

    // nagłówek icmp
    struct icmphdr header;
    memset(&header, 0, sizeof(header));
    header.type = ICMP_ECHO;
    header.code = 0;
    header.un.echo.id = lower_pid_bits;
    header.un.echo.sequence = iter_id;
    header.checksum = compute_icmp_checksum ((u_int16_t*)&header, sizeof(header));

    // odbiorca pakietu
    struct sockaddr_in recipient;
    memset (&recipient, 0, sizeof(recipient));
    recipient.sin_family = AF_INET;
    
    if (inet_pton(AF_INET, ip, &recipient.sin_addr) <= 0) {
        ERROR("inet_pton failed for destination IP");
    }

    

    // wysłanie pakietu
    ssize_t bytes_sent = sendto (
        socket,
        &header,
        sizeof(header),
        0,
        (struct sockaddr*)&recipient,
        sizeof(recipient)
    );

    if (bytes_sent < 0) {
        ERROR("sendto failed");
    } else if ((unsigned long)bytes_sent < sizeof(header)) {
        fprintf(stderr, "Partial packet sent (%zd bytes out of %zu)\n", bytes_sent, sizeof(header));
    }

    return sending_time;
}


// funkcja obiera wszystie pakiety w określonym czasie (1000ms)
int receive_packet(int socket_fd, uint32_t current_id, struct timeval receive_times[], char received_ip_table[][20]){
    
    // timestamp, pilnujący początku i pomagający obliczyć ile czasu minęło od wywołania funkcji
    struct timeval start_time, receiving_time;
    if (gettimeofday(&start_time, NULL) < 0) {
        ERROR("gettimeofday error");
    }

    int packets_received = 0;
    int amount_of_unique_packets = 0;
    double elapsed_ms = 0;
    while (packets_received < 3 && elapsed_ms < 1000.0){
        
        struct pollfd ps;
        ps.fd = socket_fd;
        ps.events = POLLIN;
        ps.revents = 0;
        // czekamy na zapis na socket, dopóki mamy 'budżet'
        int ready = poll(&ps, 1, 1000.0 - elapsed_ms);

        if (ready < 0) {
            if (errno == EINTR) {
                fprintf(stderr, "Poll interrupted by signal, continuing...\n");
                continue;
            } else {
                ERROR("poll failed");
            }
        }
        
        if (gettimeofday(&receiving_time, NULL) < 0) {
            ERROR("gettimeofday error");
        }

        elapsed_ms = (receiving_time.tv_sec - start_time.tv_sec) * 1000.0;
        elapsed_ms += (receiving_time.tv_usec - start_time.tv_usec) / 1000.0;
        receive_times[packets_received] = receiving_time;

        if (elapsed_ms >= 1000.0){
            break;
        }

        // jak udało się coś przeczytać
        if (ready > 0 && (ps.revents & POLLIN)){

            // właściwy odbiór pakietów
            struct sockaddr_in sender;
            socklen_t sender_len = sizeof(sender);
            u_int8_t buffer[IP_MAXPACKET];

            // odczyt z socekt'a
            ssize_t packet_len = recvfrom(socket_fd, buffer, IP_MAXPACKET, 0, (struct sockaddr*)&sender, &sender_len);
            
            if (packet_len < 0) {
                if (errno == EINTR) {
                    fprintf(stderr, "recvfrom interrupted by signal, continuing...\n");
                    continue;
                } else {
                    ERROR("recvfrom error");
                }
            }

            char sender_ip_str[20] = {0};
            if (inet_ntop(AF_INET, &(sender.sin_addr), sender_ip_str, sizeof(sender_ip_str)) == NULL) {
                ERROR("inet_ntop failed to convert sender IP");
            }
            

            struct iphdr* ip_header = (struct iphdr*) buffer;
            u_int8_t* icmp_packet = buffer + 4 * ip_header->ihl;

            struct icmphdr* icmp_header = (struct icmphdr*)icmp_packet;

            uint16_t proc_id;
            uint16_t iter_id; 

            if (icmp_header->type == ICMP_ECHOREPLY) {
                proc_id = icmp_header->un.echo.id;
                iter_id = icmp_header->un.echo.sequence;

            } else if (icmp_header->type == ICMP_TIME_EXCEEDED) {
                // orygnialny ip jest 8 bajtów dalej
                struct iphdr* orig_ip = (struct iphdr*)(icmp_packet + 8);
                // z oryginalnego ip można odczytać standardowo icmp
                u_int8_t* orig_icmp = (u_int8_t*)orig_ip + 4 * orig_ip->ihl;
                struct icmphdr* orig_icmp_header = (struct icmphdr*)orig_icmp;
                
                proc_id = orig_icmp_header->un.echo.id;;
                iter_id = orig_icmp_header->un.echo.sequence;
            }

            // sprawdzamy czy to jest pakiet z dobrej tury
            if (current_id == create_composite_id(proc_id, iter_id)){
        
                // czy taki pakiet już był odebrany, jeśli nie dodajemy do tablicy
                int ip_already_added = 0;
                packets_received++;

                for (int p = 0; p < amount_of_unique_packets; p++){
                    if (strcmp(sender_ip_str, received_ip_table[p]) == 0){
                        ip_already_added = 1;
                        break;
                    }
                }
                if (!ip_already_added){
                    strcpy(received_ip_table[amount_of_unique_packets], sender_ip_str);
                    amount_of_unique_packets++;
                }
                
            }

            
        }

    }   

    return packets_received;
}
