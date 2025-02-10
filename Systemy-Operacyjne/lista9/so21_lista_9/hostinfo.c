#include "csapp.h"

#define DEFAULT_PORT "http"

int main(int argc, char **argv) {
  struct addrinfo *p, *listp, hints;
  char buf[MAXLINE];
  char serv[NI_MAXSERV];// bufor na usługi
  int rc, flags;
  char *port; // port, z którego info zbierzemy

  if (argc < 2 || argc > 3)
    app_error("usage: %s <domain name> [port number]\n", argv[0]);

  if (argc == 3){
    port = argv[2];
  }else {
    port = DEFAULT_PORT;
  }

  /* Get a list of addrinfo records */
  memset(&hints, 0, sizeof(struct addrinfo));
  hints.ai_family = AF_UNSPEC; /* AF_INET - IPv4 only,liwiamy oba protokoły AF_UNSPEC IPv4 igb IPv6 */
  hints.ai_socktype = SOCK_STREAM;
  /* Connections only */
  if ((rc = getaddrinfo(argv[1], port, &hints, &listp)) != 0)
    gai_error(rc, "getaddrinfo");

  /* Walk the list and display each IP address */
  // dodaliśmy NI_NUMERICSERV, żeby usługa wyświetlała się w postaci numerycznej
  flags = NI_NUMERICHOST | NI_NUMERICSERV; /* Display address string instead of domain name */
  for (p = listp; p; p = p->ai_next) {
    Getnameinfo(p->ai_addr, p->ai_addrlen, buf, MAXLINE, serv, sizeof(serv), flags);
    if (p->ai_family == AF_INET6) { // IPv6
      printf("[%s]:%s\n", buf, serv);
    } else { // IPv4
      printf("%s:%s\n", buf, serv);
    }
  }

  /* Clean up */
  freeaddrinfo(listp);

  return EXIT_SUCCESS;
}
