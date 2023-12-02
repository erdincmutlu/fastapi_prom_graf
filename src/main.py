from fastapi import FastAPI, HTTPException
import prometheus_client as prom
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Enable Prometheus metrics
Instrumentator().instrument(app).expose(app)
# Define Prometheus metrics
hello_counter = prom.Counter('hello_requests', 'Total number of requests to /hello')
things_counter = prom.Counter('things_requests', 'Total number of requests to /things')

# GET endpoint: /hello
@app.get("/hello")
def hello_world(name:str):
    if name == "":
        name = "World"

    hello_counter.inc()  # Increment Prometheus counter
    return {"greeting": f"Hello {name}!"}

# POST endpoint: /things
@app.post("/things")
def things(data: dict):
    if not data or 'name' not in data or 'city' not in data or 'age' not in data:
        raise HTTPException(status_code=400, detail="Invalid data. Make sure to provide name, city, and age.")

    name = data['name']
    city = data['city']
    age = data['age']

    things_counter.inc()  # Increment Prometheus counter
    return {"response":f"Hello {name}! {age} years old from {city}"}

if __name__ == '__main__':
    app.run(debug=True)
