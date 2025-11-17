# Projeto: Detecção de Invasão de Rede com Machine Learning

Este projeto tem como objetivo construir um modelo de machine learning de alta precisão para a detecção de intrusões em redes de computadores. O modelo é treinado para classificar o tráfego de rede como `normal` ou `anomalia` (ataque), com base em um conjunto de features extraídas dos pacotes de dados.

**Autor:** Vinicius Cantanhede dos Santos

---

## 1. Contexto do Projeto

Este é o segundo projeto desenvolvido como parte do curso **[Inteligência Artificial para Segurança Cibernética](https://www.datascienceacademy.com.br/course/inteligencia-artificial-para-seguranca-cibernetica)** da Data Science Academy. O objetivo é aplicar técnicas de classificação supervisionada para identificar atividades maliciosas em um grande volume de tráfego de rede, um desafio central na cibersegurança moderna.

O modelo utiliza o dataset KDD Cup '99 (ou similar), que contém uma vasta gama de conexões de rede rotuladas como normais ou como parte de um ataque.

## 2. Metodologia

O projeto está contido no notebook `Prevendo-Invasoes.ipynb` e segue um fluxo completo de ciência de dados, desde a preparação até o deploy.

### 2.1. Análise e Preparação dos Dados

1.  **Carga de Dados**: O modelo foi treinado com `dados_treino.csv` (125.973 registros) e avaliado com `dados_teste.csv` (22.544 registros), ambos com 42 colunas.
2.  **Limpeza de Duplicatas**: Foram identificadas e removidas 59.963 linhas duplicadas do conjunto de treino para evitar viés no modelo.
3.  **Análise Exploratória (EDA)**: Foi verificado que não havia dados ausentes. A variável alvo `classe` (Normal vs. Anomalia) mostrou-se desbalanceada, um ponto de atenção comum em datasets de detecção de fraude ou intrusão.

### 2.2. Pré-processamento e Feature Engineering

1.  **Label Encoding**: As features categóricas (`protocol_type`, `service`, `flag`) e a variável alvo (`classe`) foram convertidas em representações numéricas usando `LabelEncoder`. Os encoders de features foram salvos para serem usados no deploy.
2.  **Feature Scaling**: Todas as features preditoras (numéricas e categóricas codificadas) foram normalizadas usando `MinMaxScaler`. O scaler também foi salvo para garantir que os novos dados de deploy sejam processados da mesma forma.

### 2.3. Modelagem e Otimização

1.  **Seleção de Modelo**: Foram testados quatro algoritmos de classificação distintos:
    * Random Forest Classifier (Acurácia: 99.80%)
    * Decision Tree Classifier
    * K-Nearest Neighbors (KNN)
    * Gaussian Naive Bayes

    O **Random Forest Classifier** foi selecionado como o modelo base devido à sua performance superior.

2.  **Otimização de Hiperparâmetros**: Foi utilizado `GridSearchCV` para encontrar a melhor combinação de hiperparâmetros para o `RandomForestClassifier`, focando em `n_estimators`, `max_depth`, `min_samples_leaf` e `min_samples_split`.

3.  **Melhores Parâmetros**: `{'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 100}`.

## 3. Resultados

O modelo final, treinado com os hiperparâmetros otimizados, alcançou uma performance excepcional nos dados de teste.

* **Acurácia Final**: **89.3%**

O desempenho detalhado, incluindo a **Matriz de Confusão** e o **Relatório de Classificação**, pode ser encontrado no final do notebook. Os resultados mostram uma capacidade extremamente alta de identificar corretamente tanto o tráfego normal quanto as anomalias, com altíssima precisão e recall.