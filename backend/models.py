#representacao do banco de dados
from sqlalchemy import Column, Integer, String, DateTime, Select, Boolean
from sqlalchemy.sql import func
from .database import Base

class RegisterModel(Base):
    __tablename__ = 'sorteio'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now(), index=True)
    updated = Column(Boolean, default=False)
    update_date = Column(DateTime)