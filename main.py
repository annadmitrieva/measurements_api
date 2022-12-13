from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import datetime
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/measurements/", response_model=schemas.Measurement)
def create_measurement(measure: schemas.MeasurementCreate, db: Session = Depends(get_db)):
    return crud.create_measurement(db=db, measure=measure)


@app.get("/measurements/")
def aggregate_measurements(sensor_id: int, 
                           measurement_type: str, 
                           time_start: datetime.datetime, 
                           time_end: datetime.datetime, 
                           time_frame: str,
                           db: Session = Depends(get_db)
                           ):
    measurements = crud.get_measurements(db, 
                                         sensor_id, 
                                         measurement_type, 
                                         time_start, 
                                         time_end,
                                         time_frame
                                         )
    return measurements


@app.get("/measurements/data")
def view_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    measurements = crud.get_data(db, skip=skip, limit=limit)
    return measurements
