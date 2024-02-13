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
    char buffer[20];
    puts("Enter your name: ");
    fgets(buffer, 200, stdin);
    puts(buffer);
}

int main() {
    setup();
    chall();
    return 0;
}
