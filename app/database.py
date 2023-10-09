import sqlalchemy
import databases

DATABASE_URL = "postgresql://postgres:postgres@localhost/contest"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL)

from app.models import Task, AnsValidation

async def init_db():
    await database.connect()
    metadata.create_all(engine)
    await database.disconnect()