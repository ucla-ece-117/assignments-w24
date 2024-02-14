#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

void print_flag() {
    setuid(0);
    char flag[64];
    FILE *f = fopen("flag-3.txt", "r");
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
    char name[20];
    char message[64];

    printf("Welcome to the game!\n");
    printf("What's your name? ");
    fgets(name, sizeof(name), stdin);

    printf("Hello, ");
    printf(name);
    printf("! Let's play a game.\n");

    printf("What's your message? ");
    fgets(message, 100, stdin);

    printf("Your message is ");
    puts(message);
}

int main() {
    setup();
    game();
    return 0;
}
