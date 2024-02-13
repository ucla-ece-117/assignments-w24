#include <stdio.h>
#include <stdlib.h>

void setup() {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

void win() {
    system("/bin/sh");
}

void chall() {
    char leak[20];
    char buffer[20];
    puts("Leak? ");
    fgets(leak, 20, stdin);
    printf(leak);
    puts("Enter your name: ");
    fgets(buffer, 200, stdin);
    puts(buffer);
}

int main() {
    setup();
    chall();
    return 0;
}
