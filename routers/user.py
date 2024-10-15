from fastapi import APIRouter, Depends, status, HTTPException
from backend.db_depends import get_db
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from models import Task, User
from schemas import CreateUser, UpdateUser, CreateTask, UpdateTask
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

tsk = APIRouter(prefix='/user' ,tags=['user' ])
@tsk.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalar(select(User).where())
    return users
@tsk.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)],user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    return user
@tsk.post('/create')
async def  create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db.execute(insert(User).values(username=create_user.username,
                                   firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   slug=slugify(create_user.username),
                                   age=create_user.age))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }
@tsk.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, upd_user: CreateUser):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    db.execute(update(User).where(User.id == user_id).values(
        firstname=upd_user.firstname,
        lastname=upd_user.lastname,

        age=upd_user.age
    ))
    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'User update is successful!'}


@tsk.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'User delete is successful!'}

# @tsk.get('/{user_slug}')
# async def user_by_slag(db: Annotated[Session, Depends(get_db)], user_slug: str):
#     user = db.scalar(select(User).where(User.slug == user_slug))
#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail='User was not found'
#         )
#     return user
#
