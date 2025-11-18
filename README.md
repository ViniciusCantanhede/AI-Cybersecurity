# Inteligência Artificial para Segurança Cibernética


Repositório dedicado aos projetos desenvolvidos durante o curso **[Inteligência Artificial para Segurança Cibernética](https://www.datascienceacademy.com.br/course/inteligencia-artificial-para-seguranca-cibernetica)** da Data Science Academy. O objetivo é aplicar conceitos de IA e Machine Learning para resolver desafios no domínio da cibersegurança.

---

# Projetos Desenvolvidos

# Projeto 1:  Detecção de URL de Phishing (ClassificacaoPhishing)

Este projeto tem como objetivo construir um modelo de machine learning capaz de classificar URLs como legítimas ou maliciosas (phishing), atendendo à necessidade de uma empresa de e-commerce que deseja proteger seus usuários de anúncios com links perigosos.

#### Contexto

Uma empresa de e-commerce implementou um sistema de banners de anúncios onde terceiros podem inserir links. Para mitigar o risco de direcionar usuários a sites maliciosos, foi desenvolvido um modelo preditivo que analisa as características de uma URL e a classifica como segura ou como uma tentativa de phishing.


-----

# Projeto 2: Detecção de Invasão de Rede com Machine Learning

Este projeto tem como objetivo construir um modelo de machine learning de alta precisão para a detecção de intrusões em redes de computadores. O modelo é treinado para classificar o tráfego de rede como `normal` ou `anomalia` (ataque), com base em um conjunto de features extraídas dos pacotes de dados.


### Contexto do Projeto

Este é o segundo projeto desenvolvido como parte do curso **[Inteligência Artificial para Segurança Cibernética](https://www.datascienceacademy.com.br/course/inteligencia-artificial-para-seguranca-cibernetica)** da Data Science Academy. O objetivo é aplicar técnicas de classificação supervisionada para identificar atividades maliciosas em um grande volume de tráfego de rede, um desafio central na cibersegurança moderna.


----

# Projeto 3: 🔎 Detectando Acessos Suspeitos e Maliciosos em Aplicações WEB

Este projeto realiza uma **análise exploratória de dados (EDA)** em logs fictícios de um servidor web para identificar **padrões de acesso suspeitos** e **ações maliciosas**.  
Ao final, um modelo de **machine learning** é treinado para prever e classificar automaticamente esses acessos.

----

# Projeto 4 - IA para Geração de Relatório de Segurança 📊

Sistema automatizado de análise de logs de servidores web com Inteligência Artificial para identificação de anomalias e geração de relatórios de segurança.

## 📋 Sobre o Projeto

Este projeto utiliza IA (Ollama com modelo Gemma3) para analisar logs de servidores web, identificar possíveis tentativas de ataque, anomalias de segurança e gerar automaticamente um relatório completo em formato Word (.docx) com recomendações de segurança.

---- 

# Projeto 5: 🔎 Detecção de Transações Fraudulentas em Base de Dados Desbalanceada

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

# Projeto 6: 🔐 Detecção de Ameaças em Dispositivos IoT  
Análise de Dados Reais com o Dataset UNSW-NB15

Este projeto realiza uma análise completa sobre um conjunto de dados real utilizado para identificar **ataques cibernéticos em dispositivos IoT**. O foco principal é explorar os dados, tratar o desbalanceamento das classes e propor um modelo de **classificação multiclasse** capaz de detectar diferentes tipos de ameaças.

---

# Projeto 7: 🔒 Detector de Ataques Botnet com IA

Sistema de detecção de ataques de botnet utilizando aprendizado semi-supervisionado com Flask para deploy web.

## 📋 Sobre o Projeto

Este projeto utiliza técnicas de **aprendizado semi-supervisionado** (Label Spreading) para identificar e prever ataques de botnet em redes, combinando dados rotulados e não rotulados para aumentar a precisão do modelo. O projeto inclui:

- Criação e análise exploratória de dados sintéticos
- Pré-processamento e normalização de features
- Treinamento de modelo com algoritmo Label Spreading
- Aplicação web Flask para detecção em tempo real
- Interface HTML intuitiva para entrada de dados

---

# Projeto 8: Fine-Tuning de LLM para Detecção de Anomalias de Tráfego de Rede

Este projeto demonstra o processo de fine-tuning de um modelo de linguagem grande (LLM), especificamente o `bert-base-uncased`, para a tarefa de detecção de anomalias em tráfego de rede. O notebook `Fine_Tuning.ipynb` guia através de todas as etapas, desde o carregamento e pré-processamento dos dados até o treinamento, avaliação e previsão com o modelo.

---

# Projeto 9: Detecção e Prevenção de Ataques SQL Injection

## 📋 Descrição do Projeto

Este projeto implementa um **modelo de Machine Learning preditivo** capaz de detectar e prevenir ataques cibernéticos de **SQL Injection**. O objetivo é classificar consultas SQL como seguras (0) ou maliciosas (1), contribuindo para a segurança de aplicações web e sistemas de banco de dados.

---

# Projeto 10: Time de Agentes de IA para Teste de Vulnerabilidades

Um sistema multi-agente baseado em **LangGraph** que utiliza inteligência artificial para realizar análise automatizada de vulnerabilidades de segurança, pesquisa de ameaças e geração de relatórios técnicos.

## 📋 Visão Geral

Este projeto implementa um workflow automatizado com três agentes especializados que trabalham em conjunto para:

1. **Pesquisador** - Busca informações sobre vulnerabilidades usando a API Tavily
2. **Analista de Segurança** - Avalia e categoriza vulnerabilidades por nível de risco
3. **Redator Técnico** - Elabora relatório detalhado com recomendações de mitigação
