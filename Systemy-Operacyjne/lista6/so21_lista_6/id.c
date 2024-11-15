#include "csapp.h"

static const char *uidname(uid_t uid) {
  /* TODO: Something is missing here! */
  // getpwuid -> zwraca wskaźnik na strukturę z pliku z hasłami
  // struct passwd {
  //     char   *pw_name;       /* username */
  //     char   *pw_passwd;     /* user password */
  //     uid_t   pw_uid;        /* user ID */
  //     gid_t   pw_gid;        /* group ID */
  //     char   *pw_gecos;      /* user information */
  //     char   *pw_dir;        /* home directory */
  //     char   *pw_shell;      /* shell program */
  // };

  struct passwd *pd;

  pd = getpwuid(uid);
  return pd->pw_name;

}

static const char *gidname(gid_t gid) {
  /* TODO: Something is missing here! */
  // getgrgid() zwraca wskaźnik na strukturę w pliku z bazą danych o grupach
  // struct group {
  //     char   *gr_name;        /* group name */
  //     char   *gr_passwd;      /* group password */
  //     gid_t   gr_gid;         /* group ID */
  //     char  **gr_mem;         /* NULL-terminated array of pointers
  //                               to names of group members */
  // };

  struct group *gd;
  gd = getgrgid(gid);

  return gd->gr_name;

}

static int getid(uid_t *uid_p, gid_t *gid_p, gid_t **gids_p) {
  gid_t *gids = NULL;
  int ngid = 2;
  int groups;

  /* TODO: Something is missing here! */
  *uid_p = getuid(); // zwraca ruid procesu
  *gid_p = getgid(); // zwraca rgid procesu

  gids = malloc(ngid * sizeof(gid_t));
  // int getgroups(int gidsetsize, gid_t grouplist[]);
  // wypełnia grouplist id grup do których należy, gidsetsize ustawia nam rozmiar tej tablicy
  groups = getgroups(0, NULL);

  gids = realloc(gids, groups * sizeof(gid_t));
  ngid = groups;

  groups = getgroups(ngid, gids);
  *gids_p = gids;
  return groups;
}

int main(void) {
  uid_t uid;
  gid_t *gids, gid;
  int groups = getid(&uid, &gid, &gids);

  printf("Liczba dodatkowych grup: %d\n", groups);
  printf("uid=%d(%s) gid=%d(%s) ", uid, uidname(uid), gid, gidname(gid));
  printf("groups=%d(%s)", gids[0], gidname(gids[0]));
  for (int i = 1; i < groups; i++)
    printf(",%d(%s)", gids[i], gidname(gids[i]));
  putchar('\n');

  free(gids);

  return 0;
}
