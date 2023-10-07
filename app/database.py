import sqlalchemy
import databases

DATABASE_URL = "postgresql://postgres:postgres@localhost/contest"

# Создание подключения к базе данных
database = databases.Database(DATABASE_URL)

# Создание объекта для работы с SQLAlchemy
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Модели базы данных (в models.py определите модели таблиц)
from app.models import Task, AnsValidation

# Асинхронная функция для инициализации базы данных
async def init_db():
    await database.connect()
    # Создание таблиц, если их нет
    metadata.create_all(engine)
    await database.disconnect()