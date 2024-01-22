# Part 0: Web Development

```
cd prompt/
docker build -t login-app .
docker run --name login-app-container -p 5000:5000 login-app
docker stop login-app-container
docker rm login-app-container
```