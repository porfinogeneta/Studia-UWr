#include "csapp.h"

#define DIRBUFSZ 256

static void print_mode(mode_t m) {
  char t;

  if (S_ISDIR(m))
    t = 'd';
  else if (S_ISCHR(m))
    t = 'c';
  else if (S_ISBLK(m))
    t = 'b';
  else if (S_ISREG(m))
    t = '-';
  else if (S_ISFIFO(m))
    t = 'f';
  else if (S_ISLNK(m))
    t = 'l';
  else if (S_ISSOCK(m))
    t = 's';
  else
    t = '?';

  char ur = (m & S_IRUSR) ? 'r' : '-';
  char uw = (m & S_IWUSR) ? 'w' : '-';
  char ux = (m & S_IXUSR) ? 'x' : '-';
  char gr = (m & S_IRGRP) ? 'r' : '-';
  char gw = (m & S_IWGRP) ? 'w' : '-';
  char gx = (m & S_IXGRP) ? 'x' : '-';
  char or = (m & S_IROTH) ? 'r' : '-';
  char ow = (m & S_IWOTH) ? 'w' : '-';
  char ox = (m & S_IXOTH) ? 'x' : '-';

  /* TODO: Fix code to report set-uid/set-gid/sticky bit as 'ls' does. */
  // user = owner
  // group - przywileje dla użytkowników w grupie pliku
  // others
  if (m & S_IRUSR){
    // ustawiamy s jeśli ten user to owner i jeśli plik jest mamy możliwość wykonania,
    // S jak owner, ale bez możliwości wykonania
    ux = (m & S_IXUSR) ? 's' : 'S';
  }
  if (m & S_ISGID) {
    gx = (m & S_IXGRP) ? 's' : 'S';
  }
  if (m & __S_ISVTX) {
    ox = (m & S_IXGRP) ? 't' : 'T';
  }
  printf("%c%c%c%c%c%c%c%c%c%c", t, ur, uw, ux, gr, gw, gx, or, ow, ox);
}

static void print_uid(uid_t uid) {
  struct passwd *pw = getpwuid(uid);
  if (pw)
    printf(" %10s", pw->pw_name);
  else
    printf(" %10d", uid);
}

static void print_gid(gid_t gid) {
  struct group *gr = getgrgid(gid);
  if (gr)
    printf(" %10s", gr->gr_name);
  else
    printf(" %10d", gid);
}

static void file_info(int dirfd, const char *name) {
  struct stat sb[1];

  /* TODO: Read file metadata. */
  // nie chcemy robić dereferencji symlinków
  Fstatat(dirfd, name, sb, AT_SYMLINK_NOFOLLOW);
  print_mode(sb->st_mode);
  printf("%4ld", sb->st_nlink);
  print_uid(sb->st_uid);
  print_gid(sb->st_gid);

  /* TODO: For devices: print major/minor pair; for other files: size. */
  mode_t m = sb->st_mode;
  if (S_ISBLK(m) || S_ISCHR(m)){
    printf(" %3d %3d", major(sb->st_dev), minor(sb->st_dev));
  }else {
    printf(" %9ld", sb->st_size);
  }

  char *now = ctime(&sb->st_mtime);
  now[strlen(now) - 1] = '\0';
  printf("%26s", now);

  printf("  %s", name);

  if (S_ISLNK(sb->st_mode)) {
  /* TODO: Read where symlink points to and print '-> destination' string. */
    char buf[PATH_MAX];
    ssize_t len;
    len = readlinkat(dirfd, name, buf, sizeof(buf) - 1);
    buf[len] = '\0';
    printf(" -> %s", buf);
  }

  putchar('\n');
}

int main(int argc, char *argv[]) {
  if (!argv[1])
    argv[1] = ".";

  int dirfd = Open(argv[1], O_RDONLY | O_DIRECTORY, 0);
  char buf[DIRBUFSZ];
  int n;

  // jak Getdents się uda zwraca liczbę bajtów
  while ((n = Getdents(dirfd, (void *)buf, DIRBUFSZ))) {
    struct linux_dirent *d;
    d = (struct linux_dirent *)buf;
    for (int i = 0; i < n; i += d->d_reclen){
      d = (struct linux_dirent *)(buf + i);
      file_info(dirfd, d->d_name);
    }
    /* TODO: Iterate over directory entries and call file_info on them. */
    // struct linux_dirent {
    //            unsigned long  d_ino;     /* Inode number */
    //            unsigned long  d_off;     /* Not an offset; see below */
    //            unsigned short d_reclen;  /* Length of this linux_dirent */
    //            char           d_name[];  /* Filename (null-terminated) */
    //                              /* length is actually (d_reclen - 2 -
    //                                 offsetof(struct linux_dirent, d_name)) */
    //            /*
    //            char           pad;       // Zero padding byte
    //            char           d_type;    // File type (only since Linux
    //                                      // 2.6.4); offset is (d_reclen - 1)
    //            */
    //        }
  }

  Close(dirfd);
  return EXIT_SUCCESS;
}
