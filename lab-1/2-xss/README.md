# Part 2: XSS

```
cd prompt/
docker build -t xss-me .
docker run --name xss-me-container -p 5000:5000 xss-me
docker stop xss-me-container
docker rm xss-me-container
```