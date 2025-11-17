# 🔒 Detector de Ataques Botnet com IA

Sistema de detecção de ataques de botnet utilizando aprendizado semi-supervisionado com Flask para deploy web.

## 📋 Sobre o Projeto

Este projeto utiliza técnicas de **aprendizado semi-supervisionado** (Label Spreading) para identificar e prever ataques de botnet em redes, combinando dados rotulados e não rotulados para aumentar a precisão do modelo. O projeto inclui:

- Criação e análise exploratória de dados sintéticos
- Pré-processamento e normalização de features
- Treinamento de modelo com algoritmo Label Spreading
- Aplicação web Flask para detecção em tempo real
- Interface HTML intuitiva para entrada de dados

## 🎯 Características do Sistema

O modelo analisa 5 características principais do tráfego de rede:

- **Tráfego**: Volume de dados trafegados (em bytes)
- **Duração da Conexão**: Tempo de duração da conexão (em segundos)
- **Número de Pacotes**: Quantidade de pacotes transmitidos
- **Bytes Transferidos**: Total de bytes transferidos
- **Número de Erros**: Quantidade de erros durante a transmissão

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **Flask**: Framework web para deploy
- **scikit-learn**: Algoritmo Label Spreading para aprendizado semi-supervisionado
- **Pandas & NumPy**: Manipulação e análise de dados
- **Matplotlib & Seaborn**: Visualização de dados
- **Joblib**: Serialização de modelos

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos para instalação

1. Clone o repositório ou baixe os arquivos do projeto

2. Navegue até o diretório do projeto:
```bash
cd 7.PrevendoBotNet
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 💻 Como Usar

### 1. Treinamento do Modelo

Abra e execute o notebook `projeto7.ipynb` para:
- Gerar o dataset sintético
- Realizar análise exploratória
- Treinar o modelo Label Spreading
- Salvar o modelo e o scaler na pasta `modelos/`

### 2. Executar a Aplicação Web

```bash
python deploy.py
```

A aplicação estará disponível em: `http://127.0.0.1:5000`

### 3. Fazer Previsões

1. Acesse a interface web no navegador
2. Preencha os campos com os valores de tráfego de rede:
   - Tráfego (em bytes)
   - Duração da Conexão (em segundos)
   - Número de Pacotes
   - Bytes Transferidos
   - Número de Erros
3. Clique em "Prever"
4. O sistema retornará: **"Botnet Detectado"** ou **"Tráfego Normal"**

## 📊 Estrutura do Projeto

```
7.PrevendoBotNet/
│
├── deploy.py                 # Aplicação Flask para deploy
├── projeto7.ipynb           # Notebook com análise e treinamento
├── requirements.txt         # Dependências do projeto
│
├── modelos/
│   ├── scaler.pkl          # Scaler para normalização
│   └── botnet_detector_model.pkl  # Modelo treinado
│
└── templates/
    └── index.html          # Interface web
```

## 🧠 Sobre o Algoritmo Label Spreading

O **Label Spreading** é um algoritmo de aprendizado semi-supervisionado que:

- Utiliza tanto dados rotulados quanto não rotulados
- Propaga rótulos através da estrutura dos dados
- Explora similaridades entre exemplos
- É ideal quando há poucos dados rotulados disponíveis

### Vantagens
- Aproveita dados não rotulados para melhorar a precisão
- Reduz custos de rotulagem manual
- Captura estruturas complexas nos dados

## 📈 Métricas de Avaliação

O modelo é avaliado usando:
- **Acurácia**: Percentual de previsões corretas
- **Precision, Recall e F1-Score**: Métricas por classe
- **Matriz de Confusão**: Visualização de acertos e erros

## 🔍 Exemplo de Uso da API

```python
import requests
import json

url = 'http://127.0.0.1:5000/predict'
data = {
    'input': [1200, 45, 650, 950, 35]  # [trafego, duracao, pacotes, bytes, erros]
}

response = requests.post(url, json=data)
result = response.json()
print(f"Previsão: {result['prediction']}")  # 0 = Normal, 1 = Botnet
```

## 🎓 Contexto Educacional

Este projeto faz parte do **Curso Data Science Academy (DSA)** - Projeto 7, focado em aplicações práticas de Machine Learning para cibersegurança.

## ⚠️ Observações

- Os dados utilizados são **sintéticos** e gerados para fins educacionais
- Em um ambiente de produção, seria necessário treinar com dados reais de tráfego de rede
- O modelo deve ser retreinado periodicamente com novos padrões de ataque
- Considere adicionar autenticação e validação para uso em produção

## 📝 Licença

Este projeto é desenvolvido para fins educacionais.

## 👤 Autor

Desenvolvido como parte do Curso DSA

---

**Data Science Academy** | Projeto 7 - Prevenção de Ataques Botnet
