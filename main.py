from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlmodel import create_engine, Session, select

import models, schemes

# http://127.0.0.1:8000/docs
# uvicorn main:app --reload

connect_args = {"check_same_thread": False} 
engine = create_engine("sqlite:///database.db", echo=True, connect_args=connect_args)
models.Base.metadata.create_all(bind=engine)

def get_db():
    with Session(engine) as session:
        yield session

app = FastAPI()

@app.post("/story/")
def create_story(storyData: schemes.StoryCreate, db: Session = Depends(get_db)):
    db_story = models.Story(**storyData.dict(exclude={"preview", "storyScreens"}))
    db.add(db_story)

    db_preview = models.StoryPreview(story_id=db_story.id, **storyData.preview.dict(exclude={"previewText"}))
    db.add(db_preview)

    db_previewText = models.StoryPreviewText(storyPreview_id=db_preview.id, **storyData.preview.previewText.dict())
    db.add(db_previewText)

    for screen in storyData.storyScreens:
        db_screen = models.StoryScreen(story_id=db_story.id, **screen.dict(exclude={"storyText", "storyButton"}))
        db.add(db_screen)

        db_story_text = models.StoryText(storyScreen_id=db_screen.id, **screen.storyText.dict())
        db.add(db_story_text)

        db_story_button = models.StoryButton(storyScreen_id=db_screen.id, **screen.storyButton.dict())
        db.add(db_story_button)

    db.commit()
    db.refresh(db_story)
    return db_story

@app.get("/story/{user_id}", response_model=schemes.StoryCreate)
def read_story(user_id: int, db: Session = Depends(get_db)):
    story = db.execute(select(models.Story).where(models.Story.id == user_id)).first()
    return story
