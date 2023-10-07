from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(String, primary_key=True, default=str(uuid.uuid4()), unique=True, index=True)
    description = Column(String, nullable=False)
    time_limit = Column(Integer, nullable=False)
    memory_limit = Column(Integer, nullable=False)

    # Связь с таблицей AnsValidation
    validations = relationship("AnsValidation", back_populates="task")

class AnsValidation(Base):
    __tablename__ = 'ans_validations'

    id = Column(Integer, primary_key=True, index=True)
    input_data = Column(String, nullable=False)
    expected_output = Column(String, nullable=False)

    # Внешний ключ для связи с таблицей Task
    task_id = Column(String, ForeignKey('tasks.id'))

    # Связь с таблицей Task
    task = relationship("Task", back_populates="validations")
