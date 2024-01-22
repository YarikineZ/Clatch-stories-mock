from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class AccessLevel(str, Enum):
    onlyClatchTeam = "onlyClatchTeam"
    allUsers = "allUsers"


class PreviewText(BaseModel):
    #TODO Вынести все в отдельный файл schemes
    textColor: Optional[str]
    title: Optional[str]
    subtitle: Optional[str]
    sizeBetweenTitles: Optional[float]


class Preview(BaseModel):
    previewImageUrl: str
    previewText: Optional[PreviewText]


class StoryTextBase(BaseModel):
    textColor: Optional[str]
    title: Optional[str]
    fontSizeTitle: Optional[float]
    lineSpacingTitle: Optional[float]
    subTitle: Optional[str]
    fontSizeSubtitle: Optional[float]
    lineSpacingSubtitle: Optional[float]
    sizeBetweenTitle: Optional[float]
    textPosition: Optional[str]
    textAlign: Optional[str]


class StoryButton(BaseModel):
    text: str
    textColor: Optional[str]
    buttonColor: Optional[str]
    url: str


class StoryScreen(BaseModel):
    imageUrl: str
    duration: Optional[int]
    storyText: StoryTextBase
    storyButton: StoryButton


class StoryBase(BaseModel):
    progressBarColor: str
    statusBarColor: str
    accessLevel: Optional[AccessLevel]
    storyScreens: List[StoryScreen]
    preview: Preview


class StoryCreate(StoryBase):
    pass

class Story(StoryBase):
    id: int


    class Config:
        orm_mode = True