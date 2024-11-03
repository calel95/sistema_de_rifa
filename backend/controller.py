from sqlalchemy.orm import Session
from sqlalchemy.sql import func, text
from . import schema
from . import models

def get_registers(db:Session):
    return db.query(models.RegisterModel).all()

def get_register(db:Session, register_id: int):
    return db.query(models.RegisterModel).filter(models.RegisterModel.numero == register_id).first()


def create_register(db: Session ,register:schema.RegisterBase):
    numero = register.numero
    valida_numero = db.query(models.RegisterModel).filter(models.RegisterModel.numero == numero).first()
    if valida_numero:
        print("ja tem")
    else:
        db_rifa = models.RegisterModel(**register.model_dump())
        db.add(db_rifa)
        db.commit()
        db.refresh(db_rifa)
        return db_rifa

def update_register(db: Session,register_id: int, register: schema.RegisterUpdate):
    db_rifa = db.query(models.RegisterModel).filter(models.RegisterModel.numero == register_id).first()

    if db_rifa is None:
        return None
    if register.numero is not None:
        db_rifa.numero = register.numero
    if register.numero is None:
        db_rifa.numero = db_rifa.numero
    if register.nome is not None:
        db_rifa.nome = register.nome
    if register.nome is None:
        db_rifa.nome = db_rifa.nome
    db_rifa.updated = True
    db_rifa.update_date = func.now()
    db.commit()
    db.refresh(db_rifa)
    return db_rifa


def delete_register(db: Session, register_id: int):
    db_rifa = db.query(models.RegisterModel).filter(models.RegisterModel.numero == register_id).first()
    if db_rifa is None:
        return None
    db.delete(db_rifa)
    db.commit()
    return db_rifa

def inserir_numeros_em_massa(db: Session):
    numeros = [{"numero": i} for i in range(1, 1001)]
    db.bulk_insert_mappings(models.RegisterModel,numeros)
    db.commit()
    return {"mensagem": "Inserção de números concluída com sucesso!"} 
    
def delete_truncate(db:Session):
    db.execute(text("truncate sorteio"))
    db.commit()
    return {"mensagem": "tabela truncada com sucesso!"} 