from fastapi import APIRouter
from .get_info import step_3_work
from models import Session

router = APIRouter(prefix="/homework", tags=['Step3'])


@router.post('/{car_number}/')
def get_info(car_number='AB1234CD'):
    session: Session = Session
    result = step_3_work(session, car_number)
    session.close()
    return result
