#include "csapp.h"
#include <unistd.h>


// static sprawia, że funkcja może jedynie zostać zawołana z tego pliku,
// oprócz tego nie można wywoływać tej funkcji z innego pliku
// funkcja zwracająca pozycję danego hermana, generujemy dla każdej potencjalnej pozycji proces
static int ndselect(int n) {
  /* TODO: A loop is missing here that spawns processes and waits for them! */
  pid_t q_proccesses[n];

  for (int i = 0; i < n; i++){
      q_proccesses[i] = Fork();
      // w procesie dziecku zwróć zaproponowaną pozycję
      if (q_proccesses[i] == 0){
        // printf("ndselect, process PID %d\n", (int)getpid());
        return i; // przekazanie kontroli do funkcji wywołującej, nie jest wołany exit(0)
      } 
      else {
        // jak już wrócimy z tego procesu, to go od razu zabijamy,
        // robimy to po to, aby likwidować procesy po kolei, w ten sposób
        // nie będą się przeplatać, wtedy wszystko na spokojnie się wyprintuje, bo będziemy
        // czekać z zabiciem procesu drukującego
        Waitpid(q_proccesses[i], NULL, 0);
      }
    
    }

  // for (int i = 0; i < n; i++){
  //   Waitpid(q_proccesses[i], NULL, 0);
  // }

  exit(0);
}



static int conflict(int x1, int y1, int x2, int y2) {
  return x1 == x2
    || y1 == y2
    || x1 + y1 == x2 + y2
    || x1 - y1 == x2 - y2;
}

static void print_line_sep(int size) {
  for (int i = 0; i < size; ++i) 
    printf("+---");
  printf("+\n");
}

static void print_board(int size, int board[size]) {
  for (int i = 0; i < size; ++i) {
    print_line_sep(size);
    for (int j = 0; j < size; ++j)
      printf("|%s", board[i] == j ? " Q " : "   ");
    printf("|\n");
  }
  print_line_sep(size);
  printf("\n");
}

int main(int argc, char **argv) {
  if (argc != 2)
    app_error("Usage: %s [SIZE]", argv[0]);

  int size = atoi(argv[1]);

  if (size < 3 || size > 9)
    app_error("Give board size in range from 4 to 9!");

  int board[size];

  /* TODO: A loop is missing here that initializes recursive algorithm. */
  for (int i = 0; i <= size; i++){

    if (i == size){
      break;
    }

    int free_col = ndselect(size);

    if (free_col == -1){
      exit(0);
    }

    // printf("main, PID %d, placed in row: %d, column: %d\n", (int)getpid(), i, free_col);

    board[i] = free_col; // ustawiamy hetmana
    // sprawdzamy konflikty aż do obecnie ustawionego wiersza 
    for (int j = 0; j < i; j++){
      if (conflict(i, board[i], j, board[j])){
        exit(0);
      }
    }

  }

  
  printf("PID: %d\n", (int)getpid());
  print_board(size, board);

  return 0;
}
