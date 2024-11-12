// #include "csapp.h"

// static void signal_handler(int signum, siginfo_t *info, void *data) {
//   if (signum == SIGINT) {
//     safe_printf("(%d) Screw you guys... I'm going home!\n", getpid());
//     _exit(0);
//   }
// }

<<<<<<< HEAD
static void play(pid_t next, const sigset_t *set) {
  for (;;) {
    printf("(%d) Waiting for a ball!\n", getpid());
    /* TODO: Something is missing here! */
    Sigsuspend(set);
    usleep((300 + random() % 400) * 1000);
    Kill(next, SIGUSR1);
    printf("(%d) Passing ball to (%d)!\n", getpid(), next);
  }
}
=======
// static void play(pid_t next, const sigset_t *set) {
//   for (;;) {
//     printf("(%d) Waiting for a ball!\n", getpid());
//     /* TODO: Something is missing here! */
//     usleep((300 + random() % 400) * 1000);
//     Kill(next, SIGUSR1);
//     printf("(%d) Passing ball to (%d)!\n", getpid(), next);
//   }
// }
>>>>>>> origin/main

// int main(int argc, char *argv[]) {
//   if (argc != 2)
//     app_error("Usage: %s [CHILDREN]", argv[0]);

//   int children = atoi(argv[1]);

//   if (children < 4 || children > 20)
//     app_error("Give number of children in range from 4 to 20!");

<<<<<<< HEAD
  /* Register signal handler for SIGUSR1 */
  struct sigaction action = {.sa_sigaction = signal_handler};
  Sigaction(SIGINT, &action, NULL);
  Sigaction(SIGUSR1, &action, NULL);
  
  pid_t pid, last = getpid();
  sigset_t cur,old;
  sigemptyset(&cur);
  sigaddset(&cur, SIGUSR1);
  Sigprocmask(SIG_BLOCK, &cur, &old);

  /* TODO: Start all processes and make them wait for the ball! */
  for (int i =0; i < children; i++){
    if ((pid = Fork()) == 0){
      play(last, &old);
    }else {
      last = pid;
    }

  }

  Kill(last, SIGUSR1);

  play(last, &old);

  return EXIT_SUCCESS;
}





















// #include "csapp.h"

// static void signal_handler(int signum, siginfo_t *info, void *data) {
//   if (signum == SIGINT) {
//     safe_printf("(%d) Screw you guys... I'm going home!\n", getpid());
//     _exit(0);
//   }
// }

// static void play(pid_t next, const sigset_t *set) {
//   for (;;) {
//     printf("(%d) Waiting for a ball!\n", getpid());
//     /* TODO: Something is missing here! */
//     Sigsuspend(set);
//     usleep((300 + random() % 400) * 1000);
//     Kill(next, SIGUSR1);
//     printf("(%d) Passing ball to (%d)!\n", getpid(), next);
//   }
// }

// int main(int argc, char *argv[]) {
//   if (argc != 2)
//     app_error("Usage: %s [CHILDREN]", argv[0]);

//   int children = atoi(argv[1]);

//   if (children < 4 || children > 20)
//     app_error("Give number of children in range from 4 to 20!");

//   /* Register signal handler for SIGUSR1 */
//   struct sigaction action = {.sa_sigaction = signal_handler};
//   Sigaction(SIGINT, &action, NULL);
//   Sigaction(SIGUSR1, &action, NULL);

//   pid_t pid, parent, last = getpid();
//   sigset_t cur,old;
//   sigemptyset(&cur);
//   sigaddset(&cur, SIGUSR1);
//   Sigprocmask(SIG_BLOCK, &cur, &old);

//   /* TODO: Start all processes and make them wait for the ball! */
//   if ((last = Fork()) == 0){
//     play(last, &old);
//     exit(0);
//   }

//   for (int i; i < children; i++){
//     if ((pid = Fork()) == 0){
//       play(last, &old);
//       exit(0);
//     }else {
//       last = pid;
//     }
//   }

//   Kill(last, SIGUSR1);
//   play(last,&old);

=======
//   /* Register signal handler for SIGUSR1 */
//   struct sigaction action = {.sa_sigaction = signal_handler};
//   Sigaction(SIGINT, &action, NULL);
//   Sigaction(SIGUSR1, &action, NULL);

//   /* TODO: Start all processes and make them wait for the ball! */

>>>>>>> origin/main
//   return EXIT_SUCCESS;
// }
