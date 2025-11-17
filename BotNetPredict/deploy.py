from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd

# Carregar o modelo treinado e o scaler
scaler = joblib.load('modelos/scaler.pkl')
modelo = joblib.load ('modelos/botnet_detector_model.pkl')

#definindo os nomes das colunas que o scaler espera
feature_names = ['trafego', 'duracao_conexao', 'num_pacotes', 'bytes_transferidos', 'num_erros']

# cria o app
app = Flask(__name__)

#criar a rota raiz
@app.route('/')
def index():
    return render_template('index.html')

#cria a rota para previsao
@app.route('/predict', methods=['POST'])
def predict():
    #recebe os dados do formulario da pagina index.html
    data = request.get_json(force = True)
    #ajusta o shape
    input_data = np.array(data['input']).reshape(1, -1)
    #coverte os dados de entrada em um dataframe com os nomes das colunas
    input_df = pd.DataFrame(input_data, columns = feature_names)
    #padroniza os dados de entrada usando o memso scaler do treinamento
    scaled_input = scaler.transform(input_df)
    #faz a previsao
    prediction = modelo.predict(scaled_input)[0]
    #retorna a previsao em formato json
    return jsonify({'prediction': int(prediction)})

#Executa o app web
if __name__ == '__main__':
    app.run(debug=True)