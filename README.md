# Inteligência Artificial para Segurança Cibernética


Repositório dedicado aos projetos desenvolvidos durante o curso **[Inteligência Artificial para Segurança Cibernética](https://www.datascienceacademy.com.br/course/inteligencia-artificial-para-seguranca-cibernetica)** da Data Science Academy. O objetivo é aplicar conceitos de IA e Machine Learning para resolver desafios no domínio da cibersegurança.

---

## Projetos Desenvolvidos

### 1. Detecção de URL de Phishing (ClassificacaoPhishing)

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
