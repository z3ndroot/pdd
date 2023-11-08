from sqlalchemy import (
    create_engine,
    Column,
    Integer
)
from sqlalchemy.orm import (
    declarative_base,
    declared_attr,
    sessionmaker,
    scoped_session,
)
import config_db


class Base:
    @declared_attr
    def __tablename__(cls):
        """
        :return:
        """
        return f"pdd_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True, nullable=False)

    def __repr__(self):
        return str(self)


engine = create_engine(config_db.DB_URL, echo=True)
Base = declarative_base(bind=engine, cls=Base)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
