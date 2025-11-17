# 🔎 Detecção de Transações Fraudulentas em Base de Dados Desbalanceada

Este projeto aborda o problema de **detecção de fraudes** em transações financeiras usando técnicas de *Machine Learning*, com foco especial no tratamento de **bases de dados extremamente desbalanceadas**.  
Mais de **98% das transações são normais**, enquanto menos de **2% representam fraudes**, tornando o aprendizado supervisionado tradicional ineficiente sem técnicas adicionais.

---

## 📌 Objetivo

O objetivo do projeto é:

- Analisar um dataset altamente desbalanceado  
- Testar estratégias para lidar com esse cenário  
- Treinar modelos capazes de identificar transações fraudulentas  
- Comparar técnicas de balanceamento e algoritmos especializados  

---

## 🔍 O Desafio: Classes Extremamente Desbalanceadas

Modelos de classificação tradicionais tendem a **ignorar a classe minoritária** quando a diferença é muito grande.  
Com 98% de transações normais, um modelo pode acertar 98% das previsões apenas classificando tudo como "normal" — mas isso é inútil, pois **não detecta fraudes**.

Para resolver isso, foram aplicadas duas abordagens:

---

# 🛠️ 1. Algoritmos Específicos para Datasets Desbalanceados

Alguns algoritmos de classificação conseguem lidar melhor com bases desbalanceadas sem necessidade de alterar os dados.

Entre as estratégias utilizadas:

### ✅ *Class Weight*
Algoritmos como **Logistic Regression**, **Random Forest**, **SVM** e **XGBoost** permitem ajustar pesos das classes:

- Classe normal → peso menor  
- Classe fraudulenta → peso maior  

Isso força o modelo a prestar mais atenção nos exemplos raros.

### ✅ *Anomaly Detection Algorithms*
Técnicas projetadas para identificar padrões anômalos, como:

- Isolation Forest  
- LOF (Local Outlier Factor)  

São úteis quando as fraudes são extremamente raras e bem diferentes do padrão normal.

---

# 🛠️ 2. Balanceamento de Dados com SMOTE

A segunda abordagem foi o uso de técnicas de *oversampling*, especialmente o **SMOTE (Synthetic Minority Over-sampling Technique)**.

### 🔬 Como o SMOTE funciona?

- Ele identifica exemplos da classe minoritária  
- Gera **novas amostras sintéticas** interpolando entre vizinhos próximos  
- Aumenta o número de fraudes até equilibrar o dataset  

Diferente de duplicar dados, o SMOTE cria novos exemplos “intermediários”, ajudando o modelo a aprender padrões mais robustos.

### 📌 Vantagens:

- Melhora recall e F1-score  
- Reduz overfitting comparado com oversampling simples  
- Facilita aprendizado de modelos como Random Forest e Gradient Boosting  

---

## ⚙️ Pipeline do Projeto

1. **Carregamento e análise inicial do dataset**  
2. **Verificação do nível de desbalanceamento**  
3. **Treinamento com algoritmos que utilizam `class_weight`**  
4. **Aplicação do SMOTE para gerar novas instâncias da classe fraudulenta**  
5. **Treinamento de modelos balanceados**  
6. **Avaliação com métricas adequadas**:  
   - Recall  
   - Precision  
   - F1-score  
   - Matriz de confusão  
   - ROC-AUC  

---

## 📈 Resultados e Comparação

- O uso apenas de *class weights* melhora o recall da classe fraudulenta sem alterar os dados.  
- O SMOTE aumenta significativamente a capacidade do modelo de identificar fraudes, especialmente para algoritmos baseados em árvores.  
- No geral, usar **SMOTE + Random Forest** oferece os melhores resultados em datasets altamente desbalanceados.

---

## ▶️ Como Executar

```bash
pip install -r requirements.txt
jupyter notebook Projeto5.ipynb
