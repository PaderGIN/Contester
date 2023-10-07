# app/client/client_routes.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/task/{task_id}")
def get_task(task_id: int):
    # Логика для отображения задачи клиенту
    ...

@router.post("/submit/")
def submit_code():
    # Логика для отправки решения клиентом
    ...

# Другие маршруты для клиента
