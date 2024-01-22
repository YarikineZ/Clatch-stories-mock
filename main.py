from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.story_model import StoryRead, StoryCreate




app = FastAPI()

@app.post("/story/")
def create_story(story: StoryCreate):
    pass  # Здесь должен быть код для сохранения пользователя и адреса в базу данных

@app.get("/story/{user_id}", response_model=StoryRead)
def read_story(user_id: int):
    pass  # Здесь должен быть код для чтения пользователя и его адреса из базы данных
