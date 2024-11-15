#include "csapp.h"

static noreturn void usage(int argc, char *argv[]) {
  fprintf(stderr, "Usage: %s [-t times] [-l length] -s "
          "[write|fwrite|fwrite-line|fwrite-full|writev]\n", argv[0]);
  exit(EXIT_FAILURE);
}

int main(int argc, char *argv[]) {
  int length = -1, times = -1;
  bool dosync = false;
  int opt;

  while ((opt = getopt(argc, argv, "l:t:s")) != -1) {
    if (opt == 'l')
      length = atoi(optarg);
    else if (opt == 't')
      times = atoi(optarg);
    else if (opt == 's')
      dosync = true;
    else 
      usage(argc, argv);
  }

  if (optind >= argc || length <= 0 || times <= 0)
    usage(argc, argv);

  char *choice = argv[optind];

  char *line = malloc(length + 1);
  memset(line, '*', length);
  line[length] = '\n';

  int res = 0;
  if (strcmp(choice, "write") == 0) {
    for (int j = 0; j < times; j++){
      for (int k = 0; k < length; k++){
        res = write(STDOUT_FILENO, line + k, length + 1 - k);
        if (res < 0){
          perror("error in simple write\n");
        }
      }
    }
  }

  if (strncmp(choice, "fwrite", 6) == 0) {
    size_t size;
    int mode;
    void *buf = NULL; 

    if (strcmp(choice, "fwrite-line") == 0) {
      mode = _IOLBF;
      size = length + 1;
    } else if (strcmp(choice, "fwrite-full") == 0) {
      mode = _IOFBF;
      size = getpagesize();
    } else {
      mode = _IONBF;
      size = 0;
    }

    /* TODO: Attach new buffer to stdout stream. */
    // dla NULL jako buf setvbuf tworzy nowy bufor
    int status = setvbuf(stdout, buf, mode, size);
    if (status < 0){
      perror("error attaching new buffer\n");
    }

    for (int j = 0; j < times; j++)
      for (int k = 0; k <= length; k++)
        fwrite(line + k, length + 1 - k, 1, stdout); 
    fflush(stdout);

    free(buf);
  }

  if (strcmp(choice, "writev") == 0) {
    int n = sysconf(_SC_IOV_MAX);
    struct iovec iov[n];
    /* TODO: Write file by filling in iov array and issuing writev. */
    // writev() zapisuje n struct'ów iov do pliku z podanym deskryptorem
    // struct iovec {
    //   void  *iov_base;    /* Starting address */
    //   size_t iov_len;     /* Number of bytes to transfer */
    // };
    for (int j = 0; j < times; j++) {
      for (int k = 0; k < length; k++){
        iov[(j*length + k) % n].iov_base = line + k;
        iov[(j*length + k) % n].iov_len = length + 1 - k;
        
        // jak doszliśmy do końca tablicy wypisujemy
        if ((j*length + k) % n == n - 1){
          ssize_t written = writev(STDOUT_FILENO, iov, n);
          if (written == -1) {
              perror("writev");
              exit(EXIT_FAILURE);
          }
        }

      }

      // jak nie doszliśmy do końca tablicy to sprzątamy bufor
      if ((times * length) % n){
        ssize_t written = writev(STDOUT_FILENO, iov, (times * length) % n);
          if (written == -1) {
              perror("writev");
              exit(EXIT_FAILURE);
          }
      }
        
    }

    
  }

  free(line);

  if (dosync && !isatty(STDOUT_FILENO))
    fsync(STDOUT_FILENO);

  return 0;
}
