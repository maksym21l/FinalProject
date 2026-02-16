from datetime import datetime

from sqlalchemy import Column, DateTime, String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column

from ..db.database import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f'<User {self.username}>'

    def __str__(self):
        return self.username