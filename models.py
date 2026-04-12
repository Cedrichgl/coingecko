from sqlalchemy import String, Integer, Column, Float
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Bourse(Base):
    __tablename__ = 'bourse'

    id: Mapped[str] = mapped_column(String, primary_key=True, index=True) 
    symbol: Mapped[str] = mapped_column(String, nullable=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    current_price: Mapped[float] = mapped_column(Float, nullable=True)
    market_cap: Mapped[float] = mapped_column(Float, nullable=True)
    total_volume: Mapped[float] = mapped_column(Float, nullable=True)
