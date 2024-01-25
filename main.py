from typing import List
from fastapi import FastAPI, Depends, HTTPException
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
def create_story(storyData: schemes.Story, db: Session = Depends(get_db)):
    db_story = models.Story(**storyData.dict(exclude={"preview", "storyScreens"}))
    db.add(db_story)

    db_preview = models.StoryPreview(story=db_story, **storyData.preview.dict(exclude={"previewText"}))
    db.add(db_preview)

    db_previewText = models.StoryPreviewText(storyPreview=db_preview, **storyData.preview.previewText.dict())
    db.add(db_previewText)

    for screen in storyData.storyScreens:
        db_screen = models.StoryScreen(story=db_story, **screen.dict(exclude={"storyText", "storyButton"}))
        db.add(db_screen)

        db_story_text = models.StoryText(storyScreen=db_screen, **screen.storyText.dict())
        db.add(db_story_text)

        db_story_button = models.StoryButton(storyScreen=db_screen, **screen.storyButton.dict())
        db.add(db_story_button)

    db.commit()
    db.refresh(db_story)
    return db_story

@app.get("/all_stories/", response_model=schemes.Story)
def get_all_stories(db: Session = Depends(get_db))  -> List[schemes.Story]:
    stories = db.execute(select(models.Story)).all()
    if stories is None:         #TODO добавить none в серриализатор
        return None
    return [schemes.Story.from_orm(story) for story in stories]


@app.get("/story/", response_model=schemes.Story)
def get_story(story_id: int, db: Session = Depends(get_db)):
    story = db.execute(select(models.Story).where(models.Story.id == story_id)).first()
    if story is None:
        raise HTTPException(status_code=404, detail="Story not found")
    print(schemes.Story.from_orm(story))
    return schemes.Story.from_orm(story)

@app.get("/story-button/", response_model=schemes.Story)
def get_storyButton(storyButton_id: int, db: Session = Depends(get_db)):
    storyButton = db.execute(select(models.StoryButton).where(models.StoryButton.id == storyButton_id)).first()
    print(storyButton)
    print(schemes.StoryButton.from_orm(storyButton))
    if storyButton is None:
        raise HTTPException(status_code=404, detail="Story Button not found")
    return schemes.StoryButton.from_orm(storyButton)


