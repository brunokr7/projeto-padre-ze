from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Operador(Base):
    __tablename__ = "operadores"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    nome = Column(String(100), nullable=False)

class Beneficiario(Base):
    __tablename__ = "beneficiarios"

    id = Column(Integer, primary_key=True, index=True)
    cpf = Column(String(14), unique=True, index=True, nullable=False)
    nome_completo = Column(String(150), nullable=False)
    endereco = Column(Text, nullable=False)
    membros_familia = Column(Integer, nullable=False)
    
    atendimentos = relationship("Atendimento", back_populates="beneficiario")

class Atendimento(Base):
    __tablename__ = "atendimentos"

    id = Column(Integer, primary_key=True, index=True)
    beneficiario_id = Column(Integer, ForeignKey("beneficiarios.id"), nullable=False)
    tipo_auxilio = Column(String(100), nullable=False)
    observacoes = Column(Text, nullable=True)
    data_atendimento = Column(DateTime, default=datetime.utcnow)

    beneficiario = relationship("Beneficiario", back_populates="atendimentos")
