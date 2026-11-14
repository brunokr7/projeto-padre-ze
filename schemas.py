from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class LoginRequest(BaseModel):
    email: EmailStr
    senha: str

class BeneficiarioCreate(BaseModel):
    cpf: str
    nome_completo: str
    endereco: str
    membros_familia: int
    tipo_auxilio: str
    observacoes: Optional[str] = "Entregue"

class AtendimentoResponse(BaseModel):
    id: int
    tipo_auxilio: str
    observacoes: Optional[str]
    data_atendimento: datetime

    class Config:
        from_attributes = True

class BeneficiarioResponse(BaseModel):
    id: int
    cpf: str
    nome_completo: str
    endereco: str
    membros_familia: int
    atendimentos: List[AtendimentoResponse] = []

    class Config:
        from_attributes = True
