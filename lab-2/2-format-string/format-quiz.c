#include <stdio.h>

void setup() {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

void chall() {
    int secret1 = 0x1337;
    long secret2 = 0xdeadbeef;
    char secret3[0x20] = "Hello, World!";

    char buffer[0x20];
    puts("Enter your answer: ");
    fgets(buffer, 0x20, stdin);
    printf(buffer);
}

int main() {
    setup();
    printf("Welcome to the format string quiz!\n");
    chall();
    return 0;
}