#include <stdio.h>

void setup() {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

void chall() {
    volatile int secret1 = 0x1337;
    volatile long secret2 = 0xdeadbeef;
    volatile char secret3[] = "Hello, World!\0";

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