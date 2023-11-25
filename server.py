from flask import Flask, request, jsonify

app = Flask(__name__)

# GET endpoint: /hello
@app.route('/hello', methods=['GET'])
def hello_world():
    name = request.args.get('name', 'World')
    return jsonify(greeting=f"Hello {name}!")

# POST endpoint: /things
@app.route('/things', methods=['POST'])
def things():
    data = request.get_json()

    if not data or 'name' not in data or 'city' not in data or 'age' not in data:
        return jsonify({'error': 'Invalid data. Make sure to provide name, city, and age.'}), 400

    name = data['name']
    city = data['city']
    age = data['age']

    return jsonify(response=f"Hello {name}! {age} years old from {city}.")

if __name__ == '__main__':
    app.run(debug=True)
