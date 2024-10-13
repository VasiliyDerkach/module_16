from backend.db import Base
from sqlalchemy.orm import  relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from models import *
class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority= Column(Integer,default=0)
    completed = Column(Boolean,default=False)
    user_id = Column(Integer, ForeignKey('users.id'), index=True,nullable=False)
    slug = Column(String, index=True,unique=True)
    user = relationship('User',    back_populates = 'tasks')
from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))