# models.py - файл где хранятся все таблицы БД
# во Flask они называются - моделями

# импортируем из пакета app нашу переменную db (экземпляр БД)
from app import db
# импортируем из модуля datetime функцию datetime - для работы с датой и временем
from datetime import datetime

# после создания моделей - их необходимо импортировать в файл __init__.py

# создаем таблицу Car. Модель базы данных (таблица) - это класс.
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_auto = db.Column(db.String(128), nullable=False)
    describe = db.Column(db.String(128), nullable=False)
    rent_price = db.Column(db.Float)
    transmission = db.Column(db.Boolean)
    img_url = db.Column(db.String(128))
    img_url2 = db.Column(db.String(128))
    img_url3 = db.Column(db.String(128))
    img_url4 = db.Column(db.String(128))
    rents = db.relationship('Rent', backref='car', cascade='all,delete-orphan')

# создаем таблицу (класс )Rent - это будет журнал аренды авто
class Rent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))
    created = db.Column(db.DateTime, default=datetime.now)
    completion = db.Column(db.DateTime)
