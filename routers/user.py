from fastapi import APIRouter
tsk = APIRouter(prefix='/user' ,tags=['user' ])
@tsk.get('/')
async def all_users():
    pass
@tsk.get('/user_id')
async def user_by_id():
    pass
@tsk.post('/create')
async def  create_user():
    pass
@tsk.put('/update')
async def update_user():
    pass
@tsk.delete('/delete')
async def delete_user():
    pass
