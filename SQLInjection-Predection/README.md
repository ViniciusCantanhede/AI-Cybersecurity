# Detecção e Prevenção de Ataques SQL Injection

## 📋 Descrição do Projeto

Este projeto implementa um **modelo de Machine Learning preditivo** capaz de detectar e prevenir ataques cibernéticos de **SQL Injection**. O objetivo é classificar consultas SQL como seguras (0) ou maliciosas (1), contribuindo para a segurança de aplicações web e sistemas de banco de dados.

O modelo foi desenvolvido e comparado em **6 versões diferentes**, utilizando diversos algoritmos de aprendizado supervisionado, e a melhor versão foi selecionada para deploy.

## 🎯 O que é SQL Injection?

SQL Injection é um tipo de ataque cibernético em que o invasor insere comandos SQL maliciosos em campos de entrada (formulários, URLs, parâmetros) para manipular o banco de dados de uma aplicação.

### Exemplo de ataque:
```
Entrada esperada: admin
Entrada maliciosa: admin' OR '1'='1
```

Se a aplicação não tratar isso corretamente, o atacante pode conseguir acesso sem senha, roubar dados ou deletar informações críticas.

## 📁 Estrutura do Projeto

```
9.DetectarSQLInjection/
├── README.md                  # Este arquivo
├── Projeto9.ipynb             # Notebook com análise completa
├── requirements.txt           # Dependências do projeto
├── dados/
│   ├── dados_sql.csv          # Dataset com 32.000+ queries SQL
│   └── novos_dados_sql.txt    # Exemplos para teste do modelo
└── modelos/
    ├── vectorizer             # TfidfVectorizer treinado
    └── melhor_modelo.pkl      # Modelo Logistic Regression em produção
```

## 📊 Dataset

- **Fonte**: [Kaggle - SQL Injection Dataset](https://www.kaggle.com/datasets/sajid576/sql-injection-dataset)
- **Tamanho**: 32.000+ registros
- **Colunas**:
  - `Query`: String de consulta SQL bruta
  - `Label`: 0 (consulta segura) ou 1 (consulta maliciosa)

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas**: Manipulação e análise de dados
- **Scikit-learn**: Modelos de Machine Learning
- **TfidfVectorizer**: Vetorização de texto (TF-IDF)

## Testar o Modelo em Produção

```python
import pickle
import pandas as pd

# Carregar vectorizer e modelo
vetorizador = pickle.load(open("modelos/vectorizer", 'rb'))
modelo = pickle.load(open("modelos/melhor_modelo.pkl", "rb"))

# Exemplo de query SQL
query = ["SELECT * FROM users WHERE id = 1"]

# Vetorizar e prever
query_vetorizada = vetorizador.transform(query)
resultado = modelo.predict(query_vetorizada)

if resultado[0] == 0:
    print("✅ Query Segura!")
else:
    print("⚠️ Query Maliciosa! Possível Ataque SQL Injection!")
```

### Testar com Novos Dados

```python
import pickle
import pandas as pd

# Carregar dados
with open("dados/novos_dados_sql.txt", "r") as file:
    lines = file.readlines()

novos_dados = pd.DataFrame(lines, columns=['Query'])
novos_dados = novos_dados.replace("\n", "", regex=True)

# Fazer previsões
vetorizador = pickle.load(open("modelos/vectorizer", 'rb'))
modelo = pickle.load(open("modelos/melhor_modelo.pkl", "rb"))

sql_query = vetorizador.transform(novos_dados['Query'])
resultados = modelo.predict(sql_query)

print(resultados)
```

## 🤖 Modelos Avaliados

### Versão 1: Logistic Regression ⭐ (Selecionado)
- **F1-Score**: 0.962
- **Precision**: 0.937
- **Recall**: 0.989
- **Accuracy**: 0.972

**Razão da seleção**: Melhor equilíbrio entre precisão e recall, com a maior acurácia geral.

### Versão 2: Decision Tree
- **F1-Score**: 0.951
- **Precision**: 0.930
- **Recall**: 0.973
- **Accuracy**: 0.963

### Versão 3: Random Forest
- **F1-Score**: 0.956
- **Precision**: 0.934
- **Recall**: 0.980
- **Accuracy**: 0.968

### Versão 4: Support Vector Machines (SVM)
- **F1-Score**: 0.950
- **Precision**: 0.925
- **Recall**: 0.976
- **Accuracy**: 0.961

### Versão 5: Multinomial Naive Bayes
- **F1-Score**: 0.957
- **Precision**: 0.928
- **Recall**: 0.988
- **Accuracy**: 0.969

### Versão 6: Gradient Boosting
- **F1-Score**: 0.954
- **Precision**: 0.932
- **Recall**: 0.977
- **Accuracy**: 0.966

## 📈 Métricas de Avaliação

As métricas utilizadas para comparar os modelos foram:

- **Accuracy**: $(TP + TN) / (TP + TN + FP + FN)$
- **Precision**: $TP / (TP + FP)$
- **Recall**: $TP / (TP + FN)$
- **F1-Score**: $2 \times (Precision \times Recall) / (Precision + Recall)$

Onde:
- **TP** (True Positive): Queries maliciosas corretamente identificadas
- **TN** (True Negative): Queries seguras corretamente identificadas
- **FP** (False Positive): Queries seguras incorretamente classificadas como maliciosas
- **FN** (False Negative): Queries maliciosas não detectadas

## 🔍 Pré-processamento de Dados

### TF-IDF (Term Frequency - Inverse Document Frequency)

O `TfidfVectorizer` foi utilizado para vetorizar as queries SQL:

- **Term Frequency (TF)**: Frequência de cada termo na query
- **Inverse Document Frequency (IDF)**: Inverso da frequência do termo em todo o dataset
- **Resultado**: Matriz numérica que alimenta os modelos de ML

```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X_treino = vectorizer.fit_transform(X_treino)
X_teste = vectorizer.transform(X_teste)
```

## 🎓 Como Identificar SQL Injection

### 1. Comportamentos Suspeitos
- Mensagens de erro SQL aparecem na tela
- Páginas quebram com caracteres como `'`, `"`, `--`, `;`, `)`

### 2. Testes Manuais
```sql
-- Teste com aspas
' 
" 
'' 

-- Teste com operadores lógicos
' OR 1=1 --
" OR "1"="1

-- Teste de comentários
admin' --
```

### 3. Sinais de Alerta
- Entrada comum quebra a página
- Consegue burlar autenticação
- Altera resultados de consultas
- Erros SQL são exibidos ao usuário

## 🛡️ Como Prevenir SQL Injection

1. **Usar Prepared Statements**: Separar comando SQL dos dados
2. **Validar Entradas**: Verificar tipos e formatos esperados
3. **Sanitizar Dados**: Remover caracteres perigosos
4. **Aplicar Principle of Least Privilege**: Limitar permissões do banco de dados
5. **Usar ORM Frameworks**: Abstração de banco de dados (ex: SQLAlchemy)
6. **Implementar Web Application Firewall (WAF)**

## 📝 Divisão Treino/Teste

- **Treino**: 70% dos dados (22.400+ queries)
- **Teste**: 30% dos dados (9.600+ queries)
- **Random State**: 1 (para reprodutibilidade)

## ✅ Validação do Modelo

O modelo foi testado com:
- Queries SQL seguras conhecidas
- Queries SQL maliciosas conhecidas
- Novos exemplos de ataques SQL Injection

Todos os testes apresentaram resultados consistentes e confiáveis.

## 📚 Referências

- [Kaggle - SQL Injection Dataset](https://www.kaggle.com/datasets/sajid576/sql-injection-dataset)
- [OWASP - SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Data Science Academy](https://www.datascienceacademy.com.br)

## 👨‍💻 Autor

Projeto desenvolvido como parte da formação em **IA para Cibersegurança** pela Data Science Academy.

