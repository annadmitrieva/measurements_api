This repository contains a FastAPI application for storing raw measurements from sensors as well as retrieving data aggregates from these sensors. It uses a PostgreSQL database.  

The database contains one table, "Measurements", an example of which is provided in the repository.  

There are three endpoinds in this api:  

1) **Create measurements**: stores raw measurement values, containing sensor ID, measurement type, timestamp of recording (timestap with timezone), and measurement value (float).  
2) **View data**: see all data points currently in the table.
3) **Aggregate measurements**: retrieve measurement aggregates (time-series) for a given sensor ID. The user is able to provide:
    * **Sensor ID**: in the example table, 12 or 13
    * **Measurement type**: in the example table, temperature celsius or relative humidity
    * **Time frame**: start and end times of measurements. The earliest time in the example database is around `2022-12-11T14:40:00.966000+02:00`, and the latest is around `2022-12-12T17:00:00.834000+02:00`.
    * Choose whether **5 minute aggregates or hourly aggregates** are being returned: string value of `5 minutes` or `hour`.

**NB!** Don't forget to change values in database.py for your database name, username and password.
