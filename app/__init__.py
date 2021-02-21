# __init__.py - обязательный файл для инициализации приложения, инициализация – это подготовка к запуску

# импортируем из модуля flask объект Flask, спец класс, который создает приложение
from flask import Flask
# для работы с БД, импортируем из библиотеки flask_sqlalchemy пакет SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# импортируем из библиотеки flask_migrate пакет Migrate для работы с миграциями
from flask_migrate import Migrate

# создаем экземпляр класса Flask, по сути это и будет наше приложение
# первый аргумент - это имя модуля или пакета приложения, мы передаем туда обязательную переменную __name__
# static_url_path и static_folder — это специальные параметры, в которых указывается путь к статическим файлам
app = Flask(__name__,
            static_url_path='',
            static_folder='static')

# подключаем базу данных к приложению
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../carshering.sqlite"

# создаем саму базу данных - объект db, для чего передаем SQLAlchemy app (переменную являющуюся нашим приложением)
db = SQLAlchemy(app)    # создаем экземпляр базы данных

# отключаем вывод технических сообщений
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# создаем объект для работы с миграциями
migrate = Migrate(app, db)

# импортируем из пакета app файл маршрутизации views.py
from app import views
# импортируем из пакета app файл с моделями (таблицами) models.py
from app import models
