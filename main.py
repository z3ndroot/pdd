from models import Base, Session
from sqlalchemy.orm import Session as SessionType
from base_settings import create_all
from fastapi import FastAPI
from step3.get_info_views import router as step3_router
import uvicorn

app = FastAPI()
app.include_router(step3_router)


@app.get("/")
def hello_index():
    return {"message": "Hello index!"}


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


def main():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    session: SessionType = Session
    create_all(session)
    session.close()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=5000)
