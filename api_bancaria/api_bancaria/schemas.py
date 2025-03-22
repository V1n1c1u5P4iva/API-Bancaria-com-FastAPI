from pydantic import BaseModel
from datetime import datetime


class TransacaoBase(BaseModel):
    valor: float
    tipo: str 
    conta_id: int


class TransacaoCreate(TransacaoBase):
    pass


class Transacao(TransacaoBase):
    id: int
    data: datetime

    
    class Config:
        from_attributes = True


class ContaBase(BaseModel):
    nome: str


class ContaCreate(ContaBase):
    pass


class Conta(ContaBase):
    id: int
    saldo: float
    transacoes: list[Transacao] = []

    class Config:
        from_attributes = True
