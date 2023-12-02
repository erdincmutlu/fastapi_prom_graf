from fastapi import FastAPI, HTTPException

app = FastAPI()

# GET endpoint: /hello
@app.get("/hello")
def hello_world(name:str):
    if name == "":
        name = "World"
    return {"greeting": f"Hello {name}!"}

# POST endpoint: /things
@app.post("/things")
def things(data: dict):
    if not data or 'name' not in data or 'city' not in data or 'age' not in data:
        raise HTTPException(status_code=400, detail="Invalid data. Make sure to provide name, city, and age.")

    name = data['name']
    city = data['city']
    age = data['age']

    return {"response":f"Hello {name}! {age} years old from {city}"}

if __name__ == '__main__':
    app.run(debug=True)
