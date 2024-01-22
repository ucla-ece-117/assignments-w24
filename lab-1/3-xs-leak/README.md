# Part 3: XS-Leak

```
cd prompt/
docker build -t dice-guesser .
docker run --name dice-guesser-container -p 5000:5000 dice-guesser
docker stop dice-guesser-container
docker rm dice-guesser-container
```