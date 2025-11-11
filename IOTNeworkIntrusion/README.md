# 🔐 Detecção de Ameaças em Dispositivos IoT  
Análise de Dados Reais com o Dataset UNSW-NB15

Este projeto realiza uma análise completa sobre um conjunto de dados real utilizado para identificar **ataques cibernéticos em dispositivos IoT**. O foco principal é explorar os dados, tratar o desbalanceamento das classes e propor um modelo de **classificação multiclasse** capaz de detectar diferentes tipos de ameaças.

---

## 📌 Dataset Utilizado

Os dados utilizados são do **UNSW-NB15**, gerado por uma ferramenta que combina características modernas de tráfego de rede com simulações de ataques.  
Dataset disponível em:

- https://research.unsw.edu.au/projects/unsw-nb15-dataset

O dataset contém atividades normais e diversas categorias de ataques, como:

- **Fuzzers**
- **Analysis**
- **Backdoors**
- **DoS**
- **Exploits**
- **Generic**
- **Reconnaissance**
- **Shellcode**
- **Worms**

---

## 🧪 Objetivo

O objetivo do projeto é construir um modelo capaz de identificar qual tipo de ataque está ocorrendo, considerando que:

- Trata-se de um **problema de classificação multiclasse**
- Existe um **forte desbalanceamento entre as classes**
- Algumas classes possuem muitos exemplos, enquanto outras têm poucos dados

---

## 🧭 Etapas do Projeto

### 1. 📊 Análise Exploratória (EDA)
- Inspeção das variáveis do dataset  
- Identificação de padrões e comportamentos  
- Visualizações para entender a distribuição das classes  

---

### 2. ⚠️ Verificação do Desbalanceamento
Foi identificado um desbalanceamento severo entre as classes.  
Esse problema impacta diretamente o desempenho dos modelos, fazendo com que:

- As classes majoritárias dominem o aprendizado  
- O modelo apresente baixa performance nas classes com poucos exemplos  

---

### 3. 🛠️ Técnicas Consideradas para Tratar o Desbalanceamento
Para enfrentar esse desafio, duas abordagens principais foram analisadas:

#### **1️⃣ Algoritmos adequados para datasets desbalanceados**
Modelos que lidam melhor com esse tipo de distribuição, como:
- Random Forest com class_weight
- Árvores de decisão ajustadas

---

## 🤖 Modelagem
Após o tratamento dos dados, o projeto parte para:

- Preparação dos dados  
- Normalização/Padronização  
- Treinamento do modelo  
- Avaliação com métricas adequadas (precision, recall, F1-score, matriz de confusão)

---

## 🧾 Conclusões

Este projeto demonstra a importância de:
- Entender profundamente o dataset antes do treinamento  
- Considerar o desbalanceamento para modelos de classificação multiclasse  
- Testar diferentes técnicas de balanceamento e modelos para melhor performance  

Ele também fornece uma base sólida para estudos em:
- Segurança Cibernética  
- Machine Learning aplicado a redes  
- Modelagem com dados desbalanceados  



