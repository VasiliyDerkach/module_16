from fastapi import APIRouter, Depends, status, HTTPException
from backend.db_depends import get_db
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from models import User, Task
from schemas import CreateUser, UpdateUser, CreateTask, UpdateTask
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

tsk = APIRouter(prefix='/task' ,tags=['task' ])
@tsk.get('/')
async def all_tasks():
    pass

@tsk.get('/task_id')
async def  task_by_id():
    pass
@tsk.post( '/create')
async def create_task():
    pass
@tsk.put('/update')
async def update_task():
    pass
@tsk.delete('/delete')
async def delete_task():
    pass