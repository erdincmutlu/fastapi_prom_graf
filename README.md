# fast_prom_graf
FastAPI Prometheus Grafana

## Running
```
docker compose up
```

## Endpoints

### GET /hello
```
http://127.0.0.1:8000/hello?name=Erdinc
```
Returns
```
{
"greeting": "Hello Erdinc!"
}
```

### POST /things
To post things
```
curl -X POST -H "Content-Type: application/json" -d '{"name": "Erdinc", "city": "London", "age": 25}' http://127.0.0.1:8000/things
```
Returns
```
{
  "response": "Hello Erdinc! 25 years old from London."
}
```

## Prometheus
You can access Prometheus at http://localhost:9090/ and explore the metrics collected
