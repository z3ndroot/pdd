from . import Base

from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Date)

from sqlalchemy.orm import relationship


class Violation(Base):
    violation_type = Column(String(100), nullable=False)
    violation_description = Column(String(100), nullable=False)
    violation_city = Column(String(100), nullable=False)
    violation_date = Column(Date, nullable=False)
    violation_area = Column(String(100), nullable=False)
    fine_id = Column(Integer, ForeignKey('pdd_fines.id'), nullable=False, unique=False)

    fine = relationship('Fine', back_populates='violation')

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
