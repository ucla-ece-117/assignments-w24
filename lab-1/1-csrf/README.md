# Part 1: CSRF

```
cd prompt/
docker build -t csrfing-usa .
docker run --name csrfing-usa-container -p 5000:5000 csrfing-usa
docker stop csrfing-usa-container
docker rm csrfing-usa-container
```