import json

from sqlalchemy.orm import relationship
from run import db


# Database models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text(100))
    last_name = db.Column(db.Text(100))
    age = db.Column(db.Integer)
    email = db.Column(db.Text(50))
    role = db.Column(db.Text(50))
    phone = db.Column(db.Text(20))
    offers = relationship('Offer', cascade="all, delete")

    def to_dict(self) -> dict[str, any]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }


    def update_user(self, params: [str, str]):
        try:
            self.first_name = params["first_name"]
        except KeyError:
            ...

        try:
            self.last_name = params["last_name"]
        except KeyError:
            ...

        try:
            self.age = params["age"]
        except KeyError:
            ...

        try:
            self.email = params["email"]
        except KeyError:
            ...

        try:
            self.role = params["role"]
        except KeyError:
            ...

        try:
            self.phone = params["phone"]
        except KeyError:
            ...


class Offer(db.Model):
    __tablename__ = 'offers'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def to_dict(self) -> dict[str, any]:
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id
        }


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(100))
    description = db.Column(db.Text(200))
    start_date = db.Column(db.Text(50))
    end_date = db.Column(db.Text(50))
    address = db.Column(db.Text(200))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    customer = relationship("User", foreign_keys=[customer_id], backref='customer', lazy=True, cascade="all, delete")
    executor = relationship("User", foreign_keys=[executor_id], cascade="all, delete")

    def to_dict(self) -> dict[str, any]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price
        }

    def update(self, params: [str, str]):
        try:
            self.name = params["name"]
        except KeyError:
            ...

        try:
            self.description = params["description"]
        except KeyError:
            ...

        try:
            self.start_date = params["start_date"]
        except KeyError:
            ...

        try:
            self.end_date = params["end_date"]
        except KeyError:
            ...

        try:
            self.address = params["address"]
        except KeyError:
            ...

        try:
            self.customer_id = params["customer_id"]
        except KeyError:
            ...

        try:
            self.executor_id = params["executor_id"]
        except KeyError:
            ...

def setup_database():
    db.drop_all()
    db.create_all()

    users = []
    with open('static/data/users.json', 'rt', encoding='utf-8') as file:
        ary = json.load(file)
        for item in ary:
            model = User(**item)
            users.append(model)

    orders = []
    with open('static/data/orders.json', 'rt', encoding='utf-8') as file:
        ary = json.load(file)
        for item in ary:
            model = Order(**item)
            orders.append(model)

    offers = []
    with open('static/data/offers.json', 'rt', encoding='utf-8') as file:
        ary = json.load(file)
        for item in ary:
            model = Offer(**item)
            offers.append(model)

    with db.session.begin():
        db.session.add_all(users)
        db.session.add_all(orders)
        db.session.add_all(offers)