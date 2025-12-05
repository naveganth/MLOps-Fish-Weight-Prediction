# 🐟 Fish Weight Prediction - End-to-End MLOps

Este projeto é uma solução completa de Machine Learning para prever o peso de peixes com base em medidas físicas. O objetivo foi demonstrar boas práticas de MLOps, desde a engenharia de dados até o deploy de uma API escalável e interface de usuário.

## 🎯 O Desafio

Desenvolver um pipeline reprodutível para treinar um modelo de regressão (**XGBoost**), versionar artefatos e disponibilizar o modelo para inferência via API e Docker.

## 🏗 Arquitetura da Solução

O projeto está modularizado para garantir separação de responsabilidades:

- **Feature Pipeline:** Ingestão, limpeza e transformação dos dados (`src/feature_pipeline`).
- **Training Pipeline:** Treinamento do modelo XGBoost com rastreamento de métricas via MLflow (`src/training_pipeline`).
- **Inference:** API REST de alto desempenho com FastAPI.
- **Frontend:** Interface interativa com Streamlit para testes manuais.
- **Infraestrutura:** Containerização com Docker e automação via Makefile.
- **CI/CD:** Pipeline de testes automatizados via GitHub Actions.

## 📂 Estrutura do Projeto

```text
├── .github/workflows  # Pipeline de CI (Testes e Build)
├── data/              # Dados brutos e processados
├── models/            # Artefatos do modelo (.pkl)
├── src/
│   ├── api/           # Código da API (FastAPI)
│   ├── feature_.../   # Scripts de processamento
│   ├── training_.../  # Scripts de treino e tuning
│   └── app.py         # Frontend Streamlit
├── tests/             # Testes unitários e de integração
├── Dockerfile         # Configuração da imagem da API
├── Makefile           # Comandos rápidos de execução
└── pyproject.toml     # Dependências (gerenciado pelo uv)
```

## 🚀 Como Executar

### Pré-requisitos

- **Docker** (Recomendado para execução isolada)
- Ou **Python 3.11+** com `uv` instalado para execução local.

---

### Opção 1: Via Docker (Recomendado 🐳)

Esta opção sobe a API pronta para uso sem instalar nada no seu Python local.

**1. Construir e Rodar a API:**
Isso irá construir a imagem, remover containers antigos e iniciar a API na porta 8000.

```bash
make docker-auto
```

**2. Testar a API:**

- Acesse a documentação interativa (Swagger): [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)
- Ou veja a seção **"Como Realizar a Inferência"** abaixo.

---

### Opção 2: Execução Local (Desenvolvimento)

Se preferir rodar os scripts manualmente:

**1. Instalar dependências:**

```bash
pip install uv
make install
```

**2. Treinar o Modelo:**
Executa o pipeline completo (Load -\> Preprocess -\> Feature Eng -\> Train). O modelo será salvo em `models/xgb_model.pkl` e as métricas registradas no MLflow.

```bash
make train
```

**3. Rodar a API:**

```bash
make run-api
```

**4. Rodar o Dashboard (Streamlit):**
Para visualizar uma interface gráfica amigável:

```bash
make run-app
```

- Acesse em: [http://localhost:8501](https://www.google.com/search?q=http://localhost:8501)

## 📡 Como Realizar a Inferência

A API aceita requisições POST no endpoint `/predict`. Abaixo estão exemplos de como testar.

**Exemplo de Payload (JSON):**

```json
[
  {
    "Species": "Perch",
    "Length1": 20.0,
    "Length2": 22.0,
    "Length3": 23.5,
    "Height": 5.5,
    "Width": 3.3
  }
]
```

**Comando cURL:**

```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '[{"Species": "Perch", "Length1": 20.0, "Length2": 22.0, "Length3": 23.5, "Height": 5.5, "Width": 3.3}]'
```

**Resposta Esperada:**

```json
{
  "predictions": [245.32]
}
```

## ✅ Checklist de Entregas

### Requisitos Obrigatórios

- [x] **Python + ML:** Modelo XGBoost treinado com separação clara de pipelines.
- [x] **Pipeline de MLOps:** Versionamento de modelos com MLflow e scripts modulares.
- [x] **Deploy:** API servida via Container Docker.
- [x] **README:** Documentação completa da arquitetura e execução.

### Diferenciais Implementados (Opcionais)

- [x] **Testes Unitários:** Cobertura de testes com pytest (API, Schema e Inferência).
- [x] **CI/CD:** Pipeline no GitHub Actions para testes e build automático.
- [x] **Makefile:** Automação de comandos para facilitar a execução.
- [x] **Model Registry:** Integração com MLflow para rastreamento de experimentos.
- [x] **Visualização:** Aplicação Fullstack com Streamlit.

## 🔮 Possíveis Melhorias

Pontos identificados para evolução futura do projeto:

- **Monitoramento de Drift:** Integração com EvidentlyAI para alertar se os peixes na inferência tiverem medidas muito diferentes do treino.
- **Deploy em Cloud:** Configuração de deploy contínuo (CD) para AWS ECS ou Lambda utilizando Terraform.
- **Feature Store:** Para um cenário com milhões de registros, implementar uma Feature Store (ex: Feast) para servir features pré-calculadas.
- **Autenticação:** Adicionar camada de segurança (OAuth2) na API.

---

**Autor:** [Seu Nome]

---
