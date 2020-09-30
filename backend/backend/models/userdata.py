from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    Float,
)

from .meta import Base


class UserData(Base):
    __tablename__ = 'userdata'
    id = Column(Integer, primary_key=True)
    userdata_name = Column(String(50))
    userdata_email = Column(String(50), index=True)
    userdata_wa = Column(String(50))

Index('userdata_index', UserData.userdata_email)
