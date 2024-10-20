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

// ps -jH

static void grandchild(void) {
  printf("(%d) Waiting for signal!\n Group (%d)", getpid(), getpgrp());
  /* TODO: Something is missing here! */
  pause();
  printf("(%d) Got the signal!\n", getpid());
}

static void child(void) {
  pid_t pid;
  /* TODO: Spawn a child! */
  Setpgid(getpid(), getpid());
  pid = spawn(grandchild);
  printf("(%d) Grandchild (%d) spawned!\n", getpid(), pid);
}

/* Runs command "ps -o pid,ppid,pgrp,stat,cmd" using execve(2). */
static void ps(void) {
  /* TODO: Something is missing here! */
  char *const args[] = {"/bin/ps", "-o", "pid,ppid,pgrp,stat,cmd", NULL};
  execv(args[0], args);
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
  
  // spawning a child
  pgrp = spawn(child);
  Waitpid(pgrp, NULL, 0);
    
 
  pid = spawn(ps);
  Waitpid(pid, NULL, 0);

  // Kill(-pgrp, SIGKILL);

  printf("(%d) SIGINT sent to every process from group: %d\n", getpid(), pgrp);
  // wait for every other process
  Waitpid(-1, &status, 0);
  printf("(%d) Grandchild exit status is: %d\n", getpid(), WEXITSTATUS(status));
  

  return EXIT_SUCCESS;
}
