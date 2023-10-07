from fastapi import FastAPI
from app.admin import admin_routes
from app.client import client_routes
from app.database import init_db

app = FastAPI()

app.include_router(admin_routes.router, prefix="/admin")
app.include_router(client_routes.router, prefix="/client")


# Инициализация базы данных
@app.on_event("startup")
async def startup_db():
    await init_db()