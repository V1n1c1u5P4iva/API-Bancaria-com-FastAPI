from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


class Conta(Base):
    __tablename__ = "contas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    saldo = Column(Float, default=0.0)
    transacoes = relationship("Transacao", back_populates="conta")


class Transacao(Base):
    __tablename__ = "transacoes"
    id = Column(Integer, primary_key=True, index=True)
    valor = Column(Float)
    tipo = Column(String) 
    data = Column(DateTime, default=datetime.utcnow)
    conta_id = Column(Integer, ForeignKey("contas.id"))
    conta = relationship("Conta", back_populates="transacoes")
