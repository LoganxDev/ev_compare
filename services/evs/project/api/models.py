from sqlalchemy.sql import func
from project import db


class EV(db.Model):

    __tablename__ = 'evs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    make = db.Column(db.String(128), nullable=False)
    brand = db.Column(db.String(128), nullable=False)
    ranges = db.relationship('Range', backref='ev', lazy=True)
    base_price = db.Column(db.Integer, nullable=False)
    storage = db.Column(db.Integer, nullable=False)
    option_ids = db.relationship('Option', backref='ev', lazy=True)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, make, brand, ranges, base_price,
                 storage, option_ids):
        self.make = make
        self.brand = brand
        if ranges:
            self.ranges = ranges
        self.base_price = base_price
        self.storage = storage
        if option_ids:
            self.option_ids = option_ids

    def to_json(self):
        return {
            'id': self.id,
            'make': self.make,
            'brand': self.brand,
            'ranges': self.ranges if self.ranges else [],
            'base_price': self.base_price,
            'storage': self.storage,
            'option_ids': self.option_ids if self.option_ids else []
        }


class Range(db.Model):
    __tablename__ = 'ranges'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    miles = db.Column(db.Integer, nullable=False)
    added_cost = db.Column(db.Integer, nullable=False)
    make_id = db.Column(db.Integer, db.ForeignKey('evs.id'), nullable=False)
    # Might add battery capacity with the range later
    # kwH = db.Column(db.Integer, nullable=False)

    def __init__(self, miles, added_cost):
        self.miles = miles
        self.added_cost = added_cost


class Option(db.Model):
    __tablename__ = 'options'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    option = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    added_cost = db.Column(db.Integer, nullable=False)
    make_id = db.Column(db.Integer, db.ForeignKey('evs.id'))

    def __init__(self, option, description, added_cost):
        self.option = option
        self.description = description
        self.added_cost = added_cost
