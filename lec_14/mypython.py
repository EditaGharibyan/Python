from flask import Flask, jsonify, request, abort
import json
import os

app = Flask(__name__)

DATA_FILE = 'cars.json'

def initialize_data_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as file:
            json.dump([], file)


def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_data(cars):
    with open(DATA_FILE, 'w') as file:
        json.dump(cars, file, indent=4)


initialize_data_file()


@app.route('/cars', methods=['GET'])
def get_cars():
    cars = load_data()
    return jsonify(cars)

@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    cars = load_data()
    car = next((car for car in cars if car['id'] == car_id), None)
    if not car:
        abort(404, description="Car not found")
    return jsonify(car)

@app.route('/cars', methods=['POST'])
def create_car():
    if not request.json or not {'make', 'model', 'year', 'price'}.issubset(request.json):
        abort(400, description="Missing required fields")

    cars = load_data()
    new_id = max((car['id'] for car in cars), default=0) + 1
    car = {
        "id": new_id,
        "make": request.json['make'],
        "model": request.json['model'],
        "year": request.json['year'],
        "price": request.json['price']
    }
    cars.append(car)
    save_data(cars)
    return jsonify(car), 201

@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    cars = load_data()
    car = next((car for car in cars if car['id'] == car_id), None)
    if not car:
        abort(404, description="Car not found")

    updates = request.json
    car.update({
        k: updates[k] for k in ['make', 'model', 'year', 'price'] if k in updates
    })
    save_data(cars)
    return jsonify(car)

@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    cars = load_data()
    car = next((car for car in cars if car['id'] == car_id), None)
    if not car:
        abort(404, description="Car not found")

    cars.remove(car)
    save_data(cars)
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
