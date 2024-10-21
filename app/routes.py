from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database, qr_utils

app = FastAPI()

# Crear eventos
@app.post("/events/", response_model=schemas.EventCreate)
def create_event(event: schemas.EventCreate, db: Session = Depends(database.get_db)):
    return crud.create_event(db=db, event=event)

# Registrar asistentes y generar código QR
@app.post("/attendees/", response_model=schemas.Attendee)
def create_attendee(attendee: schemas.AttendeeCreate, db: Session = Depends(database.get_db)):
    db_attendee = crud.create_attendee(db=db, attendee=attendee)
    qr_utils.generate_qr_code(db_attendee.id)
    return db_attendee

# Validar asistente
@app.get("/attendees/validate/{attendee_id}")
def validate_attendee(attendee_id: int, db: Session = Depends(database.get_db)):
    attendee = crud.get_attendee(db=db, attendee_id=attendee_id)
    if not attendee:
        raise HTTPException(status_code=404, detail="Attendee not found")
    
    attendee.is_present = True
    db.commit()
    return {"message": "Attendee validated", "attendee_id": attendee.id}
