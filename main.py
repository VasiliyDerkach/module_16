from fastapi import FastAPI
from routers import user, task
app = FastAPI()
@app.get('/')
async def get_main():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.tsk)
app.include_router(task.tsk)

#python -m uvicorn main:app