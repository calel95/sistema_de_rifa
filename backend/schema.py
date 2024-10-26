from pydantic import BaseModel, PositiveFloat, EmailStr, validator, Field
from enum import Enum
from datetime import datetime
from typing import Optional

class RegisterBase(BaseModel):
    numero: int
    nome: str


    class Config:
        from_attributes = True

class RegisterGet(RegisterBase):
    id: int
    created_at: datetime
    updated: bool | None = None
    update_date: datetime | None

    class Config:
        from_attributes = True

class RegisterUpdate(BaseModel):
    numero: Optional[int] = None
    nome: Optional[str] = None