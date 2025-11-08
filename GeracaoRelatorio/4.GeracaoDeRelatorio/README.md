# 📊 Projeto 4 - IA para Geração de Relatório de Segurança

Sistema automatizado de análise de logs de servidores web com Inteligência Artificial para identificação de anomalias e geração de relatórios de segurança.

## 📋 Sobre o Projeto

Este projeto utiliza IA (Ollama com modelo Gemma3) para analisar logs de servidores web, identificar possíveis tentativas de ataque, anomalias de segurança e gerar automaticamente um relatório completo em formato Word (.docx) com recomendações de segurança.

## 🎯 Funcionalidades

- ✅ **Validação Automática de Logs**: Verifica integridade, formato e estrutura dos arquivos de log
- 🔍 **Análise Inteligente**: Utiliza IA para análise semântica de cada entrada do log
- 🛡️ **Detecção de Ameaças**: Identifica padrões suspeitos, tentativas de ataque e anomalias
- 📄 **Geração de Relatório**: Cria documento Word profissional com análises e recomendações
- 🔄 **Pipeline Automatizado**: Execução sequencial com tratamento de erros

## 🏗️ Estrutura do Projeto

```
4.GeracaoDeRelatorio/
├── ExecutandoAnalise.py          # Script principal que executa o pipeline
├── ValidaArquivo.py              # Valida formato e integridade dos logs
├── AnalisaArquivo.py             # Análise com IA e geração do relatório
├── log-web-server.txt            # Arquivo de log de entrada
├── requirements.txt              # Dependências do projeto
└── Relatorio_Seguranca_Log_Web_Server.docx  # Relatório gerado (output)
```

## 🔧 Componentes

### 1. ExecutandoAnalise.py
Script orquestrador que executa o pipeline completo:
- Executa ValidaArquivo.py
- Executa AnalisaArquivo.py
- Monitora sucesso/falha de cada etapa
- Calcula tempo total de execução

### 2. ValidaArquivo.py
Validador de logs que verifica:
- Formato do arquivo (separadores, colunas esperadas)
- Integridade dos dados
- Validação de tipos (datas, IPs, portas)
- Tamanho máximo de cada campo
- Arquivo vazio ou corrompido

### 3. AnalisaArquivo.py
Motor de análise com IA:
- Carrega logs usando Pandas
- Processa cada linha individualmente
- Envia contexto para o modelo Gemma3
- Recebe análise de segurança especializada
- Gera documento Word formatado

## 📦 Instalação

### Pré-requisitos

- Python 3.10 ou superior
- [Ollama](https://ollama.ai/) instalado
- Modelo Gemma3 (1b ou 4b)

### Passo 1: Instalar Ollama e o Modelo

```bash
# Instalar Ollama (macOS)
brew install ollama

# Baixar o modelo Gemma3
ollama pull gemma3:1b
# ou para o modelo maior (mais preciso)
ollama pull gemma3:4b

# Verificar modelos instalados
ollama list
```

### Passo 2: Configurar Ambiente Python

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual (macOS/Linux)
source .venv/bin/activate

# Ativar ambiente virtual (Windows)
.venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

## 🚀 Como Usar

### Execução Básica

```bash
# Ativar ambiente virtual
source .venv/bin/activate

# Executar pipeline completo
python ExecutandoAnalise.py
```

### Executar Componentes Separadamente

```bash
# Apenas validar o arquivo
python ValidaArquivo.py

# Apenas gerar relatório (após validação)
python AnalisaArquivo.py
```

## 📊 Formato do Log

O arquivo de log deve seguir o formato padrão de logs IIS/Web Server:

```
date time s-ip cs-method cs-uri-stem cs-uri-query s-port cs-username c-ip cs(User-Agent) cs(Referer) sc-status sc-substatus sc-win32-status time-taken
```

**Exemplo de linha:**
```
2022-01-01 00:58:33 57.222.145.109 GET index.aspx - 443 - 89.251.124.218 Mozilla/5.0 https://bankofpunk.local/index.aspx 200 0 0 21
```

## 🎨 Saída do Sistema

### Console
```
Projeto 4 - IA para Geração de Relatório de Segurança a Partir da Análise de Logs de Servidores Web

Executando ValidaArquivo.py...
Script ValidaArquivo.py executado com sucesso

Saída:
O arquivo foi validado com sucesso e contém 10 linhas.

Executando AnalisaArquivo.py...
Relatório de segurança gerado com sucesso: Relatorio_Seguranca_Log_Web_Server.docx

Pipeline concluído com sucesso em X.XX segundos.
```

### Arquivo Gerado
- **Relatorio_Seguranca_Log_Web_Server.docx**: Documento Word profissional contendo:
  - Análise detalhada de cada linha do log
  - Identificação de anomalias e tentativas de ataque
  - Recomendações de segurança específicas
  - Insights sobre padrões suspeitos

## ⚙️ Configuração

### Alterar Modelo de IA

Edite o arquivo `AnalisaArquivo.py`, linha 7:

```python
# Modelo menor e mais rápido
llm = Ollama(model = "gemma3:1b")

# Modelo maior e mais preciso
llm = Ollama(model = "gemma3:4b")
```

### Personalizar Análise

Modifique o prompt do sistema em `AnalisaArquivo.py`, linhas 18-21:

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "Seu prompt personalizado aqui..."),
    ("user", "question: {question}")
])
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.13**: Linguagem principal
- **Pandas**: Manipulação e análise de dados
- **LangChain**: Framework para aplicações com LLM
- **Ollama**: Motor de execução de modelos locais
- **Gemma3**: Modelo de linguagem do Google
- **python-docx**: Geração de documentos Word

## 📝 Dependências Principais

```
pandas==2.3.1
langchain==0.3.26
langchain-community==0.3.27
langchain-core==0.3.69
python-docx==1.2.0
```

## 🐛 Solução de Problemas

### Erro: "name 'pd' is not defined"
- ✅ Verifique o import: `import pandas as pd`

### Erro: "Ollama call failed with status code 404"
- ✅ Instale o modelo: `ollama pull gemma3:1b`
- ✅ Verifique modelos disponíveis: `ollama list`

### Erro: "ModuleNotFoundError: No module named 'langchain_core.output_parses'"
- ✅ Corrija o import: `from langchain_core.output_parsers import StrOutputParser`

### Warning: "invalid escape sequence"
- ✅ Use raw strings: `sep = r'\s+'` ao invés de `sep = '\s+'`

## 📈 Melhorias Futuras

- [ ] Suporte a múltiplos formatos de log
- [ ] Dashboard interativo com visualizações
- [ ] Alertas em tempo real
- [ ] Integração com SIEM
- [ ] Exportação em múltiplos formatos (PDF, HTML, JSON)
- [ ] Análise estatística avançada
- [ ] Machine Learning para detecção de padrões

## 👨‍💻 Autor

Projeto desenvolvido como parte do curso Data Science Academy (DSA).

## 📄 Licença

Este projeto é de uso educacional.

---

**💡 Dica**: Execute o pipeline regularmente em seus logs de produção para monitoramento contínuo de segurança!
