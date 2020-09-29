from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    Float,
)

from .meta import Base


class AirData(Base):
    __tablename__ = 'airdata'
    id = Column(Integer, primary_key=True)
    airdata_gps_location = Column(String(50))
    airdata_co2 = Column(Float)
    airdata_pm25 = Column(Float)
    airdata_pm10 = Column(Float)
    airdata_temperature = Column(String(5))


Index('airdata_index', AirData.airdata_gps_location, unique=True, mysql_length=255)
