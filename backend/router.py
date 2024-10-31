from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import database, schema, controller
from typing import List

router = APIRouter()

@router.get("/numeros/", response_model=List[schema.RegisterGet], description="Faz a leitura de todos os numeros armazenados no banco")
def read_all_registers(db: Session = Depends(database.get_db)):
    registers = controller.get_registers(db)
    return registers

@router.get("/numeros/{register_id}", response_model=schema.RegisterGet, description="Faz a leitura de um Registro")
def read_one_register(register_id: int, db: Session = Depends(database.get_db)):
    db_rifa = controller.get_register(db=db, register_id=register_id)
    if db_rifa is None:
        raise HTTPException(status_code=404, detail="Registro com o id {register_id} não encontrado")
    return db_rifa

@router.post("/numeros/", response_model=schema.RegisterBase, description="Faz a criação de um novo Registro")
def create_register(register: schema.RegisterBase ,db: Session = Depends(database.get_db)):
    db_rifa = controller.create_register(db=db,register=register)
    if db_rifa is None:
        raise HTTPException(status_code=404, detail="Registro com o numero ja existe")
    return db_rifa

@router.delete("/numeros/{register_id}", response_model=schema.RegisterGet, description="Faz a deleção de um Registro")
def delete_product(register_id: int, db: Session = Depends(database.get_db)):
    db_rifa = controller.delete_register(db=db,register_id=register_id)
    if db_rifa is None:
        raise HTTPException(status_code=404, detail="Registro com o id {register_id} não encontrado")
    return db_rifa

@router.put("/numeros/{register_id}",response_model=schema.RegisterGet, description="Faz a atualização de um Registro")
def update_products(register_id: int, register: schema.RegisterUpdate, db: Session = Depends(database.get_db)):
    db_rifa = controller.update_register(db=db, register_id=register_id, register=register)
    if db_rifa is None:
        raise HTTPException(status_code=404, detail="Registro com o id {register_id} não encontrado")
    return db_rifa