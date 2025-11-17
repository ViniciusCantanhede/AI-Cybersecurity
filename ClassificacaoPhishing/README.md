# Projeto: Detecção de URL de Phishing

Este projeto tem como objetivo construir um modelo de machine learning capaz de classificar URLs como legítimas ou maliciosas (phishing), atendendo à necessidade de uma empresa de e-commerce que deseja proteger seus usuários de anúncios com links perigosos.

**Autor:** Vinicius Cantanhede dos Santos

---

## 1. Contexto do Projeto

Uma empresa de comércio eletrônico que vende diversos produtos online está ativando a opção de banners de anúncios em seu website, que recebe milhares de visitantes diariamente. O novo sistema permite que anunciantes aluguem um banner por um período e insiram um link direcionando o usuário para seu próprio site.

A empresa está ciente de que algumas URLs de anúncios podem conter links maliciosos (phishing), enganando usuários, roubando informações confidenciais e, consequentemente, tornando a empresa responsável por eventuais prejuízos.

O objetivo deste projeto foi fornecer um modelo preditivo para analisar cada URL cadastrada pelos anunciantes e determinar se ela é propensa a phishing ou não.

## 2. Metodologia

O projeto foi dividido em duas etapas principais, detalhadas nos notebooks:

1.  `Modelagem.ipynb`: Contém todo o processo de análise exploratória, limpeza de dados, engenharia de features, treinamento, otimização e avaliação do modelo.
2.  `Deploy.ipynb`: Um notebook simples que demonstra como carregar os modelos treinados e utilizá-los para fazer previsões em novos dados.

### 2.1. Análise e Preparação dos Dados

O conjunto de dados inicial (`dados/dataset.csv`) continha 10.000 amostras e 32 colunas.

1.  **Limpeza Inicial**: A coluna `indice` foi removida por não ser relevante para a modelagem.
2.  **Tratamento de Duplicatas**: Foram identificadas e removidas 4.611 linhas duplicadas, resultando em um conjunto de dados limpo com 5.389 amostras únicas.
3.  **Análise de Valores**: Foi confirmado que todas as 30 features preditoras e a variável alvo (`resultado`) são categóricas, utilizando valores como `1`, `0` ou `-1`. Não foram encontrados valores nulos.
4.  **Variável Alvo**: A variável `resultado` possui duas classes:
    * `-1`: URL Legítima
    * `1`: URL de Phishing

### 2.2. Engenharia e Seleção de Features

1.  **Análise de Multicolinearidade**: Foi calculada uma matriz de correlação para identificar features altamente correlacionadas (limite > 0.8).
    * `favicon` e `pop_up_window` (Correlação: 0.93)
    * `redirecionamento_double_slash` e `servico_encurtamento` (Correlação: 0.81)
2.  **Remoção de Features**: Para reduzir a redundância, as features `favicon` e `redirecionamento_double_slash` foram removidas, restando 28 features preditoras.
3.  **Redução de Dimensionalidade (PCA)**: Para simplificar o modelo e otimizar o desempenho (especialmente para deploy), foi aplicada a Análise de Componentes Principais (PCA). Um `GridSearchCV` foi utilizado para encontrar o número ideal de componentes, determinando-se que **26 componentes** ofereciam o melhor equilíbrio entre performance (CV Score: 91.9%) e redução de dimensionalidade.

### 2.3. Modelagem e Otimização

O problema foi tratado como uma classificação binária, e o modelo escolhido foi a **Regressão Logística**.

1.  **Modelo Baseline (Sem PCA)**: Um modelo inicial de Regressão Logística treinado com as 28 features originais atingiu uma acurácia de **92,57%**.
2.  **Otimização de Hiperparâmetros**: Utilizando os dados transformados pelo PCA de 26 componentes, um `GridSearchCV` foi executado para encontrar os melhores hiperparâmetros para a Regressão Logística.
    * **Melhores Parâmetros**: `{'C': 0.1, 'penalty': 'l2', 'solver': 'newton-cg'}`.
3.  **Modelo Final**: O modelo final consiste em um pipeline que:
    * Aplica a transformação PCA com 26 componentes.
    * Utiliza o classificador `LogisticRegression` com os hiperparâmetros otimizados.

## 3. Resultados

O modelo final foi treinado em 70% dos dados limpos e avaliado em 30% (dados de teste).

* **Acurácia**: **92,5%**
* **ROC AUC**: **0.978** (calculado em um split anterior, demonstrando excelente poder de separação)
* **Relatório de Classificação (no teste de 30%)**:

| Classe | Precision | Recall | F1-Score |
| :--- | :--- | :--- | :--- |
| -1 (Legítima) | 0.93 | 0.93 | 0.93 |
| 1 (Phishing) | 0.92 | 0.92 | 0.92 |

O modelo demonstrou alta performance e equilíbrio, sendo capaz de identificar corretamente tanto URLs legítimas quanto maliciosas com alta precisão e recall.

## 4. Modelos Salvos

Dois arquivos de modelo foram salvos na pasta `modelo/`:

1.  `modelo_pca.joblib`: O objeto `PCA` treinado (fit) com `n_components=26`.
2.  `modelo_versao_final.joblib`: O classificador `LogisticRegression` treinado e otimizado.

## 5. Como Usar (Deploy)

O notebook `Deploy.ipynb` demonstra como usar os modelos salvos para fazer uma nova previsão:

1.  **Carregar os modelos**:
    ```python
    from joblib import load
    modelo_pca_deploy = load('modelo/modelo_pca.joblib')
    modelo_classificador_deploy = load('modelo/modelo_versao_final.joblib')
    ```
2.  **Carregar novos dados**: Os dados devem estar em um formato (ex: DataFrame) com as 28 features esperadas (após a remoção de `indice`, `favicon` e `redirecionamento_double_slash`).
    ```python
    dados_novos = pd.read_csv('dados/novos_dados.csv', header = 0)
    ```
3.  **Pré-processar os dados**: Converter para array NumPy e aplicar a transformação PCA.
    ```python
    dados_array = dados_novos.to_numpy()
    dados_array_pca = modelo_pca_deploy.transform(dados_array)
    ```
4.  **Fazer a Previsão**:
    ```python
    previsao = modelo_classificador_deploy.predict(dados_array_pca)
    # Exemplo de saída: [-1] (Legítima)
    ```

## 6. Bibliotecas Utilizadas

* `numpy`
* `pandas`
* `matplotlib`
* `seaborn`
* `scikit-learn` (para `train_test_split`, `PCA`, `LogisticRegression`, `GridSearchCV`, `Pipeline` e métricas de avaliação)
* `joblib` (para salvar e carregar modelos)
* `mlxtend` (para plotar a matriz de confusão)