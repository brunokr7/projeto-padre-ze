# SGPD – Sistema de Gestão e Triagem Operacional
**Instituição Beneficente Padre Zé**

---

## 📌 Visão Geral
O **SGPD** é um MVP de software desenvolvido por **Bruno** para otimizar o fluxo de triagem e o atendimento social na Instituição Beneficente Padre Zé. O sistema foca em eficiência operacional, segurança de dados e acessibilidade digital (WCAG 2.1 AA), sustentando diretamente os objetivos da **Meta 2.1 do ODS 2 (Fome Zero e Agricultura Sustentável)**.

## 👥 Equipe e Validação
* **Desenvolvedor / Responsável Técnico:** Bruno
* **Representante / Coordenadora Parceira:** Maria da Silva Oliveira (Coordenadora de Atendimento Social e Recepção)

## 🛠️ Stack Tecnológica
* **Backend:** FastAPI, Python, Pydantic, SQLAlchemy, Uvicorn, Bcrypt
* **Banco de Dados:** SQLite (configurado para operação offline robusta)
* **Frontend:** HTML5, Tailwind CSS, JavaScript (com componentes dinâmicos de acessibilidade e alertas)

## 📂 Estrutura do Projeto
* `database.py`: Conexão e gestão de sessão SQLAlchemy com SQLite.
* `models.py`: Modelos relacionais (Operador, Beneficiário, Histórico de Atendimentos).
* `schemas.py`: Schemas Pydantic para validação rigorosa de dados de entrada e saída.
* `main.py`: Endpoints da API (autenticação, consultas por CPF, gestão de cadastros e triagem).
* `index.html`: Interface web adaptada com recursos de acessibilidade e usabilidade humanizada.

## 🚀 Principais Funcionalidades e Aprimoramentos Pós-Validação
* **Triagem Ágil de Beneficiários:** Consulta rápida por CPF, registro de vulnerabilidade e histórico social integrado.
* **Acessibilidade Completa (WCAG 2.1 AA):** Modo de alto contraste, tipografia ampliada e suporte a navegação assistida.
* **Melhorias de Usabilidade (UI/UX):** 
  * Barra de ações fixa (*Sticky Action Bar*) em formulários extensos para evitar atrito no preenchimento.
  * Notificações flutuantes (*Toast Notifications*) posicionadas na zona de foco visual imediato do operador.
* **Operação Offline Dedicada:** Base de dados local otimizada para garantir estabilidade mesmo em cenários de instabilidade de rede na instituição.
