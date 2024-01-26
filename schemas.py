from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class AccessLevel(str, Enum):
    onlyClatchTeam = "onlyClatchTeam"
    allUsers = "allUsers"


class StoryPreviewText(BaseModel):
    textColor: Optional[str]
    title: Optional[str]
    subTitle: Optional[str]
    sizeBetweenTitles: Optional[float]


class StoryPreview(BaseModel):
    previewImageUrl: str
    previewText: Optional[StoryPreviewText]


class StoryTextBase(BaseModel):
    textColor: Optional[str]
    title: Optional[str]
    fontSizeTitle: Optional[float]
    lineSpacingTitle: Optional[float]
    subTitle: Optional[str]
    fontSizeSubtitle: Optional[float]
    lineSpacingSubtitle: Optional[float]
    sizeBetweenTitles: Optional[float]
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

    class Config:
        orm_mode = True


class StoryBase(BaseModel):
    progressBarColor: str
    statusBarColor: str
    accessLevel: Optional[AccessLevel]
    storyScreens: List[StoryScreen]
    preview: StoryPreview



class StoryCreate(StoryBase):
    pass

class Story(StoryBase):
    id: Optional[int]

    # progressBarColor: Optional[str]
    # statusBarColor: Optional[str]
    # accessLevel: Optional[AccessLevel]
    # storyScreens: Optional[List[StoryScreen]]
    # preview: Optional[StoryPreview]

    class Config:
        orm_mode = True