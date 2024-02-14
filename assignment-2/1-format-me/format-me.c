#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

void print_flag() {
    setuid(0);
    char flag[64];
    FILE *f = fopen("flag-1.txt", "r");
    if (f == NULL) {
        printf("Flag file is missing.");
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

  srand(time(NULL));
}

long lrand() {
  long higher, lower;
  higher = (((long)rand()) << 32);
  lower = (long)rand();
  return higher + lower;
}

void game() {
    char buffer[64] = {0};
    long code, guess = 0;
    int correct = 0;

    while(correct < 10) {
        code = lrand();

        printf("Recipient? ");
        fgets(buffer, sizeof(buffer), stdin);
        printf("Sending to ");
        printf(buffer);
        printf("...\n");

        printf("Guess? ");
        scanf("%lu", &guess);
        if (guess == code) {
            printf("Correct code! Package sent.\n");
            getchar();
            correct++;
        } else {
            printf("Incorrect code. The correct code was %lu. Guess you have to start again.\n", code);
            return;
        }
    }

    printf("You've sent 10 packages. Here's your flag: ");
    print_flag();
}

int main() {
    printf("Welcome to the package sending service!\n");
    setup();
    game();
    return 0;
}
