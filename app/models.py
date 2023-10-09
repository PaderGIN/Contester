from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import List


import uuid

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(String, primary_key=True, default=str(uuid.uuid4()), unique=True, index=True)
    name = Column(String, nullable=False)  # Название задачи
    description = Column(String, nullable=False)  # Описание задачи
    time_limit = Column(Integer, nullable=False)  # Ограничение времени
    memory_limit = Column(Integer, nullable=False)  # Ограничение памяти
    input_format = Column(String, nullable=False)  # Формат ввода
    output_format = Column(String, nullable=False)  # Формат вывода

    # Связь с таблицей AnsValidation
    validations = relationship("AnsValidation", back_populates="task")

    # Метод для преобразования объекта Task в словарь
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "time_limit": self.time_limit,
            "memory_limit": self.memory_limit,
            "input_format": self.input_format,
            "output_format": self.output_format,
        }

class AnsValidation(Base):
    __tablename__ = 'ans_validations'

    id = Column(Integer, primary_key=True, index=True)
    input_data = Column(String, nullable=False)
    expected_output = Column(String, nullable=False)

    # Внешний ключ для связи с таблицей Task
    task_id = Column(String, ForeignKey('tasks.id'))

    # Связь с таблицей Task
    task = relationship("Task", back_populates="validations")

class TaskCreate(BaseModel):
    name: str
    description: str
    time_limit: int
    memory_limit: int
    input_format: str
    output_format: str
    input_data: List[str]
    expected_output: List[str]
