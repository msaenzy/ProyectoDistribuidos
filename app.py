from flask import Flask, render_template
import pandas as pd
from sklearn.neighbors import LocalOutlierFactor

app = Flask(__name__)

# Ruta al archivo CSV
file_path = 'energia.csv'

# Cargar el archivo CSV en un DataFrame de Pandas
data = pd.read_csv(file_path, encoding='latin1')

@app.route('/')
def index():
    # Lista de nombres de meses
    meses = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE']

    # Diccionario para almacenar los índices de las anomalías de cada mes
    anomalous_indices = {}

    # Crear un modelo de detección de anomalías para cada mes
    for mes in meses:
        # Seleccionar una muestra aleatoria de 100 filas del DataFrame para el mes actual
        muestra_aleatoria = data.sample(n=100)

        # Crear un modelo de detección de anomalías
        lof = LocalOutlierFactor(contamination=0.1)

        # Entrenar el modelo con los datos de consumo de energía para el mes actual
        consumo = muestra_aleatoria[f'CONSUMO_KWH_{mes}'].values.reshape(-1, 1)
        lof.fit(consumo)

        # Predecir las anomalías para el mes actual
        anomalies = lof.fit_predict(consumo)

        # Obtener los índices de las anomalías para el mes actual y guardarlos en el diccionario
        anomalous_indices[mes] = muestra_aleatoria.index[anomalies == -1].tolist()

    return render_template('index.html', meses=meses, anomalous_indices=anomalous_indices)

if __name__ == '__main__':
    app.run(debug=True)
