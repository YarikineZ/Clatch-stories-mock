from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from typing import List

Base = declarative_base()


#=========================StoryPreviewText
class StoryPreviewText(Base):
    __tablename__ = "storyPreviewText"

    id = Column(Integer, primary_key=True)
    textColor = Column(String)
    title = Column(String)
    subTitle = Column(String)
    sizeBetweenTitles = Column(Float)

class StoryPreviewTextBase(BaseModel):
    textColor: str
    title: str
    subtitle: str
    sizeBetweenTitles: float


#=========================StoryPreview
class StoryPreview(Base):
    __tablename__ = "storyPreview"

    id = Column(Integer, primary_key=True)
    previewImageUrl  = Column(String)
    previewText = relationship("PreviewText", back_populates="storyPreview")

class StoryPreviewBase(BaseModel):
    previewImageUrl: str
    previewText: StoryPreviewTextBase



#=========================StoryText
class StoryText(Base):
    __tablename__ = "storyText"

    id = Column(Integer, primary_key=True)
    textColor = Column(String)
    title = Column(String)
    fontSizeTitle = Column(Float)
    lineSpacingTitle = Column(Float)
    subTitle = Column(String)
    fontSizeSubtitle = Column(Float)
    lineSpacingSubtitle = Column(Float)
    sizeBetweenTitles = Column(Float)
    textPosition = Column(String) # TODO ENUM
    textAlign = Column(String) # TODO ENUM

class StoryTextBase(BaseModel):
    textColor: str
    title: str
    fontSizeTitle: float
    lineSpacingTitle: float
    subTitle: str
    fontSizeSubtitle: float
    lineSpacingSubtitle: float
    sizeBetweenTitle: float
    textPosition: str
    textAlign: str


#=========================StoryButton
class StoryButton(Base):
    __tablename__ = "storyButton"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    textColor = Column(String)
    buttonColor = Column(String)
    url = Column(String)


class StoryButtonBase(BaseModel):
    text: str
    textColor: str
    buttonColor: str
    url: str


#=========================StoryScreen
class StoryScreen(Base):
    __tablename__ = "storyScreen"

    id = Column(Integer, primary_key=True)
    imageUrl = Column(String)
    duration = Column(Integer)
    storyText = relationship("StoryText", back_populates="storyScreen")
    storyButton = relationship("StoryButton", back_populates="storyScreen")

    story = relationship("Story", back_populates="storyScreen")

class StoryScreenBase(BaseModel):
    imageUrl: str
    duration: int
    storyText: StoryTextBase
    storyButton: StoryButtonBase


#=========================Story        
class Story(Base):
    __tablename__ = "story"

    id = Column(Integer, primary_key=True, index=True)
    progressBarColor = Column(String)
    statusBarColor = Column(String)
    preview = relationship("StoryPreview", back_populates="story")
    storyScreens = relationship("StoryScreen", back_populates="story")
    accessLevel = Column(String) # TODO ENUM

class StoryBase(BaseModel):
    # В Base прописывыем все, кроме связей и id
    progressBarColor: str
    statusBarColor: str
    accessLevel: str

class StoryCreate(StoryBase):
    # Наследуюется от Base, добавляются связи, нет id
    storyScreens: List[StoryScreenBase]

class StoryRead(StoryBase):
    #Наследуюется от Base, добавляются связи, добавляется id
    id: int
    storyScreens: List[StoryScreenBase]
    StoryPreview: StoryPreviewBase

    class Config:
        orm_mode = True