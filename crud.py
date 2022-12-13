from sqlalchemy.orm import Session
import datetime
from sqlalchemy.sql import func
from sqlalchemy import select
from . import models, schemas


TIME_FRAMES = {'5 minutes': 300, 'hour': 3600}


def get_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Measurement).offset(skip).limit(limit).all()


def get_measurements(db: Session, 
                     sensor_id: int, 
                     measurement_type: str, 
                     time_start: datetime.datetime, 
                     time_end: datetime.datetime,
                     time_frame: str
                     ):
    seconds = TIME_FRAMES[time_frame]
    r = db.query(func.to_timestamp(seconds*func.floor(func.extract('epoch', models.Measurement.timestamp)/seconds)).label('time_stamp'), 
                 func.min(models.Measurement.measurement_value).label('minimum'), 
                 func.max(models.Measurement.measurement_value).label('maximum'),
                 func.avg(models.Measurement.measurement_value).label('mean')).filter(models.Measurement.sensor_id == sensor_id, 
                                                                                      models.Measurement.measurement_type == measurement_type,
                                                                                      models.Measurement.timestamp.between(time_start, time_end)
                                                                                      ).group_by('time_stamp')
    return r.all()


def create_measurement(db: Session, measure: schemas.MeasurementCreate):
    db_measure = models.Measurement(sensor_id=measure.sensor_id, measurement_type=measure.measurement_type, 
    timestamp=measure.timestamp, measurement_value=measure.measurement_value)
    db.add(db_measure)
    db.commit()
    db.refresh(db_measure)
    return db_measure