# файл - скрипт для создания БД

# импортируем из пакета app нашу переменную db (экземпляр БД)
from app import db


# метод create_all() создает БД, т.е. он создаст файл "carshering.sqlite"
db.create_all()
