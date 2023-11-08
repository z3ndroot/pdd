from . import Base
from sqlalchemy import (
    Column,
    String,
    Date)


class Driver(Base):
    driver_name = Column(String(100), nullable=False)
    driver_license_number = Column(String(100), nullable=False, unique=True)
    driver_address = Column(String(100), nullable=False)
    expiration_date = Column(Date, nullable=False)
