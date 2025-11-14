# Fine-Tuning de LLM para Detecção de Anomalias de Tráfego de Rede

Este projeto demonstra o processo de fine-tuning de um modelo de linguagem grande (LLM), especificamente o `bert-base-uncased`, para a tarefa de detecção de anomalias em tráfego de rede. O notebook `Fine_Tuning.ipynb` guia através de todas as etapas, desde o carregamento e pré-processamento dos dados até o treinamento, avaliação e previsão com o modelo.

## Modelo Utilizado

- **Modelo:** `bert-base-uncased`
- **Fonte:** [Hugging Face Model Hub](https://huggingface.co/bert-base-uncased)

## Estrutura do Projeto

```
.
├── Fine_Tuning.ipynb
├── dados/
│   ├── dados_historicos.csv
│   └── novos_dados.csv
└── requirements.txt
```

- `Fine_Tuning.ipynb`: O notebook principal contendo todo o código para o projeto.
- `dados/dados_historicos.csv`: Dados históricos de tráfego de rede utilizados para treinamento e teste do modelo.
- `dados/novos_dados.csv`: Novos dados de tráfego de rede para realizar previsões com o modelo treinado.
- `requirements.txt`: Arquivo contendo as dependências do projeto.

## Como Executar

1.  **Instale as dependências:**
    Certifique-se de ter o Python instalado e, em seguida, instale as bibliotecas necessárias executando o seguinte comando no terminal:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Execute o Notebook:**
    Abra e execute o notebook `Fine_Tuning.ipynb` em um ambiente Jupyter (como Jupyter Lab, Jupyter Notebook ou VS Code) para treinar o modelo e ver o processo em ação.

## Processo

1.  **Carregamento de Dados:** Os dados de tráfego de rede são carregados a partir de um arquivo CSV.
2.  **Pré-processamento:** Os dados categóricos (IPs, protocolos) são codificados, e as características são concatenadas em uma única string para servir de entrada para o BERT.
3.  **Modelagem e Fine-Tuning:** O modelo `bert-base-uncased` pré-treinado é carregado e fine-tuned com os dados de tráfego de rede.
4.  **Avaliação:** O desempenho do modelo é avaliado usando métricas como Acurácia, ROC-AUC e F1-Score.
5.  **Previsão:** O modelo treinado é usado para prever se novos registros de tráfego de rede são anomalias.

## Resultados

O modelo treinado é capaz de classificar novos dados de tráfego de rede como anômalos ou não. O notebook demonstra a previsão em um novo conjunto de dados, classificando-os como anomalias.
