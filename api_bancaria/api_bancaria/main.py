from fastapi import FastAPI
from api_bancaria.endpoints import transacoes, auth
from api_bancaria.database import Base, engine

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(transacoes.router)
app.include_router(auth.router)  