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
    db_story = models.Story(
        progressBarColor=storyData.progressBarColor,
        statusBarColor=storyData.statusBarColor,
        accessLevel=storyData.accessLevel,
    )
    db.add(db_story)
    # db.commit()

    db_preview = models.StoryPreview(
        previewImageUrl=storyData.preview.previewImageUrl,
        story=db_story #возможно это не сработает. тогда используем нижее
    )
    db.add(db_preview)


    db_previewText = models.StoryPreviewText(
        textColor=storyData.preview.previewText.textColor,
        title=storyData.preview.previewText.title,
        subTitle=storyData.preview.previewText.subTitle,
        sizeBetweenTitles=storyData.preview.previewText.sizeBetweenTitles,
        storyPreview_id = db_preview.id
        )    
    db.add(db_previewText)


    for screen in storyData.storyScreens:
        db_screen = models.StoryScreen(
            imageUrl=screen.imageUrl,
            duration=screen.duration,
            story=db_story    
            # Добавьте остальные атрибуты StoryScreen
        )
        # db_screen.story_id = story.id
        db.add(db_screen)

        db_story_text = models.StoryText(
            textColor=screen.storyText.textColor,
            title=screen.storyText.title,
            fontSizeTitle=screen.storyText.fontSizeTitle,
            lineSpacingTitle=screen.storyText.lineSpacingTitle,
            subTitle=screen.storyText.subTitle,
            fontSizeSubtitle=screen.storyText.fontSizeSubtitle,
            lineSpacingSubtitle=screen.storyText.lineSpacingSubtitle,
            sizeBetweenTitles=screen.storyText.sizeBetweenTitles,
            textPosition=screen.storyText.textPosition,
            textAlign=screen.storyText.textAlign,

            storyScreen=db_screen

        )
        db.add(db_story_text)

        db_story_button = models.StoryButton(
            text=screen.storyButton.text,
            textColor=screen.storyButton.textColor,
            buttonColor=screen.storyButton.buttonColor,
            url=screen.storyButton.url,

            storyScreen=db_screen
        )
        db.add(db_story_button)





    db.commit()
    db.refresh(db_story)
    return db_story

@app.get("/story/{user_id}", response_model=schemes.StoryCreate)
def read_story(user_id: int):
    pass  # Здесь должен быть код для чтения пользователя и его адреса из базы данных
