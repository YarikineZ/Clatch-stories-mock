from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models, schemes
from sqlmodel import Session, create_engine, select

# http://127.0.0.1:8000/docs
# uvicorn main:app --reload

connect_args = {"check_same_thread": False} # Не понял зачем этот проверяльщик, но он нужен только для SQLite
engine = create_engine("sqlite:///database.db", echo=True, connect_args=connect_args)
models.Base.metadata.create_all(bind=engine)

# def get_session():
#     with Session(engine) as session:
#         yield session


def get_db():
    db = sessionmaker.SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

@app.post("/story/")
def create_story(storyData: schemes.StoryCreate):
    db = Session(engine) #TODO вынести как аргумент функции db: Session = Depends(get_db)
    # db_story = models.Story(**storyData.dict()) - не завелось
    story = models.Story(
        progressBarColor=storyData.progressBarColor,
        statusBarColor=storyData.statusBarColor,
        accessLevel=storyData.accessLevel,
    )
    db.add(story)
    db.commit()

    for screen in storyData.storyScreens:
        db_screen = models.StoryScreen(
            imageUrl=screen.imageUrl,
            duration=screen.duration,
            # Добавьте остальные атрибуты StoryScreen
        )
        db_screen.story_id = story.id
        db.add(db_screen)

    preview = models.StoryPreview(
        previewImageUrl=storyData.preview.previewImageUrl
        # Добавьте остальные атрибуты StoryPreview
        # TODO Добавить Пресью текст и остальные модели
    )
    preview.story_id = story.id
    db.add(preview)

    db.commit()
    db.refresh(story)
    return story

@app.get("/story/{user_id}", response_model=schemes.StoryCreate)
def read_story(user_id: int):
    pass  # Здесь должен быть код для чтения пользователя и его адреса из базы данных
