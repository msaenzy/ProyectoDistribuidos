from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Ruta al archivo CSV
file_path = 'C:/Users/famil/Downloads/PROYECTODISTRIBUIDO/energia.csv'

# Cargar el archivo CSV en un DataFrame de Pandas
data = pd.read_csv(file_path, encoding='latin1')

@app.route('/')
def index():
    # Seleccionar una muestra aleatoria de 10 filas del DataFrame
    muestra_aleatoria = data.sample(n=10)

    # Generar gráficos para cada mes en la muestra aleatoria
    plots = []
    for mes in ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE']:
        plt.figure(figsize=(8, 6))
        plt.bar(range(len(muestra_aleatoria)), muestra_aleatoria[f'CONSUMO_KWH_{mes}'], color='skyblue')
        plt.title(f'Consumo de energía en {mes}')
        plt.xlabel('Muestra')
        plt.ylabel('Consumo de energía (kWh)')
        plt.xticks(range(len(muestra_aleatoria)), muestra_aleatoria.index)  
        plt.grid(True)

        # Convertir el gráfico a formato base64 para mostrarlo en HTML
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        img_str = base64.b64encode(buffer.read()).decode('utf-8')
        plots.append(img_str)
        plt.close()

    return render_template('index.html', plots=plots)

if __name__ == '__main__':
    app.run(debug=True)
