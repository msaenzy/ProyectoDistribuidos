import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Ruta al archivo CSV
file_path = 'energia.csv'

# Cargar todos los registros de datos del archivo CSV en un DataFrame de Pandas
data = pd.read_csv(file_path)

# Seleccionar las columnas de consumo de energía de enero a octubre y la columna de parroquia
columnas_consumo_energia = ['CONSUMO_KWH_ENERO', 'CONSUMO_KWH_FEBRERO', 'CONSUMO_KWH_MARZO', 'CONSUMO_KWH_ABRIL',
                            'CONSUMO_KWH_MAYO', 'CONSUMO_KWH_JUNIO', 'CONSUMO_KWH_JULIO', 'CONSUMO_KWH_AGOSTO',
                            'CONSUMO_KWH_SEPTIEMBRE', 'CONSUMO_KWH_OCTUBRE']
columna_parroquia = 'PARROQUIA'

# Calcular el total de consumo de energía por mes y parroquia
consumo_energia_por_mes_y_parroquia = data.groupby(columna_parroquia)[columnas_consumo_energia].sum()

# Meses de enero a octubre
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre']

# Obtener una paleta de colores de seaborn
paleta_colores = sns.color_palette("husl", len(meses))

def plot_graph(parroquia):
    consumo_energia = consumo_energia_por_mes_y_parroquia.loc[parroquia]
    plt.figure(figsize=(14, 6))
    plt.bar(meses, consumo_energia, color=paleta_colores)
    plt.title(f'Total de Consumo de Energía para la Parroquia: {parroquia}')
    plt.xlabel('Mes')
    plt.ylabel('Total de Consumo de Energía (kWh)')
    plt.xticks(rotation=45)
    plt.savefig(f'static/{parroquia}_consumo_energia_por_mes.png')  # Guardar la imagen como PNG en la carpeta static
    plt.close()  # Cerrar la figura para liberar memoria

# Generar imágenes para todas las parroquias
for parroquia in consumo_energia_por_mes_y_parroquia.index:
    plot_graph(parroquia)
