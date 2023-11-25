# flask_prom_graf
Flask Prometheus Grafana

## Building and Running
### To Build
```
./build.sh
```
## To run
On terminal
```
./run_server.sh
```

On another terminal
```
./run_prometheus.sh
```

## Flask Server
Run Flask server
```
python server.py
```

### GET /hello
```
http://127.0.0.1:5000/hello?name=Erdinc
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
curl -X POST -H "Content-Type: application/json" -d '{"name": "Erdinc", "city": "London", "age": 25}' http://127.0.0.1:5000/things
```
Returns
```
{
  "response": "Hello Erdinc! 25 years old from London."
}
```

## Prometheus
You can access Prometheus at http://localhost:9090/ and explore the metrics collected
