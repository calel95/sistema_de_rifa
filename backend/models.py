#representacao do banco de dados
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from .database import Base

class RegisterModel(Base):
    __tablename__ = 'sorteio'
    #id = Column(Integer, primary_key=True, index=True, autoincrement="false")
    nome = Column(String)
    numero = Column(Integer, primary_key=True, index=True, autoincrement="false")
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated = Column(Boolean)
    update_date = Column(DateTime)