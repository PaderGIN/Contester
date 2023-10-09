from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.admin import admin_routes
from app.client import client_routes
from app.database import init_db
from fastapi.templating import Jinja2Templates

import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="../static"), name="static")

templates = Jinja2Templates(directory="../templates")

app.include_router(admin_routes.router, prefix="/admin")
app.include_router(client_routes.router, prefix="/client")

# Инициализация базы данных
@app.on_event("startup")
async def startup_db():
    await init_db()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5050)
