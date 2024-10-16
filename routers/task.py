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
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select().where(Task)).all()
    return tasks

@tsk.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)],task_id):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )
    return task
@tsk.post( '/create')
async def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask, user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    usr_id = user_id
    if user is None:
        usr_id = None
    # если пользователь не найден, то Task создается, но с user, user_id = None (по крайней мере, я так понял задание)
    db.execute(insert(Task).values(title=create_task.title,
                                   content=create_task.content,
                                   priority=create_task.priority,
                                   slug=slugify(create_task.title),
                                   completed=create_task.completed,
                                   user_id=usr_id,
                                   user=user
                                   )
                )
    db.commit()

    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': f'Successful{ ", but user was not found" if user is None else ""}'
    }
@tsk.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, upd_task: UpdateTask):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )
    db.execute(update(Task).where(Task.id == task_id).values(
        title=upd_task.title,
        content=upd_task.content,
        priority=upd_task.priority,
        completed=upd_task.completed,
        slug=slugify(upd_task.title)
        )
    )
    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'Task update is successful!'}
@tsk.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'Task delete is successful!'}