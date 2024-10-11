from fastapi import APIRouter
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