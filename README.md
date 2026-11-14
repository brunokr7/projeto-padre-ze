# SGPD — Sistema de Gestão e Triagem Operacional
**Instituição Beneficente Padre Zé**

## Visão Geral
O SGPD é um MVP desenvolvido para otimizar a triagem e o atendimento social, garantindo eficiência, segurança e acessibilidade (WCAG 2.1 AA), alinhado à Meta 2.1 do ODS 2.

## Stack Tecnológica
- **Backend:** FastAPI, Python, Pydantic, SQLAlchemy, Bcrypt
- **Banco de Dados:** PostgreSQL
- **Frontend:** HTML5, Tailwind CSS

## Estrutura do Projeto
- `database.py`: Conexão e sessão SQLAlchemy com PostgreSQL.
- `models.py`: Modelos relacionais (Operador, Beneficiário, Atendimento).
- `schemas.py`: Schemas Pydantic para validação de entrada e saída.
- `main.py`: Endpoints da API (login, consulta por CPF, cadastro e registro de triagem).
- `index.html`: Interface web prototipada com as 3 telas principais.
* Atualização para validação de Pull Request