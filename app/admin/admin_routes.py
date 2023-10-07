# app/admin/admin_routes.py
from fastapi import APIRouter

router = APIRouter()

@router.post("/task/create")
def create_task():
    # Логика для создания задачи администратором
    ...

@router.post("/task/update")
def update_task():
    # Логика для обновления задачи администратором
    ...

# Другие маршруты для администратора
