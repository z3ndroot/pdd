from . import Base
from sqlalchemy import (
    Integer,
    Column,
    String,
    DateTime)


class Driver(Base):
    driver_id = Column(Integer, primary_key=True, nullable=False)
    driver_name = Column(String(30), nullable=False)
    driver_license_number = Column(String(30), nullable=False, unique=True)
    driver_address = Column(String(30), nullable=False)
    expiration_date = Column(DateTime, nullable=False)
