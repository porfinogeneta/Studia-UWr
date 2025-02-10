#include "csapp.h"

static __unused void outc(char c) {
  Write(STDOUT_FILENO, &c, 1);
}

#define N 3
#define M 6

static struct {
  /* TODO: Put semaphores and shared variables here. */
  sem_t pot_full;
  sem_t pot_empty;
  sem_t mutex;
  int soup;
  int cook_busy;
} *shared = NULL;


static void savage(void) {
  for (;;) {
    /* TODO Take a meal or wait for it to be prepared. */
    Sem_wait(&shared->mutex);
    if (shared->soup <= 0){
      outc('0');
      Sem_post(&shared->pot_empty);
      Sem_wait(&shared->pot_full);
    }
    outc('E');
    shared->soup--;

    Sem_post(&shared->mutex);
    /* Sleep and digest. */
    usleep(rand() % 1000 + 1000);

  }

  exit(EXIT_SUCCESS);
}

static void cook(void) {
  for (;;) {
    /* TODO Cook is asleep as long as there are meals.
     * If woken up they cook exactly M meals. */
    Sem_wait(&shared->pot_empty);
    shared->soup = M;
    outc('C'); 
    Sem_post(&shared->pot_full);
    
    

  }
}

/* Do not bother cleaning up after this process. Let's assume that controlling
 * terminal sends SIGINT to the process group on CTRL+C. */
int main(void) {
  shared = Mmap(NULL, getpagesize(), PROT_READ|PROT_WRITE, MAP_ANON|MAP_SHARED,
                -1, 0);

  /* TODO: Initialize semaphores and other shared state. */
  // 1 na drugim argumencie oznacza, że semafor jest na proces
  Sem_init(&shared->mutex, 1, 1);
  Sem_init(&shared->pot_empty, 1, 0);
  Sem_init(&shared->pot_full, 1, 0);
  shared->soup = M;

  for (int i = 0; i < N; i++)
    if (Fork() == 0)
      savage();

  cook();

  return EXIT_SUCCESS;
}
