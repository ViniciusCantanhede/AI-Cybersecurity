# 🔎 Detectando Acessos Suspeitos e Maliciosos em Aplicações WEB

Este projeto realiza uma **análise exploratória de dados (EDA)** em logs fictícios de um servidor web para identificar **padrões de acesso suspeitos** e **ações maliciosas**.  
Ao final, um modelo de **machine learning** é treinado para prever e classificar automaticamente esses acessos.

O objetivo principal é identificar **tentativas de ataque de força bruta**, analisando o comportamento de diferentes endereços IP, os métodos de requisição (`POST`, `GET`) e os códigos de status HTTP (especialmente `401 - Unauthorized`).

---

## 🕵️ Análise Exploratória e Principais Descobertas

A análise foi conduzida em várias etapas para filtrar e identificar anomalias nos dados de log:

### 🔸 Análise de Proxy (`cs(User-Agent)`)
A primeira verificação buscou por usuários utilizando proxies (procurando pela palavra-chave _via_), mas **nenhum foi encontrado**.

### 🔸 Análise de Usuários Anônimos (`cs-username`)
Foi verificado o número de acessos anônimos (identificados por `-`).  
Embora **27.500 acessos anônimos** tenham sido encontrados, isso representou uma porção baixa do total, não sendo um indicador conclusivo por si só.

### 🔸 Volume de Solicitações por IP (`c-ip`)
A análise revelou que alguns endereços IP tinham um volume de requisições anormalmente alto, destacando-se:

- `103.211.182.34` — **244 requisições**  
- `45.84.89.130` — **67 requisições**  
- `160.116.57.249` — **46 requisições**

### 🔸 Análise de Métodos (`cs-method` e `sc-status`)
Foi identificado que a maioria das requisições suspeitas utilizava o método **POST** e recebia o status **401 (Unauthorized)**.

### 🔸 Investigação de Força Bruta (`login.aspx`)
Cruzando as informações, a análise focou nos IPs suspeitos e sua atividade na página `login.aspx`.

---

## 🎯 Conclusão da Análise

A investigação confirmou um **padrão claro de ataque de força bruta**:

- **Alvo:** A página `login.aspx` foi o alvo principal, recebendo **84.5% dos acessos com status 401** do IP `103.211.182.34`.  
- **Padrão:** Os IPs maliciosos realizaram um grande volume de requisições `POST` para a página `login.aspx` em um curto período, resultando quase que inteiramente em **falhas de autenticação (status 401)**.

### 🛑 IPs Maliciosos Identificados:
- `103.211.182.34`  
- `45.84.89.130`  
- `160.116.57.249`

> 💡 **Recomendação:** Bloquear imediatamente esses endereços IP para proteger a aplicação.

---

## 🤖 Modelagem Preditiva

Para automatizar a detecção de futuros ataques, foi desenvolvido um **modelo preditivo**.

- **Objetivo:** Classificar um acesso como **normal (0)** ou **suspeito (1)**.  
- **Variável Alvo (label):** O status `sc-status == 401` foi usado como indicador de acesso suspeito (1), e todos os outros status como normais (0).  
- **Features Selecionadas:** `c-ip`, `cs-uri-stem`, `cs(User-Agent)` (convertidas em variáveis dummy / one-hot).  
- **Desafio:** Dados altamente desbalanceados (**69.632 acessos normais** vs. **683 suspeitos**).

---

## 📊 Resultados do Modelo

Foram treinados dois modelos `RandomForestClassifier`:

### ⚙️ Modelo v1 — Linha de Base
- Random Forest padrão, sem tratamento para o desbalanceamento.  
- **Resultado:** Recall de **0.47** para a classe 1 (suspeita).  
  ➤ O modelo falhou em identificar mais da metade dos acessos maliciosos.

### 🚀 Modelo v2 — Otimizado com Balanceamento
- Random Forest treinado com `class_weight='balanced'`.  
- **Resultado:** Recall de **0.76** para a classe 1 (suspeita).  
  ➤ Embora a precisão tenha diminuído (0.37), este modelo é muito superior para o objetivo do projeto, pois **identifica corretamente 76% das ameaças reais**.

---

📌 **Conclusão:**  
O uso de análise exploratória combinada com aprendizado de máquina permite **detectar padrões de ataques de força bruta** de forma eficiente e automatizada, fortalecendo a segurança da aplicação web.
