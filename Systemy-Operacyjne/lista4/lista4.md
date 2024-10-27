![alt text](image.png)

^D -> EOF -> terminal na to reaguje

### Jak działa procedura *tty_curpos* odczytująca pozycję kursora terminala?
- plik z1.terminal.c

### Do czego służy kod sterujący CPR z *terminal.h*
```
#define CPR() CSI "6n"              /* Cursor Position Report */
```
Jest to Device Status Report i przesyła pozycję kursora w postaci
sekwencji:
```
ESC[n;mR] -> n - rząd, m - kolumna
echo -e "\033[6n"
```

### Semantyka TCGETS, TCSETSW, TIOCINQ, TIOCSTI
- TSGETS

uruchamiamy:
       int ioctl(int fd, TCGETS, struct termios *argp);

ekwiwalent *tcgetattr(fd, argp)* - pobranie aktualnych atrybutów terminala o deskryptorze plików fd

- TCSETSW

uruchamiamy:
       int ioctl(int fd, TCSETSW, const struct termios *argp);

ekwiwalent *tcsetattr(fd, TCSADRAIN, argp)* - zakończenie output'u, ustawienie nowych atrybutów terminala o deskryptorze plików fd

- TIOCINQ
       int ioctl(int fd, TIOCINQ, int *argp);
    
    podaj liczbę bajtów w buforze wejściowym

- TIOCSTI
       int ioctl(int fd, TIOCSTI, const char *argp);

    przywróć dany bufor na kolejkę wejściową

### Flagi ECHO, ICANON, CREAD - wpływ na sterownik terminala
- ECHO - umożliwia echo na terminal
- ICANON - kanonizacja linii wejściowych (czy terminal jest w trybie kanonicznym)
- CREAD - czy dajemy możliwość inputu do terminala

# zadanie 2
![alt text](image-1.png)