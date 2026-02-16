from datetime import datetime

from sqlalchemy import Column, DateTime, String, Boolean, Integer, ForeignKey, Float
from sqlalchemy.orm import Mapped, relationship, mapped_column

from ..db.database import Base


class Budget(Base):
    __tablename__ = 'budgets'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    limit_amount: Mapped[float] = mapped_column(Float, nullable=False)
    month: Mapped[str] = mapped_column(String(255), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow())
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship(back_populates='budgets')
