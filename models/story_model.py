from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class StoryPreviewText(Base):
    __tablename__ = "StoryPreviewText"

    id = Column(Integer, primary_key=True)
    textColor = Column(String)
    title = Column(String)
    subTitle = Column(String)
    sizeBetweenTitles = Column(Float)

    storyPreview_id = Column(Integer, ForeignKey('storyPreview.id'))
    storyPreview = relationship("StoryPreview", back_populates="storyPreviewText")



class StoryPreview(Base):
    __tablename__ = "storyPreview"

    id = Column(Integer, primary_key=True)
    previewImageUrl  = Column(String)

    storyPreviewText = relationship("StoryPreviewText", back_populates="storyPreview")
    story_id = Column(Integer, ForeignKey('story.id'))
    story = relationship("Story", back_populates="storyPreview")


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

    storyScreen_id = Column(Integer, ForeignKey('storyScreen.id'))
    storyScreen = relationship("StoryScreen", back_populates="storyText")


class StoryButton(Base):
    __tablename__ = "storyButton"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    textColor = Column(String)
    buttonColor = Column(String)
    url = Column(String)

    storyScreen_id = Column(Integer, ForeignKey('storyScreen.id'))
    storyScreen = relationship("StoryScreen", back_populates="storyButton")


class StoryScreen(Base):
    __tablename__ = "storyScreen"

    id = Column(Integer, primary_key=True)
    imageUrl = Column(String)
    duration = Column(Integer)
    storyText = relationship("StoryText", back_populates="storyScreen")
    storyButton = relationship("StoryButton", back_populates="storyScreen")
    story_id = Column(Integer, ForeignKey('story.id'))

    story = relationship("Story", back_populates="storyScreens")

 
class Story(Base):
    __tablename__ = "story"

    id = Column(Integer, primary_key=True, index=True)
    progressBarColor = Column(String)
    statusBarColor = Column(String)
    storyPreview = relationship("StoryPreview", back_populates="story")
    storyScreens = relationship("StoryScreen", back_populates="story")
    accessLevel = Column(String) 
