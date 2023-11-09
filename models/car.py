from . import Base
from sqlalchemy import (
    Column,
    String,
    Date,
    Integer,
    ForeignKey)

from sqlalchemy.orm import relationship


class Car(Base):
    car_make = Column(String(30), nullable=False)
    car_model = Column(String(100), nullable=False)
    car_year = Column(String(4), nullable=False)
    car_color = Column(String(20), nullable=False)
    car_number = Column(String(100), nullable=False, unique=True)
    driver_id = Column(Integer, ForeignKey('pdd_drivers.id'), nullable=False, unique=False)

    driver = relationship('Driver', back_populates='cars')
    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"car_make={self.car_make}, "
            f"car_model={self.car_model}, "
            f"car_year={self.car_year}, "
            f"car_color={self.car_number}, "
            f"car_number={self.car_number}"
            f")"
        )
