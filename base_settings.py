import json

from models import Base, Driver, Car, Fine, Violation
from sqlalchemy.orm import Session as SessionType


def open_json(path: str, key: str) -> list[dict]:
    with open(path, 'r', encoding="UTF8") as f:
        result = json.load(f)

    return result[key]


def create_user(session: SessionType, id: int,
                driver_name: str, driver_license_number, driver_address: str,
                expiration_date: str) -> Driver:
    user = Driver(id=id, driver_name=driver_name,
                  driver_license_number=driver_license_number,
                  driver_address=driver_address, expiration_date=expiration_date)
    session.add(user)
    session.commit()

    return user


def create_car(session: SessionType, id: int, car_make: str, car_model: str,
               car_year: str, car_color: str, car_number: str, driver_id: int):
    car = Car(id=id, car_make=car_make, car_model=car_model,
              car_year=car_year, car_color=car_color, car_number=car_number, driver_id=driver_id)
    session.add(car)
    session.commit()


def create_fine(session: SessionType, id: int, fine_type: str, fine_amount: int, fine_date: str, fine_count: int,
                car_id: int):
    fine = Fine(id=id, fine_type=fine_type, fine_amount=fine_amount, fine_date=fine_date, fine_count=fine_count,
                car_id=car_id)
    session.add(fine)
    session.commit()


def create_violation(session: SessionType, id: int, violation_type: str, violation_description: str,
                     violation_city: str, violation_date: str,
                     violation_area: str, fine_id: int):
    violation = Violation(id=id, violation_type=violation_type, violation_description=violation_description,
                          violation_city=violation_city, violation_date=violation_date, violation_area=violation_area,
                          fine_id=fine_id)
    session.add(violation)
    session.commit()


def create_all(session: SessionType):
    drivers = open_json("driver.json", 'drivers')
    cars = open_json("car.json", 'car')
    fines = open_json("fine.json", 'fine')
    violations = open_json('violation.json', "violations")
    for i in drivers:
        create_user(**i, session=session)

    for i in cars:
        create_car(**i, session=session)

    for i in fines:
        create_fine(**i, session=session)

    for i in violations:
        create_violation(**i, session=session)
