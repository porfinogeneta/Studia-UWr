#include "csapp.h"

static __unused void outc(char c) {
  Write(STDOUT_FILENO, &c, 1);
}

static void randsleep(void) {
  usleep(rand() % 5000 + 5000);
}

#define N 5

static pthread_t td[N];
static sem_t forks[N];
/* TODO: If you need extra shared state, define it here. */
static sem_t eating;

void *philosopher(void *id) {
  int right = (intptr_t)id;
  int left = right == 0 ? N - 1 : right - 1;

  for (;;) {
    /* Think */
    // outc('T');
    randsleep();

    /* TODO: Take forks (without deadlock & starvation) */
    // pobieram jeden zasób w filozofie
    Sem_wait(&eating);
    Sem_wait(&forks[right]);
    Sem_wait(&forks[left]);
    // outc('E');


    outc('0' + right);
    /* Eat */
    randsleep();

    /* TODO: Put forks (without deadlock & starvation) */
    Sem_post(&forks[left]);
    Sem_post(&forks[right]);
    // oddaję zasób
    Sem_post(&eating);

    // outc('P');
  
  }

  return NULL;
}

int main(void) {
  /* TODO: If you need extra shared state, initialize it here. */
  // aby pozbyć się głodzenia i deadlocka wyrzucę jednego filozofa
  /*
    1. nie wystąpi wówczas deadlock, bo nawet jak wszyscy na raz wezmą pałeczki, to przynjamniej 
    jeden weźmie dwie, i będzie się mógł wówczas skończyć
    2. nie wystąpi głodzenie, bo jak jakiś wątek się skończy, odda zasób, to ten do tej pory nieużywany będzie mógł
    coś zrobić
    3. praworęczność, czyli pobieranie zasobu w odpowiedniej kolejności już spełnione
    - widać że działa, bo w każdej grupie N filozofów w outputcie mamy wszystkie N liczb, więc żadnego filozofa nie głodzimy
  */

  // tworzę N-1 zasobów (counting semaphor)
  Sem_init(&eating, 0, N-1);

  for (int i = 0; i < N; i++)
    Sem_init(&forks[i], 0, 1);

  // uruchamiamy podaną funkcję w kolejnych wątkach
  for (int i = 0; i < N; i++)
    Pthread_create(&td[i], NULL, philosopher, (void *)(intptr_t)i);

  // sprzątamy wątki
  for (int i = 0; i < N; i++)
    Pthread_join(td[i], NULL);
  
  return EXIT_SUCCESS;
}
