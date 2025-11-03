# Inteligência Artificial para Segurança Cibernética


Repositório dedicado aos projetos desenvolvidos durante o curso **[Inteligência Artificial para Segurança Cibernética](https://www.datascienceacademy.com.br/course/inteligencia-artificial-para-seguranca-cibernetica)** da Data Science Academy. O objetivo é aplicar conceitos de IA e Machine Learning para resolver desafios no domínio da cibersegurança.

---

# Projetos Desenvolvidos

# Projeto 1:  Detecção de URL de Phishing (ClassificacaoPhishing)

Este projeto tem como objetivo construir um modelo de machine learning capaz de classificar URLs como legítimas ou maliciosas (phishing), atendendo à necessidade de uma empresa de e-commerce que deseja proteger seus usuários de anúncios com links perigosos.

#### Contexto

Uma empresa de e-commerce implementou um sistema de banners de anúncios onde terceiros podem inserir links. Para mitigar o risco de direcionar usuários a sites maliciosos, foi desenvolvido um modelo preditivo que analisa as características de uma URL e a classifica como segura ou como uma tentativa de phishing.

#### Metodologia

O desenvolvimento do modelo seguiu um pipeline completo de Machine Learning, documentado no notebook `Modelagem.ipynb`:

1.  **Análise e Limpeza de Dados**:
    * O dataset inicial continha 10.000 amostras e 32 colunas.
    * A coluna `indice`, que não possuía valor preditivo, foi removida.
    * Foram identificadas e removidas 4.611 linhas duplicadas, resultando em um conjunto de dados mais robusto com 5.389 amostras.

2.  **Engenharia e Seleção de Features**:
    * Foi realizada uma **análise de multicolinearidade** para identificar features com alta correlação (acima de 0.8).
    * Para evitar redundância e simplificar o modelo, as features `favicon` e `redirecionamento_double_slash` foram removidas.
    * **PCA (Análise de Componentes Principais)** foi aplicado para reduzir a dimensionalidade. Com o auxílio de `GridSearchCV`, determinou-se que **26 componentes principais** ofereciam a melhor performance, explicando a maior parte da variância dos dados originais.

3.  **Modelagem e Otimização**:
    * O problema foi abordado como uma classificação binária, utilizando a **Regressão Logística**.
    * Foram testadas múltiplas versões do modelo, incluindo uma baseline sem PCA e outras com diferentes números de componentes.
    * Um `GridSearchCV` foi executado para **otimização de hiperparâmetros**, resultando na seguinte configuração para o modelo final: `{'C': 0.1, 'penalty': 'l2', 'solver': 'newton-cg'}`.

#### Resultados

O modelo final alcançou uma **acurácia de 92,5%** nos dados de teste, demonstrando alta eficácia na distinção entre URLs legítimas e de phishing. A performance detalhada, incluindo precisão e recall para cada classe, pode ser consultada no final do notebook `Modelagem.ipynb`.

-----

# Projeto 2: Detecção de Invasão de Rede com Machine Learning

Este projeto tem como objetivo construir um modelo de machine learning de alta precisão para a detecção de intrusões em redes de computadores. O modelo é treinado para classificar o tráfego de rede como `normal` ou `anomalia` (ataque), com base em um conjunto de features extraídas dos pacotes de dados.


### Contexto do Projeto

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

### 3. Resultados

O modelo final, treinado com os hiperparâmetros otimizados, alcançou uma performance excepcional nos dados de teste.

* **Acurácia Final**: **89.3%**

O desempenho detalhado, incluindo a **Matriz de Confusão** e o **Relatório de Classificação**, pode ser encontrado no final do notebook. Os resultados mostram uma capacidade extremamente alta de identificar corretamente tanto o tráfego normal quanto as anomalias, com altíssima precisão e recall.

----
