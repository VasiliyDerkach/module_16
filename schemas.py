from pydantic import BaseModel
class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int
class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int
class CreateTask(BaseModel):
    title: str
    content: str
    priority: int
class UpdateTask(BaseModel) с теми же атрибутами, что и CreateTask.
    title: str
    content: str
    priority: int