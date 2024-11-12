#include <termios.h>
#include <sys/ioctl.h>

#include "terminal.h"

int tty_open(void) {
    const char *dev = ttyname(STDIN_FILENO);
    if (!dev) {
        errno = ENOTTY;
        unix_error("tty_open error");
    }
    return Open(dev, O_RDWR | O_NOCTTY, 0);
    }

// w dużym skrócie
// zapisujemy aktualny input do tymczasowej zmiennej
// do bufora wrzucamy raport o aktualnej pozycji kursora
// na podstawie raportu modyfikujemy x i y
// przywracamy stary input
void tty_curpos(int fd, int *x, int *y) {
    struct termios ts, ots; // struktura przechowująca konfigurację terminala

    // fd - deskryptor pliku terminala
    // ts - pointer na strukturę terminos
    tcgetattr(fd, &ts); // funkcja do pobierania atrybutów terminala
    memcpy(&ots, &ts, sizeof(struct termios)); // wrzucamy kopię terminos do drugiego wskaźnika
    ts.c_lflag &= ~(ECHO | ICANON | CREAD); // w kopii atrybutów terminala wyłączamy echo,wyłączamy tryb kanoniczny,wyłączamy możliwość dawania inputu
    tcsetattr(fd, TCSADRAIN, &ts); // ustawiamy nową konfigurację terminala, będzie ona miała efekt dopiero po wczytaniu całego obecnego outputu

    /* How many characters in the input queue. */
    int m = 0;
    /* TODO: Need to figure out some other way to do it on MacOS / FreeBSD. */
    #ifdef LINUX
    ioctl(fd, TIOCINQ, &m); // zczytujemy ile bajtów jest na inputcie
    #endif

    /* Read them all. */
    char discarded[m];
    m = Read(fd, discarded, m); // czytamy input do terminala

    Write(fd, CPR(), sizeof(CPR())); // zapisujemy raport pozycji kursora do pliku wskazywanego przez fd (na terminal)
    char buf[20];
    int n = Read(fd, buf, 19); // odczytujemy raport o kursorze i zapisujemy go na buforze
    buf[n] = '\0';

    ts.c_lflag |= ICANON; // przywracamy tryb kanoniczny
    tcsetattr(fd, TCSADRAIN, &ts); // ustawiamy nową konfugurację
    for (int i = 0; i < m; i++)
        ioctl(fd, TIOCSTI, discarded + i); // to co wcześniej wywaliliśmy z inputu przywracamy

    tcsetattr(fd, TCSADRAIN, &ots); // przywracamy konfigurację terminala sprzed całej funkcji
    sscanf(buf, "\033[%d;%dR", x, y); // zapisujemy pod wskaźniki x,y dane z raportu o kursorze
}