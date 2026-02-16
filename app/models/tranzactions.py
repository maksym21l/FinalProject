from datetime import datetime

from sqlalchemy import DateTime, String, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from ..db.database import Base


class Tranzaction(Base):
    __tablename__ = 'tranzactions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    valyta: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow())
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship(back_populates='tranzactions')

    def __repr__(self):
        return f'<Tranzaction {self.id}>'