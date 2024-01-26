from sqlalchemy.orm import Session
import models


def get_story(db: Session, story_id: int):
    return db.query(models.Story).filter(models.Story.id == story_id).first()

