#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
db = SQLAlchemy(app)

@app.route('/restaurants' ,methods=['GET'])
def get_all_restaurants():
    restaurants = Restaurants.query.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants])
@app.route('/restaurant/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurants.query.get(id)
    if restaurant:
        return jsonify(restaurant.to_dict())
    else:
        return jsonify({'message': 'Restaurant not found'}), 404
    
@app.route('/restaurant/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurants.query.get(id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'message': 'Restaurant not found'}), 404
    
@app.route('pizzas', methods=['GET'])
def get_pizza():
    pizzas = pizzas.query.all()
    return jsonify([pizza.to_dict() for pizza in pizzas])

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')
    price = data.get('price')
    if pizza_id and restaurant_id and price:
        restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(restaurant_pizza)
        db.session.commit()
        return jsonify(restaurant_pizza.to_dict()), 201
    else:
        return jsonify({'error': ['Invalid request']}), 400
    if __name__ == '_main_':
     app.run(debug=True)

