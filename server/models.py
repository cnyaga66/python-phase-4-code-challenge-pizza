from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RestaurantPizza(db.Model):

    @validates('price')
    def validate_price(self, key, price):
        if price < 1 or price > 30:
            raise ValueError('Price must be between 1 and 30')
        return price
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    restaurant_pizza = db.relationship('RestaurantPizza', backref='restaurant', lazy=True)
class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
    restaurant_pizza = db.relationship('RestaurantPizza', backref='pizza', lazy=True)
class RestaurantPizza(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

def to_dict(self):
    return{
        'id': self.id,
        'pizza': self.pizza.to_dict(),
        'pizza_id': self_pizza_id,
        'price': self.price,
        'restaurant_id': self.restaurant_id
    }

def _init_(self, price, pizza_id, restaurant_id):
    self.price = price
    self.pizza_id = pizza_id
    self.restaurant_id = restaurant_id

def _repr_(self):
    return f'<RestaurantPizza {self.id}>'  