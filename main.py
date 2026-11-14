from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import bcrypt

from database import engine, get_db
import models
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SGPD - Sistema de Gestão e Triagem Operacional",
    description="API FastAPI para suporte à Instituição Beneficente Padre Zé (ODS 2)",
    version="1.0.0"
)

def hash_senha(senha: str) -> str:
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verificar_senha(senha: str, hashed: str) -> bool:
    return bcrypt.checkpw(senha.encode('utf-8'), hashed.encode('utf-8'))

@app.post("/api/login", status_code=status.HTTP_200_OK)
def login(dados: LoginRequest, db: Session = Depends(get_db)):
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

@app.post("/api/triagem", response_model=schemas.BeneficiarioResponse, status_code=status.HTTP_201_CREATED)
def cadastrar_e_registrar_atendimento(dados: schemas.BeneficiarioCreate, db: Session = Depends(get_db)):
    beneficiario = db.query(models.Beneficiario).filter(models.Beneficiario.cpf == dados.cpf).first()
    
    if not beneficiario:
        beneficiario = models.Beneficiario(
            cpf=dados.cpf,
            nome_completo=dados.nome_completo,
            endereco=dados.endereco,
            membros_familia=dados.membros_familia
        )
        db.add(beneficiario)
        db.commit()
        db.refresh(beneficiario)

    novo_atendimento = models.Atendimento(
        beneficiario_id=beneficiario.id,
        tipo_auxilio=dados.tipo_auxilio,
        observacoes=dados.observacoes
    )
    db.add(novo_atendimento)
    db.commit()
    
    db.refresh(beneficiario)
    return beneficiario
