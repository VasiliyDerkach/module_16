from fastapi import FastAPI
from app.routers import user, task
app = FastAPI()
@app.get('/')
async def get_main():
    return {"message": "Welcome to Taskmanager"}

app.include_router(use.router)
app.include_router(task.router)