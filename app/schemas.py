from pydantic import BaseModel

class AttendeeCreate(BaseModel):
    name: str
    email: str
    event_id: int

class EventCreate(BaseModel):
    name: str
    description: str

class Attendee(BaseModel):
    id: int
    name: str
    email: str
    is_present: bool
    event_id: int

    class Config:
        orm_mode = True
