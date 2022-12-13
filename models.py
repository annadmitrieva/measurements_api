from sqlalchemy import Column, Integer, String, DateTime, Float, Sequence
from sqlalchemy.sql import func
from .database import Base

MEASUREMENT_ID_SEQUENCE = Sequence('measurement_id')
class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(Integer, MEASUREMENT_ID_SEQUENCE, primary_key=True, server_default=MEASUREMENT_ID_SEQUENCE.next_value())
    sensor_id = Column(Integer)
    measurement_type = Column(String)
    timestamp = Column(DateTime, server_default=func.now())
    measurement_value = Column(Float)