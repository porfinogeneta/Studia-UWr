/* See LICENSE file for copyright and license details. */
#include <sys/types.h>

#include <errno.h>
#include <grp.h>
#include <pwd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include "passwd.h"
#include "util.h"

extern char **environ;

static int lflag = 0;
static int pflag = 0;

static void
usage(void)
{
    eprintf("usage: %s [-lp] [username]\n", argv0);
}

int
main(int argc, char *argv[])
{
    // struktury danych
    char *usr, *pass;
    char *shell, *envshell, *term;
    struct passwd *pw;
    char *newargv[3];
    uid_t uid;

    // ustawiamy flagi w zależności od parametrów z argumentów
    ARGBEGIN {
        case 'l':
            lflag = 1;
            break;
        case 'p':
            pflag = 1;
            break;
        default:
            // w przypadku braku l albo p, printujemy error na stderr
            usage();
    } ARGEND;

    // jak jest więcej niż 1 argument po flagach
    if (argc > 1)
        usage();
    // jak nie podaliśmy użytkownika, to root jest naszym użytkownikiem
    usr = argc > 0 ? argv[0] : "root";

    errno = 0;
    // przeszukujemy /etc/passwd w poszukiwaniu usr, zwraca wskaźnik na struct z bazy danych
    pw = getpwnam(usr);
    if (!pw) {
        if (errno)
            eprintf("getpwnam: %s:", usr);
        else
            eprintf("who are you?\n");
    }

    // bierzemy ruid procesu wołającego
    uid = getuid();
    if (uid) {
        // pobieramy input z wyłączonym echo
        pass = getpass("Password: ");
        if (!pass)
            eprintf("getpass:");
        // sprawdzamy czy hasło się zgadza, jak nie, wychodzimy EXIT_FAILURE
        if (pw_check(pw, pass) <= 0)
            exit(1);
    }
    // czytamy grupy, do których należy nasz usr (przeglądanie pliku /etc/group) 
    if (initgroups(usr, pw->pw_gid) < 0)
        eprintf("initgroups:");
    // ustawiamy egid procesu wołającego na gid od znalezionego user'a
    if (setgid(pw->pw_gid) < 0)
        eprintf("setgid:");
    // ustawiamy euid procesu wołającego na uid od znalezionego user'a
    if (setuid(pw->pw_uid) < 0)
        eprintf("setuid:");

    // jak mamy jakąś powłokę dla tego użytkownika, to ją wykorzystujemy,
    // jak nie, korzystamy z /bin/sh
    shell = pw->pw_shell[0] == '\0' ? "/bin/sh" : pw->pw_shell;
    // logujemy się do danego user'a, w przypadku flagi l
    if (lflag) {
        term = getenv("TERM");
        // czyścimy zmienne środowiskowe, ustawiamy nowe
        clearenv();
        setenv("HOME", pw->pw_dir, 1);
        setenv("SHELL", shell, 1);
        setenv("USER", pw->pw_name, 1);
        setenv("LOGNAME", pw->pw_name, 1);
        setenv("TERM", term ? term : "linux", 1);
        // zmieniamy root procesu wołającego na root użytkownika
        if (chdir(pw->pw_dir) < 0)
            eprintf("chdir %s:", pw->pw_dir);
        // tworzymy argumenty dla nowego shell'a z flagą login
        newargv[0] = shell;
        newargv[1] = "-l";
        newargv[2] = NULL;
    } else {
        // jak mamy pflag to nie zmieniamy środowiska
        if (pflag) {
            envshell = getenv("SHELL");
            if (envshell && envshell[0] != '\0')
                shell = envshell;
        } else {
            // jak nie dostarczyliśmy żadnej flagi
            // zmieniamy zmienne, na dostarczone prze user'a dane
            setenv("HOME", pw->pw_dir, 1);
            setenv("SHELL", shell, 1);
            // jak nie jest root'em to zmieniamy jego nazwę
            if (strcmp(pw->pw_name, "root") != 0) {
                setenv("USER", pw->pw_name, 1);
                setenv("LOGNAME", pw->pw_name, 1);
            }
        }
        // tworzymy nowe argumenty dla shell'a
        newargv[0] = shell;
        newargv[1] = NULL;
    }
    // odpalmy nowego shell'a
    execve(shell, newargv, environ);
    weprintf("execve %s:", shell);
    return (errno == ENOENT) ? 127 : 126;
}