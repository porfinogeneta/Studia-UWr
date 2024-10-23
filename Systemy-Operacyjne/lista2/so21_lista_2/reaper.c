#include "csapp.h"

static pid_t spawn(void (*fn)(void)) {
  pid_t pid = Fork();
  if (pid == 0) {
    fn();
    printf("(%d) I'm done!\n", getpid());
    exit(EXIT_SUCCESS);
  }
  return pid;
}

static void grandchild(void) {
  printf("(%d) Waiting for signal!\n", getpid());
  /* TODO: Something is missing here! */
  printf("(%d) Got the signal!\n", getpid());
}

static void child(void) {
  pid_t pid;
  /* TODO: Spawn a child! */
  setpgid(0, 0);
  pid = spawn(grandchild);
  if (pid){
    setpgid(pid, getpid());
  }
  printf("(%d) Grandchild (%d) spawned!\n", getpid(), pid);
}

/* Runs command "ps -o pid,ppid,pgrp,stat,cmd" using execve(2). */
static void ps(void) {
  /* TODO: Something is missing here! */
  char *path = "/usr/bin/ps";
  char *argv[] = {"ps", "o", "pid,ppid,pgrp,stat,cmd"};
  execve(path, argv, NULL);
}

int main(void) {
  /* TODO: Make yourself a reaper. */
#ifdef LINUX
  Prctl(PR_SET_CHILD_SUBREAPER, 1);
#endif
  printf("(%d) I'm a reaper now!\n", getpid());

  pid_t pid, pgrp;
  int status;

  /* TODO: Start child and grandchild, then kill child!
   * Remember that you need to kill all subprocesses before quit. */
  // tworzymy dziecko
  pid = spawn(child);

  if (pid){
    Kill(pid, SIGKILL);
  }

  ps();



  return EXIT_SUCCESS;
}
