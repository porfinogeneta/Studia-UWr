#include "csapp.h"

static __thread unsigned seed;

static void rand_usleep(int min, int max) {
  usleep(rand_r(&seed) % (max - min + 1) + min);
}

#define DEBUG
#ifdef DEBUG
static __unused void outc(char c) {
  Write(STDOUT_FILENO, &c, 1);
}

/* XXX Please use following function to simulate malicious scheduler.
 * Just insert a call to rand_yield between instructions in your solution. */
static __unused void rand_yield(void) {
  /* Once every 100 calls to this function (on average)
   * it yields and lets kernel choose another thread. */
  if (rand_r(&seed) % 100 == 42)
    sched_yield();
}
#else
#define outc(c)
#define rand_yield()
#endif

typedef struct ramen {
  /* TODO: Put internal state & mutexes & condvars here. */
  pthread_mutex_t mutex;
  // pthread_cond_t currently_eating;
  pthread_cond_t want_to_eat;
  int seats;
  int eating;
} ramen_t;

static void ramen_init(ramen_t *r, unsigned seats) {
  /* TODO: Initialize internal state of ramen restaurant. */
  Pthread_mutex_init(&r->mutex, 0);
  // Pthread_cond_init(&r->currently_eating, 0);
  Pthread_cond_init(&r->want_to_eat, 0);
  r->seats = seats;
  r->eating = 0;
}

static void ramen_destroy(ramen_t *r) {
  /* TODO: Destroy all synchronization primitives. */
  // Pthread_cond_destroy(&r->currently_eating);
  Pthread_cond_destroy(&r->want_to_eat);
  Pthread_mutex_destroy(&r->mutex);
}

static void ramen_wait(ramen_t *r) {
  /* TODO: Enter the restaurant unless it's full or people haven't left yet. */
  Pthread_mutex_lock(&r->mutex);
  // r-eating, occupied
  while (r->seats == 0){
    // czekamy na wybudzenie want_to_eat
    Pthread_cond_wait(&r->want_to_eat, &r->mutex);
  }
  r->seats--;
  r->eating++;
  Pthread_mutex_unlock(&r->mutex);
}

static void ramen_finish(ramen_t *r) {
  /* TODO: Finished eating, so wait for all other to finish before leaving. */
  Pthread_mutex_lock(&r->mutex);
  r->eating--;
  if (r->eating == 0){
    // wait _for_others
    // occupied == seats, eating < occupied
    Pthread_cond_broadcast(&r->want_to_eat);
  }
  r->seats++;
  Pthread_mutex_unlock(&r->mutex);
}

void *customer(void *data) {
  ramen_t *r = data;

  seed = (unsigned)pthread_self();

  while (true) {
    /* Wait till you get hungry. */
    rand_usleep(5000, 10000);

    /* Queue for delicious ramen. */
    outc('.');
    ramen_wait(r);

    /* It's so yummy! */
    outc('@');
    rand_usleep(1000, 2000);

    /* Time to leave, but don't be rude or else... */
    ramen_finish(r);
    outc('_');
  }
}

#define THREADS 10
#define SEATS 5

int main(void) {
  ramen_t r;
  ramen_init(&r, SEATS);

  pthread_t tid[THREADS];

  for (int i = 0; i < THREADS; i++)
    Pthread_create(&tid[i], NULL, customer, &r);

  for (int i = 0; i < THREADS; i++)
    Pthread_join(tid[i], NULL);

  ramen_destroy(&r);
  return 0;
}