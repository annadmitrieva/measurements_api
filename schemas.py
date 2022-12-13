from typing import List, Union

from pydantic import BaseModel

import datetime


class MeasurementBase(BaseModel):
    id: int
    sensor_id: int
    measurement_type: str
    timestamp: datetime.datetime
    measurement_value: float


class MeasurementCreate(MeasurementBase):
    sensor_id: int
    measurement_type: str
    timestamp: datetime.datetime
    measurement_value: float


class Measurement(MeasurementBase):
    id: int
    sensor_id: int
    measurement_type: str
    timestamp: datetime.datetime
    measurement_value: float

    class Config:
        orm_mode = True
