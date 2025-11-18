import os
from dotenv import load_dotenv
from typing import TypedDict, Optional
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.graph import StateGraph, END
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, BaseMessage, AIMessage

# Carregando variaveis
print('\nIniciando o Trabalho do Time de Agentes de IA Para Teste de Vulnerabilidades!\n')

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

if not openai_api_key or not tavily_api_key:
    raise ValueError("Chaves nao configuradas, verifique o .env")
print('APIs carregadas!')

# criando objeto agentes
search_tool = TavilySearch(max_results=5)
llm = ChatOpenAI(api_key = openai_api_key, model = "gpt-5-mini")

# definindo estrutura do estado compartilhado entre agentes
class AgentState(TypedDict):
    topic: str
    pesquisa: Optional[str]
    analise: Optional[str]
    relatorio_final: Optional[str]
    messages: list[BaseMessage]

# define funcao para criar agentes
def cria_agente(llm: ChatOpenAI, tools: list, system_prompt: str):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name = "messages"),
        MessagesPlaceholder(variable_name = "agent_scratchpad"),
    ])
    agent = create_openai_tools_agent(llm, tools, prompt)
    executor = AgentExecutor(agent = agent, tools = tools, verbose = True)
    return executor

# agente pesquisador responsavel por buscar informaçoes sobre vulnerabilidades
agente_pesquisador = cria_agente(
    llm,
    [search_tool],
    """Você é um especialista sênior em cibersegurança com experiência em detecção de vulnerabilidades e análise de ameaças.
    Sua especialidade pe identificar vulnerabilidades comuns e emergentes em websites e sistemas web.
    Sua tarefa é pesquisar o tópica fornecido e reunir informações de fontes confiáveis.
    Para isso, formule consultas de buscas concisas e eficazes baseadas no tópico para usar com a ferramenta de pesquisa.
    Ao final, forneça um resumo claro e informativo das descobertas."""
    )

#agente analista responsavel por avaliar e classficar o risco das vulnerabilidades
agente_analista = cria_agente(
    llm,
    [],
    """Você é um especialista em segurança da informação, com foco em avaliação de risco e teste de penetração.
    Sua tarefa é analisar e categorizar as vulnerabilidades encontradas no texto fornecido.
    Avalie o nível de risco (crítico, alto, médio, baixo) para cada vulnerabilidade e prepare os dados para inclusão no relatório"""
    )

#agente redator responsável por elaborar o relatorio final
agente_redator = cria_agente(
    llm,
    [],
    """Você é um redator técnico especializado em relatório de segurança da informação.
    Sua tarefa é desenvolver um relatório de segurança bem detalhado com base na análise fornecida.
    O relatório deve ser bem estruturado, claro e incluir as vulnerabilidades, seus nívei de risco e recomendações práticas para mitigação"""
    )

#define o nó responsável por executar o agente pesquisador
def node_executa_pesquisador(state: AgentState):
    print("--- NÓ: PESQUISADOR ---")

    #cria messagem humana solicitando pequisa sobre o topico fornecido
    messages = [HumanMessage(content = f"Pesquise vulnerabilidades relacionadas a {state['topic']}")]
    #invoca o agente pesquisador passando as messagens como entrada
    result = agente_pesquisador.invoke({"messages": messages})
    return {"pesquisa": result["output"], "messages": messages + [AIMessage(content = result["output"])]}


# Define o nó responsável por executar o agente analista de segurança
def node_executa_analista(state: AgentState):
    # Exibe mensagem indicando o início da execução do nó do analista
    print("--- NÓ: ANALISTA DE SEGURANÇA ---")

    # Monta o prompt que será enviado ao agente analista com as descobertas de pesquisa
    prompt = f"""Analise as seguintes vulnerabilidades encontradas e categorize-as por nível de risco.

    Descobertas da Pesquisa:
    {state['pesquisa']}
    """

    # Adiciona a nova mensagem ao histórico existente de mensagens
    current_messages = state["messages"] + [HumanMessage(content=prompt)]

    # Invoca o agente analista passando as mensagens atualizadas
    result = agente_analista.invoke({"messages": current_messages})

    # Retorna o resultado da análise e atualiza o histórico de mensagens
    return {"analise": result["output"], "messages": current_messages + [AIMessage(content=result["output"])]}


# Define o nó responsável por executar o agente redator do relatório final
def node_executa_redator(state: AgentState):
    # Exibe mensagem indicando o início da execução do nó do redator
    print("--- NÓ: GERADOR DE RELATÓRIO ---")

    prompt = f"""Crie um relatório de segurança detalhado com base na análise abaixo. Inclua vulnerabilidades, riscos e recomendações.
    Análise de Segurança:
    {state['analise']}
    """

    # Atualiza o histórico de mensagens com o novo prompt
    current_messages = state["messages"] + [HumanMessage(content=prompt)]
    # Invoca o agente redator com o contexto completo
    result = agente_redator.invoke({"messages": current_messages})
    # Retorna o relatório final e o histórico de mensagens atualizado
    return {"relatorio_final": result["output"], "messages": current_messages + [AIMessage(content=result["output"])]}


# Cria o grafo de estados (workflow) com base na estrutura AgentState
workflow = StateGraph(AgentState)

# Adiciona o nó do pesquisador ao fluxo
workflow.add_node("pesquisador", node_executa_pesquisador)

# Adiciona o nó do analista de segurança ao fluxo
workflow.add_node("analista_seguranca", node_executa_analista)

# Adiciona o nó do redator responsável pelo relatório ao fluxo
workflow.add_node("relatorio_seguranca", node_executa_redator)

# Define o ponto de entrada do fluxo (primeiro nó a ser executado)
workflow.set_entry_point("pesquisador")

# Define as transições entre os nós (ordem de execução)
workflow.add_edge("pesquisador", "analista_seguranca")
workflow.add_edge("analista_seguranca", "relatorio_seguranca")

# Define o término do fluxo após o relatório final
workflow.add_edge("relatorio_seguranca", END)

# Compila o fluxo completo para execução
app = workflow.compile()

# Bloco principal do programa
if __name__ == "__main__":

    # Define o tópico a ser analisado pelo time de agentes
    topico = "Segurança em formulários de login no site OWASP Juice Shop (https://owasp.org/www-project-juice-shop/)"

    # Exibe mensagem informando que o processo será iniciado
    print('\nTópico Definido. O Time de Agentes (LangGraph) Entrará em Ação!\n')

    # Cria o dicionário de entrada inicial para o workflow
    inputs = {"topic": topico, "messages": []}

    # Inicializa a variável que armazenará o estado final do fluxo
    final_state = None

    # Executa o fluxo e captura o estado em cada etapa
    for output in app.stream(inputs, stream_mode="values"):
        final_state = output

    # Extrai o relatório final do estado gerado
    resultado_final = final_state["relatorio_final"]

    # Exibe o relatório final no console
    print("\n\n--- RELATÓRIO FINAL GERADO ---")
    print(resultado_final)

    # Define o nome do arquivo de saída do relatório
    nome_arquivo = "relatorio_seguranca.txt"

    try:
        # Abre o arquivo para escrita e salva o relatório com cabeçalho formatado
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write("RELATÓRIO DE ANÁLISE DE VULNERABILIDADES\n")
            f.write("=" * 40 + "\n\n")
            f.write(f"TÓPICO: {topico}\n\n")
            f.write(resultado_final)

        # Exibe mensagem confirmando o sucesso da operação
        print(f"\n✅ Relatório salvo com sucesso no arquivo: {nome_arquivo}")

    # Captura e exibe erros caso ocorram ao salvar o arquivo
    except Exception as e:
        print(f"\n❌ Ocorreu um erro ao salvar o arquivo: {e}")

    # Exibe mensagem final de encerramento do programa
    print('\nObrigado Por Usar o Time de Agentes de IA Para Teste de Vulnerabilidades!\n')
