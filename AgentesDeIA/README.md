# Time de Agentes de IA para Teste de Vulnerabilidades

Um sistema multi-agente baseado em **LangGraph** que utiliza inteligência artificial para realizar análise automatizada de vulnerabilidades de segurança, pesquisa de ameaças e geração de relatórios técnicos.

## 📋 Visão Geral

Este projeto implementa um workflow automatizado com três agentes especializados que trabalham em conjunto para:

1. **Pesquisador** - Busca informações sobre vulnerabilidades usando a API Tavily
2. **Analista de Segurança** - Avalia e categoriza vulnerabilidades por nível de risco
3. **Redator Técnico** - Elabora relatório detalhado com recomendações de mitigação

## 🏗️ Arquitetura

O projeto utiliza **LangGraph** para orquestrar o fluxo de trabalho entre agentes:

```
┌─────────────────────────────────┐
│      Tópico de Pesquisa         │
└────────────┬────────────────────┘
             │
             ▼
    ┌─────────────────┐
    │   Pesquisador   │ ◄─── Busca com Tavily Search
    │   (Agente 1)    │
    └────────┬────────┘
             │
             ▼
  ┌────────────────────────┐
  │ Analista de Segurança  │ ◄─── Categorização de Risco
  │    (Agente 2)          │
  └────────┬───────────────┘
           │
           ▼
   ┌────────────────────┐
   │  Redator Técnico   │ ◄─── Geração de Relatório
   │    (Agente 3)      │
   └─────────┬──────────┘
             │
             ▼
    ┌──────────────────┐
    │ Relatório Final  │
    └──────────────────┘
```

## 🚀 Funcionalidades

- **Análise Multi-Etapas**: Pesquisa → Análise → Relatório
- **Agentes Especializados**: Cada agente tem role específico com prompts customizados
- **Integração com APIs**: Uso de OpenAI GPT e Tavily Search
- **Rastreamento de Contexto**: Histórico de mensagens mantido entre agentes
- **Saída Estruturada**: Relatórios salvos em arquivo de texto

## 📦 Dependências

As principais dependências incluem:

- **LangChain**: Framework para construir aplicações com LLMs
- **LangGraph**: Orquestração de fluxos de trabalho com agentes
- **OpenAI**: Modelo GPT para processamento de linguagem natural
- **Tavily**: API de busca para pesquisa de informações de segurança
- **python-dotenv**: Gerenciamento de variáveis de ambiente

Veja `requirements.txt` para a lista completa.

## 🔧 Instalação

### 1. Clonar o repositório
```bash
cd /path/to/project
```

### 2. Criar ambiente virtual (opcional mas recomendado)
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate  # Windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Criar arquivo `.env` na raiz do projeto:
```env
OPENAI_API_KEY=sua_chave_openai_aqui
TAVILY_API_KEY=sua_chave_tavily_aqui
```

## 🎯 Como Usar

### Executar o programa

```bash
python AgentesDeSeguranca.py
```

### Fluxo de Execução

1. O programa define um tópico de pesquisa (padrão: "Segurança em formulários de login no site OWASP Juice Shop")
2. O **Pesquisador** busca informações relevantes
3. O **Analista** avalia e categoriza as vulnerabilidades
4. O **Redator** gera o relatório técnico final
5. O relatório é salvo em `relatorio_seguranca.txt`

### Personalizar Tópico

Editar a variável `topico` no bloco `if __name__ == "__main__":` do arquivo `AgentesDeSeguranca.py`:

```python
topico = "Seu tópico de segurança aqui"
```

## 📄 Saída

O programa gera um relatório estruturado contendo:

- **Sumário Executivo**: Overview das vulnerabilidades encontradas
- **Escopo e Metodologia**: Contexto da análise
- **Vulnerabilidades Detalhadas**: Para cada vulnerabilidade:
  - Descrição
  - Nível de risco (Crítico, Alto, Médio, Baixo)
  - Impacto e probabilidade
  - Exemplos e Proof-of-Concepts
  - Recomendações técnicas
  - Score CVSS estimado

- **Plano de Ação**: Priorização e prazos de remediação
- **Checklist de Testes**: Validação pós-correção
- **Referências**: Documentação OWASP

## 🔐 Segurança

- **Variáveis de Ambiente**: Chaves de API nunca são commitadas no código
- **Uso de `.env`**: Arquivo deve estar no `.gitignore`
- **Logs Estruturados**: Rastreamento detalhado de cada etapa

## 📊 Exemplo de Saída

```
--- NÓ: PESQUISADOR ---
[Busca informações sobre o tópico...]

--- NÓ: ANALISTA DE SEGURANÇA ---
[Analisa e categoriza vulnerabilidades...]

--- NÓ: GERADOR DE RELATÓRIO ---
[Gera relatório técnico detalhado...]

--- RELATÓRIO FINAL GERADO ---
[Conteúdo completo do relatório...]

✅ Relatório salvo com sucesso no arquivo: relatorio_seguranca.txt
```

## 🛠️ Estrutura do Código

### Classes Principais

- **AgentState**: TypedDict que define o estado compartilhado entre agentes
  - `topic`: Tópico a ser analisado
  - `pesquisa`: Resultados da pesquisa
  - `analise`: Análise das vulnerabilidades
  - `relatorio_final`: Relatório gerado
  - `messages`: Histórico de mensagens

### Funções Principais

- `cria_agente()`: Factory para criar agentes com ferramentas específicas
- `node_executa_pesquisador()`: Executa o agente pesquisador
- `node_executa_analista()`: Executa o agente analista
- `node_executa_redator()`: Executa o agente redator

## 🐛 Troubleshooting

### Erro: "Chaves nao configuradas"
- Verificar se arquivo `.env` existe na raiz do projeto
- Confirmar que `OPENAI_API_KEY` e `TAVILY_API_KEY` estão definidas

### Erro de conectividade
- Verificar conexão com internet
- Validar chaves de API ativas nas plataformas OpenAI e Tavily

### Execução lenta
- Tempo de resposta depende da complexidade da análise
- Grandes prompts podem aumentar latência
- Considerar ajustar número máximo de resultados Tavily (`max_results=5`)

## 📚 Recursos Adicionais

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)


**Nota**: Este projeto é destinado para fins educacionais e de pesquisa. Sempre obtenha autorização antes de realizar testes de segurança em sistemas reais.
