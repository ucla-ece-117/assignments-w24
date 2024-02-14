#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

void print_flag() {
    setuid(0);
    char flag[64];
    FILE *f = fopen("flag-2.txt", "r");
    if (f == NULL) {
        printf("Flag file is missing.\n");
        exit(1);
    }
    fgets(flag, sizeof(flag), f);
    printf("%s\n", flag);
    fclose(f);
}

void setup() {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

void game() {
    char name[64];

    printf("Welcome to the game!\n");
    printf("What's your name? ");
    gets(name);

    printf("Hello, %s! Let's play a game.\n", name);
}

int main() {
    setup();
    game();
    return 0;
}
