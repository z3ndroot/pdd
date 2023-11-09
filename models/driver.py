from . import Base
from sqlalchemy import (
    Column,
    String,
    Date)
from sqlalchemy.orm import relationship


class Driver(Base):
    driver_name = Column(String(100), nullable=False)
    driver_license_number = Column(String(100), nullable=False, unique=True)
    driver_address = Column(String(100), nullable=False)
    expiration_date = Column(Date, nullable=False)

    cars = relationship('Car', back_populates='driver')

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"driver_name={self.driver_name}, "
            f"driver_license_number={self.driver_license_number}, "
            f"driver_address={self.driver_address}, "
            f"expiration_date={self.expiration_date} "
            f")"
        )
