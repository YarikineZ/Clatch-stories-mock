from enum import Enum
from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel





class StoryPreviewTextBase(SQLModel):
    textColor: Optional[str]
    title: Optional[str]
    subTitle: Optional[str]
    sizeBetweenTitles: Optional[float]

    storyPreview_id: Optional[int] = Field(default=None, foreign_key="storypreview.id")

class StoryPreviewText(StoryPreviewTextBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    storyPreview: Optional["StoryPreview"] = Relationship(back_populates="StoryPreviewText")

class StoryPreviewTextRead(StoryPreviewTextBase):
    id: int
    
#==============

class StoryPreviewBase(SQLModel):
    previewImageUrl: str = Field(default=None)

    story_id: Optional[int] = Field(default=None, foreign_key="story.id")

class StoryPreview(StoryPreviewBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    story: Optional["Story"] = Relationship(back_populates="screen")

  
class StoryPreviewRead(StoryPreviewBase):
    id: int
    # previewImageUrl: 
    previewText: StoryPreviewTextRead

#==============

class StoryScreenBase(SQLModel):
    imageUrl: str = Field(default=None)
    duration: Optional[int] = Field(default=15)

    story_id: Optional[int] = Field(default=None, foreign_key="story.id")


class StoryScreen(StoryScreenBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    story: Optional["Story"] = Relationship(back_populates="screen")


class StoryScreenRead(StoryScreenBase):
    id: int


#==============
    

class AccessLevel(Enum):
    onlyClatchTeam = "onlyClatchTeam"
    allUsers = "allUsers"



class StoryBase(SQLModel):
    progressBarColor: str
    statusBarColor: str
    accessLevel: Optional[AccessLevel] = Field(default=AccessLevel.allUsers)

class Story(StoryBase, table=True):
    id: int = Field(default=None, primary_key=True)
    preview: Optional[StoryPreview] = Relationship(back_populates="story")
    storyScreens: Optional[List["StoryScreen"]] = Relationship(back_populates="story")

  
class StoryRead(StoryBase):
    id: int
    storyScreens: List[StoryScreenRead]
    preview: StoryPreviewRead
