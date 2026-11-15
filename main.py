from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
import bcrypt

from database import engine, get_db
import models
import schemas

# Criação automática das tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SGPD - Sistema de Gestão e Triagem Operacional",
    description="API FastAPI para suporte à Instituição Beneficente Padre Zé (ODS 2)",
    version="1.0.0"
)

# Rota raiz para carregar a interface web moderna (index.html)
@app.get("/", response_class=HTMLResponse)
async def read_root():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>Erro: O ficheiro index.html não foi encontrado na raiz do repositório.</h1>"

def hash_senha(senha: str) -> str:
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verificar_senha(senha: str, hashed: str) -> bool:
    return bcrypt.checkpw(senha.encode('utf-8'), hashed.encode('utf-8'))

@app.post("/api/login", status_code=status.HTTP_200_OK)
def login(dados: schemas.LoginRequest, db: Session = Depends(get_db)):
    operador = db.query(models.Operador).filter(models.Operador.email == dados.email).first()
    if not operador or not verificar_senha(dados.senha, operador.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas. Verifique e-mail e senha."
        )
    return {"mensagem": "Autenticação realizada com sucesso", "nome": operador.nome}

@app.get("/api/beneficiarios/{cpf}", response_model=schemas.BeneficiarioResponse)
def consultar_beneficiario(cpf: str, db: Session = Depends(get_db)):
    beneficiario = db.query(models.Beneficiario).filter(models.Beneficiario.cpf == cpf).first()
    if not beneficiario:
        raise HTTPException(status_code=404, detail="Beneficiário não encontrado.")
    return beneficiario
