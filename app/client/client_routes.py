from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.models import Task
from app.database import init_db
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="../templates")

@router.get("/task/{task_id}")
def get_task(task_id: int):
    # Логика для отображения задачи клиенту
    ...

@router.get("/task/")
def get_task_list(request: Request):

    return

@router.get("/task/")
def get_task(request: Request):
    # Логика для отображения задачи клиенту
    return templates.TemplateResponse("client/client.html", {"request": request})

@router.post("/submit/")
def submit_code():
    # Логика для отправки решения клиентом
    ...

# Другие маршруты для клиента
