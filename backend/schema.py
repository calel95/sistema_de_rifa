from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from typing import Optional

class Register1000(BaseModel):
    numero: Optional[int] = None

class RegisterBase(BaseModel):
    #id: int
    numero: Optional[int] = None
    nome: Optional[str] = None


    class Config:
        from_attributes = True

class RegisterGet(RegisterBase):
    #id: int
    created_at: datetime
    updated: bool | None = None
    update_date: datetime | None

    class Config:
        from_attributes = True

class RegisterUpdate(BaseModel):
    numero: Optional[int] = None
    nome: Optional[str] = None