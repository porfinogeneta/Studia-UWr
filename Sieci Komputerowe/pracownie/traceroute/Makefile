CC = gcc
CFLAGS = -Wall -Wextra -pedantic -std=c99
LDFLAGS =
OBJS = main.o traceroute.o network_utils.o icmp_utils.o error_handling.o

.PHONY: all clean

all: mytraceroute

mytraceroute: $(OBJS)
	$(CC) $(CFLAGS) -o $@ $(OBJS) $(LDFLAGS)

main.o: main.c traceroute.h network_utils.h error_handling.h
	$(CC) $(CFLAGS) -c $<

traceroute.o: traceroute.c traceroute.h network_utils.h icmp_utils.h error_handling.h
	$(CC) $(CFLAGS) -c $<

network_utils.o: network_utils.c network_utils.h icmp_utils.h error_handling.h
	$(CC) $(CFLAGS) -c $<

icmp_utils.o: icmp_utils.c icmp_utils.h
	$(CC) $(CFLAGS) -c $<

error_handling.o: error_handling.c error_handling.h
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f mytraceroute $(OBJS)