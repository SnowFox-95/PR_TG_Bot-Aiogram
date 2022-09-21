import datetime

from sqlalchemy import Column, Integer, VARCHAR, DATE
from .base import baseModel


class User(baseModel):
    __tablename__ = 'users'

    # TELEGRAM_USER_ID
    user_id = Column(Integer, unique=True, nullable=False, primary_key=True)

    # TELEGRAM_USER_NAME
    username = Column(VARCHAR(32), unique=False, nullable=True)

    # Registration date
    reg_date = Column(DATE, default=datetime.date.today())

    # Last update date
    upd_date = Column(DATE, onupdate=datetime.date.today())

    def __str__(self) -> str:
        return f"<User:(self.user_id)>"
