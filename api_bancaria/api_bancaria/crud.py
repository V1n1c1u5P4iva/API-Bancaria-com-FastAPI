from sqlalchemy.orm import Session
from . import models, schemas


def get_conta(db: Session, conta_id: int):
    return db.query(models.Conta).filter(models.Conta.id == conta_id).first()


def criar_transacao(db: Session, transacao: schemas.TransacaoCreate):
    db_transacao = models.Transacao(**transacao.dict())
    db.add(db_transacao)
    db.commit()
    db.refresh(db_transacao)
    return db_transacao


def atualizar_saldo_conta(db: Session, conta_id: int, valor: float, tipo: str):
    conta = get_conta(db, conta_id)
    if tipo == "deposito":
        conta.saldo += valor
    elif tipo == "saque":
        conta.saldo -= valor
    db.commit()
    db.refresh(conta)
    return conta

def criar_conta(db: Session, conta: schemas.ContaCreate):
    db_conta = models.Conta(nome=conta.nome, saldo=0.0)  # Saldo inicial é 0.0
    db.add(db_conta)
    db.commit()
    db.refresh(db_conta)
    return db_conta