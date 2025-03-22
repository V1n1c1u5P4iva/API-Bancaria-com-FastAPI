from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, crud
from ..database import SessionLocal, engine
from api_bancaria.endpoints.auth import verificar_token

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/contas/", response_model=schemas.Conta)
def criar_conta(conta: schemas.ContaCreate, db: Session = Depends(get_db), token: dict = Depends(verificar_token)):
   
    return crud.criar_conta(db=db, conta=conta)


@router.post("/transacoes/", response_model=schemas.Transacao)
def criar_transacao(transacao: schemas.TransacaoCreate, db: Session = Depends(get_db), token: dict = Depends(verificar_token)):
    if transacao.valor <= 0:
        raise HTTPException(status_code=400, detail="Valor deve ser positivo")
    db_conta = crud.get_conta(db, conta_id=transacao.conta_id)
    if not db_conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    if transacao.tipo == "saque" and db_conta.saldo < transacao.valor:
        raise HTTPException(status_code=400, detail="Saldo insuficiente")
    crud.atualizar_saldo_conta(db, transacao.conta_id, transacao.valor, transacao.tipo)
    return crud.criar_transacao(db=db, transacao=transacao)


@router.get("/contas/{conta_id}/extrato", response_model=list[schemas.Transacao])
def ler_extrato(conta_id: int, db: Session = Depends(get_db), token: dict = Depends(verificar_token)):
    db_conta = crud.get_conta(db, conta_id=conta_id)
    if not db_conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return db_conta.transacoes