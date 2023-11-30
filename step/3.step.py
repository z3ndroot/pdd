from models import Car, Fine, Violation
from sqlalchemy.orm import Session as SessionType


def step_3_work(session: SessionType, car_number):
    query = session.query(Violation.violation_type, Violation.violation_area, Fine.fine_date, Fine.fine_amount) \
        .join(Fine) \
        .join(Car) \
        .filter(Car.car_number == car_number).all()
    return query
