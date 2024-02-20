import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Ruta al archivo CSV
file_path = 'energia.csv'

# Cargar todos los registros de datos del archivo CSV en un DataFrame de Pandas
data = pd.read_csv(file_path)

# Seleccionar las columnas de consumo de energía de enero a octubre y la columna de cantón
columnas_consumo_energia = ['CONSUMO_KWH_ENERO', 'CONSUMO_KWH_FEBRERO', 'CONSUMO_KWH_MARZO', 'CONSUMO_KWH_ABRIL',
                            'CONSUMO_KWH_MAYO', 'CONSUMO_KWH_JUNIO', 'CONSUMO_KWH_JULIO', 'CONSUMO_KWH_AGOSTO',
                            'CONSUMO_KWH_SEPTIEMBRE', 'CONSUMO_KWH_OCTUBRE']
columna_canton = 'CANTON'

# Calcular el total de consumo de energía por mes y cantón
consumo_energia_por_mes_y_canton = data.groupby(columna_canton)[columnas_consumo_energia].sum()

# Meses de enero a octubre
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre']

# Obtener una paleta de colores de seaborn
paleta_colores = sns.color_palette("husl", len(meses))

def plot_graph(canton):
    consumo_energia = consumo_energia_por_mes_y_canton.loc[canton]
    plt.figure(figsize=(8, 8))
    plt.pie(consumo_energia, labels=meses, colors=paleta_colores, autopct='%1.1f%%', startangle=140)
    plt.title(f'Distribución del Consumo de Energía para el Cantón: {canton}')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig(f'static/{canton}_consumo_energia_por_mes_pie.png')  # Guardar la imagen como PNG en la carpeta static
    plt.close()  # Cerrar la figura para liberar memoria

# Generar imágenes para todos los cantones
for canton in consumo_energia_por_mes_y_canton.index:
    plot_graph(canton)
