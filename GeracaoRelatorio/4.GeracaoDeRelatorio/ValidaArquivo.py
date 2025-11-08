import pandas as pd

file_path = "log-web-server.txt"

def valida_arquivo(file_path):
    try:
        df = pd.read_csv(file_path, sep = r'\s+') # O separador de coluna é espaço em branco
        if df.empty:
            return "O arquivo está vazio."

        num_rows = df.shape[0]

        #valida o formato da coluna
        coluna_data = 'date'
        if coluna_data in df.columns:
            try:
                df[coluna_data] = pd.to_datetime(df[coluna_data], format='%Y-%m-%d', errors='raise')
            except Exception as e:
                return f"Erro na conversão da coluna '{coluna_data}': {str(e)}"
        else: 
            return f"A coluna de data '{coluna_data}' não foi encontrada no arquivo."

        #Defindindo os tamanhos maximos esperados para cada coluna
        tamanho_colunas_esperado = {
            'time': 8,  # Formato HH:MM:SS
            's-ip': 15,  # IPv4
            'cs-method': 10,  # Ex: GET, POST
            'cs-uri-stem': 255,  # Caminho URI
            'cs-uri-query': 255,  # Parâmetros de consulta
            's-port': 5,  # Porta (até 65535)
            'cs-username': 50,  # Nome de usuário
            'c-ip': 15,  # IPv4
            'cs(User-Agent)': 255,  # User-Agent
            'cs(Referer)': 255,  # Referer
            'sc-status': 3,  # Código de status HTTP
            'sc-substatus': 3,  # Substatus HTTP
            'sc-win32-status': 3,  # Status Win32
            'time-taken': 10  # Tempo tomado
        }
    # Verificar o tamanho de cada coluna 
        for coluna, tamanho_max in tamanho_colunas_esperado.items():
            if coluna in df.columns:
                if df[coluna].map(lambda x: len(str(x))).max() > tamanho_max:
                    colunas_excedidas = df[df[coluna].map(lambda x: len(str(x))) > tamanho_max]
                    return f"A coluna '{coluna}' possui valores que excedem o tamanho máximo de {tamanho_max} caracteres."
            else:
                return f"A coluna esperada '{coluna}' não foi encontrada no arquivo."
        return f"O arquivo foi validado com sucesso e contém {num_rows} linhas."
    except Exception as e:
        return f"Erro ao ler o arquivo: {str(e)}"

resultado = valida_arquivo(file_path)
print(resultado)