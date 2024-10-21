from sqlalchemy.orm import Session
from . import models, schemas

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(name=event.name, description=event.description)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def create_attendee(db: Session, attendee: schemas.AttendeeCreate):
    db_attendee = models.Attendee(
        name=attendee.name, email=attendee.email, event_id=attendee.event_id)
    db.add(db_attendee)
    db.commit()
    db.refresh(db_attendee)
    return db_attendee

def get_attendee(db: Session, attendee_id: int):
    return db.query(models.Attendee).filter(models.Attendee.id == attendee_id).first()
