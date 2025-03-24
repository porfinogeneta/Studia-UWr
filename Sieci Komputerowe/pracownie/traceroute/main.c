// Szymon Mazurek, 338191

#include "traceroute.h"
#include "network_utils.h"
#include "icmp_utils.h"
#include "error_handling.h"
#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[]){

    if (argc != 2) {
        printf("Usage: %s <destination_ip>\n", argv[0]);
        return 1;
    }

    if (!is_valid_ip(argv[1])) {
        ERROR("Error: Invalid IP address format");
        ERROR("Please provide a valid IPv4 address (e.g., 192.168.1.1)");
        return EXIT_FAILURE;
    }


    return run_traceroute(argv[1]);
}


