from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class AccessLevel(str, Enum):
    onlyClatchTeam = "onlyClatchTeam"
    allUsers = "allUsers"

class TextAlign(str, Enum):
    left = "left"
    center = "center"
    right = "right"

class TextPosition(str, Enum):
    top = "top"
    middle = "middle"
    bottom = "bottom"

class StoryPreviewText(BaseModel):
    id: Optional[int]
    textColor: Optional[str]
    title: Optional[str]
    subTitle: Optional[str]
    sizeBetweenTitles: Optional[float]

    class Config:
        orm_mode = True


class StoryPreview(BaseModel):
    id: Optional[int]
    previewImageUrl: str
    previewText: Optional[StoryPreviewText]

    class Config:
        orm_mode = True


class StoryText(BaseModel):
    id: Optional[int]
    textColor: Optional[str]
    title: Optional[str]
    fontSizeTitle: Optional[float]
    lineSpacingTitle: Optional[float]
    subTitle: Optional[str]
    fontSizeSubtitle: Optional[float]
    lineSpacingSubtitle: Optional[float]
    sizeBetweenTitles: Optional[float]
    textPosition: Optional[TextPosition]
    textAlign: Optional[TextAlign]

    class Config:
        orm_mode = True


class StoryButton(BaseModel):
    id: Optional[int]
    text: str
    textColor: Optional[str]
    buttonColor: Optional[str]
    url: str


    class Config:
        orm_mode = True

    def __str__(self):
        return f"StoryButton(text={self.text}, textColor={self.textColor}, buttonColor={self.buttonColor}, url={self.url})"



class StoryScreen(BaseModel):
    id: Optional[int]
    imageUrl: str
    duration: Optional[int]
    storyText: StoryText
    storyButton: StoryButton



class Story(BaseModel):
    id: Optional[int]
    progressBarColor: str
    statusBarColor: str
    accessLevel: Optional[AccessLevel]
    storyScreens: List[StoryScreen]
    storyPreview: StoryPreview

    class Config:
        orm_mode = True