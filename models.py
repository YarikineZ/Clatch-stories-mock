from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel
from enums import *


class StoryBase(SQLModel):
    progressBarColor: str
    statusBarColor: str
    accessLevel: Optional[AccessLevel] = Field(default=AccessLevel.allUsers)


class StoryPreviewBase(SQLModel):
    previewImageUrl: str = Field(default=None)
    story_id: Optional[int] = Field(default=None, foreign_key="story.id")


class StoryScreenBase(SQLModel):
    imageUrl: str = Field(default=None)
    duration: Optional[int] = Field(default=15)
    story_id: Optional[int] = Field(default=None, foreign_key="story.id")


class StoryTextBase(SQLModel):
    textColor: Optional[str] = Field(default=None)
    title: Optional[str] = Field(default=None)
    fontSizeTitle: Optional[float] = Field(default=None)
    lineSpacingTitle: Optional[float] = Field(default=None)
    subTitle: Optional[str] = Field(default=None)
    fontSizeSubtitle: Optional[float] = Field(default=None)
    lineSpacingSubtitle: Optional[float] = Field(default=None)
    sizeBetweenTitles: Optional[float] = Field(default=None)
    textPosition: Optional[TextPosition] = Field(TextPosition.top) 
    textAlign: Optional[TextAlign] = Field(TextAlign.left) 
    screen_id: Optional[int] = Field(default=None, foreign_key="storyscreen.id")


class StoryButtonBase(SQLModel):
    textColor: Optional[str] = Field(default=None)
    buttonColor: Optional[str] = Field(default=None)
    url: str = Field(default=None)
    screen_id: Optional[int] = Field(default=None, foreign_key="storyscreen.id")


class StoryPreviewTextBase(SQLModel):
    textColor: Optional[str]
    title: Optional[str]
    subTitle: Optional[str]
    sizeBetweenTitles: Optional[float]
    storyPreview_id: Optional[int] = Field(default=None, foreign_key="storypreview.id")

# =====================================
    
class Story(StoryBase, table=True):
    id: int = Field(default=None, primary_key=True)
    preview: Optional["StoryPreview"] = Relationship(back_populates="story")
    storyScreens: Optional[List["StoryScreen"]] = Relationship(back_populates="story")


class StoryPreview(StoryPreviewBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    story: Optional["Story"] = Relationship(back_populates="preview")
    storyPreviewText: Optional["StoryPreviewText"] = Relationship(back_populates="storyPreview")


class StoryScreen(StoryScreenBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    story: Optional["Story"] = Relationship(back_populates="storyScreens")
    storyButton: Optional["StoryButton"] = Relationship(back_populates="storyScreen")
    storyText: Optional["StoryText"] = Relationship(back_populates="storyScreen")


class StoryText(StoryTextBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    storyScreen: Optional[StoryScreen] = Relationship(back_populates="storyText")


class StoryPreviewText(StoryPreviewTextBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    storyPreview: Optional["StoryPreview"] = Relationship(back_populates="storyPreviewText")


class StoryButton(StoryButtonBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    storyScreen: Optional["StoryScreen"] = Relationship(back_populates="storyButton")




# =====================================

class StoryButtonRead(StoryScreenBase):
    id: int

class StoryTextRead(StoryScreenBase):
    id: int

class StoryScreenRead(StoryScreenBase):
    id: int
    storyButton: Optional[StoryButtonRead]
    storyText: Optional[StoryTextRead]


class StoryPreviewTextRead(StoryPreviewTextBase):
    id: int


class StoryPreviewRead(StoryPreviewBase):
    id: int
    previewText: StoryPreviewTextRead


class StoryRead(StoryBase):
    id: int
    storyScreens: Optional[List[StoryScreenRead]]
    preview: Optional[StoryPreviewRead]

class StoryCreate(StoryBase):
    pass