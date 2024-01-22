from pydantic import BaseModel
from typing import List
from enum import Enum


class AccessLevel(str, Enum):
    onlyClatchTeam = "onlyClatchTeam"
    allUsers = "allUsers"


class StoryPreviewTextBase(BaseModel):
    #TODO Вынести все в отдельный файл schemes
    textColor: str
    title: str
    subtitle: str
    sizeBetweenTitles: float


class StoryPreviewBase(BaseModel):
    previewImageUrl: str
    previewText: StoryPreviewTextBase


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


class StoryButtonBase(BaseModel):
    text: str
    textColor: str
    buttonColor: str
    url: str


class StoryScreenBase(BaseModel):
    imageUrl: str
    duration: int
    storyText: StoryTextBase
    storyButton: StoryButtonBase


class StoryBase(BaseModel):
    # В Base прописывыем все, кроме связей и id
    progressBarColor: str
    statusBarColor: str
    accessLevel: AccessLevel


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