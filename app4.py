import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ruta al archivo CSV
file_path = 'energia.csv'

# Cargar todos los registros de datos del archivo CSV en un DataFrame de Pandas
data = pd.read_csv(file_path)

# Seleccionar las columnas de deudas de enero a octubre y la columna de cantón
columnas_deudas = ['FAC_$_ENERO', 'FAC_$_FEBRERO', 'FAC_$_MARZO', 'FAC_$_ABRIL',
                   'FAC_$_MAYO', 'FAC_$_JUNIO', 'FAC_$_JULIO', 'FAC_$_AGOSTO',
                   'FAC_$_SEPTIEMBRE', 'FAC_$_OCTUBRE']
columna_canton = 'CANTON'

# Calcular el total de deudas por mes y cantón
deudas_por_mes_y_canton = data.groupby(columna_canton)[columnas_deudas].sum()

# Meses de enero a octubre
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre']

# Obtener una paleta de colores de seaborn
paleta_colores = sns.color_palette("husl", len(meses))

def plot_graph(color):
    plt.figure(figsize=(14, 6))
    for canton, deudas in deudas_por_mes_y_canton.iterrows():
        plt.bar(meses, deudas, label=canton, color=paleta_colores)
    
    plt.title('Total de Deuda por Mes y Cantón')
    plt.xlabel('Mes')
    plt.ylabel('Total de Deuda')
    plt.grid(axis='y')
    plt.xticks(rotation=45)
    plt.legend(title='Cantón', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Hacer opacos los barras que no corresponden al color seleccionado
    for barra in plt.gca().patches:
        altura = barra.get_height()
        if altura != 0 and barra.get_facecolor() != paleta_colores[color]:
            barra.set_alpha(0.3)
    
    plt.show()

# Generar gráfico interactivo
plot_graph(0)  # Puedes cambiar el número para seleccionar otro color
