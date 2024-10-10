from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel
app = FastAPI()
users = []
class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/')
async def main_page() -> dict:
    return {'message': 'Главная страница'}

@app.get('/user/admin')
async def admin_page() -> dict:
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def user_page(user_id: Annotated[int, Path(ge=1,le=100,description='Enter User ID',example='1')]) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get('/user/{username}/{age}')
async def user_page(user_name: Annotated[str,Path(min_length=5,max_length=20,description='Enter username',
                example='UrbanUser' )], age: Annotated[int,Path(ge=18,le=120,description='Enter age',example='24')]) -> dict:
    return {'message': f'Информация о пользователе. Имя: {user_name}, Возраст: {age}'}

@app.get('/users')
async def get_users()->list:
    return users

@app.post('/user/{username}/{age}')
async def add_user(usr: User )-> User:
    usr.id = len(users)+1
    users.append(usr)
    return usr

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int)-> User:
    if user_id <= len(users):
        try:
            usr = User(id=user_id,username=username,age=age)
            users[user_id-1] = usr
            return usr
        except IndexError:
            raise HTTPException(status_code= 404, detail= "User was not found")
    else:
        raise HTTPException(status_code= 404, detail= f"User.id={user_id} was not found")
@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1,le=100,description='Enter User ID',example='1')])->User:
    try:
        usr = users[user_id]
        users.pop(user_id)
        return usr
    except IndexError:
        raise HTTPException(status_code= 404, detail= "User was not found")