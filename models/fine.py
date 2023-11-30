from . import Base
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Date)

from sqlalchemy.orm import relationship


class Fine(Base):
    fine_type = Column(String(100), nullable=False)
    fine_amount = Column(Integer, nullable=False)
    fine_date = Column(Date, nullable=False)
    fine_count = Column(Integer, nullable=False)
    car_id = Column(Integer, ForeignKey('pdd_cars.id'), nullable=False, unique=False)

    cars = relationship('Car', back_populates='fine')
    violation = relationship('Violation', back_populates='fine')

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"fine_type={self.fine_type}, "
            f"fine_amount={self.fine_amount}, "
            f"fine_date={self.fine_date}, "
            f"fine_count={self.fine_count}"
            f")"
        )