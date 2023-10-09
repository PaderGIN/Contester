from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.models import TaskCreate  # Импортируйте созданную Pydantic модель
from app.database import init_db
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="../templates")

@router.get("/create_task/")
def create_task_form(request: Request):
    return templates.TemplateResponse("admin/task_form.html", {"request": request})

@router.post("/create_task/")
def create_task(
    request: Request,
    task_data: TaskCreate,  # Используйте Pydantic модель для валидации данных
    db: Session = Depends(init_db)
):
    # Создайте объект Task из данных Pydantic модели
    task = Task(
        name=task_data.name,
        description=task_data.description,
        time_limit=task_data.time_limit,
        memory_limit=task_data.memory_limit,
        input_format=task_data.input_format,
        output_format=task_data.output_format
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return templates.TemplateResponse("admin/task_form.html", {"request": request, "task_created": True})
