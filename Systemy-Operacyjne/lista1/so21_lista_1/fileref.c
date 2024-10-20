#include "csapp.h"
#include <unistd.h>
#include <stdio.h>

static char buf[256];

#define LINE1 49
#define LINE2 33
#define LINE3 78

static void do_read(int fd) {
  /* TODO: Spawn a child. Read from the file descriptor in both parent and
   * child. Check how file cursor value has changed in both processes. */
  
  printf("started reading %d\n", (int)getpid());
  off_t positionBefore, positionAfter;
  positionBefore = Lseek(fd, 0, SEEK_CUR); // ustawiamy kursor na początku

  printf("lseek position: %ld\n", positionBefore);

  // READ
  Read(fd, buf, LINE1);

  positionAfter = Lseek(fd, 0, SEEK_CUR);
  printf("lseek position: %ld\n", positionAfter);
  printf("%s\n", buf);
  exit(0);
}

static void do_close(int fd) {
  /* TODO: In the child close file descriptor, in the parent wait for child to
   * die and check if the file descriptor is still accessible. */
  printf("closing %d\n", (int)getpid());
  printf("fd: %d\n", fd);
  int val = close(fd);
  printf("result of closing: %d\n", val);
  exit(0);
}

int main(int argc, char **argv) {
  if (argc != 2)
    app_error("Usage: %s [read|close]", argv[0]);

  // ten int t deskryptor pliku, albo liczba ujemna w przypadku błędu
  int fd = Open("test.txt", O_RDONLY, 0);

  int status;
  pid_t rc_wait;

  int rc = Fork();


  // proces dziecko
  if (rc == 0) {
    if (!strcmp(argv[1], "read"))
      do_read(fd);
    if (!strcmp(argv[1], "close"))
      do_close(fd);
  }else  {
    // proces rodzic
    if (!strcmp(argv[1], "read"))
      do_read(fd);
    if (!strcmp(argv[1], "close")) {
      rc_wait = Waitpid(rc, &status, 0);
      printf("\nClose on parent side beginning:\n parent of: %d\n (rc_wait: %d) returned with status: %d\n", rc, rc_wait, status);
      do_close(fd);
    }
  }
  
  app_error("Unknown variant '%s'", argv[1]);
}
