# Importar las librerías necesarias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar la página principal
st.title("Aplicación de Visualización de Datos")
st.write("Sube un archivo CSV para generar gráficos interactivos.")

# Función para mostrar el contenido del archivo CSV
def mostrar_datos(data):
    st.write("Datos del CSV:")
    st.write(data.head())

# Función para generar un histograma
def graficar_histograma(data, columna, titulo, xlabel, ylabel):
    fig, ax = plt.subplots()
    sns.histplot(data=data, x=columna, kde=True, ax=ax)
    ax.set_title(titulo)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)

# Función para generar un gráfico de barras
def graficar_barras(data, columna, titulo, xlabel, ylabel):
    fig, ax = plt.subplots()
    data[columna].value_counts().plot.bar(ax=ax)
    ax.set_title(titulo)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig)

# Función para generar un gráfico de torta
def graficar_torta(data, columna, titulo):
    fig, ax = plt.subplots()
    data[columna].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
    ax.set_title(titulo)
    ax.set_ylabel('')
    st.pyplot(fig)

# Cargar el archivo CSV
uploaded_file = st.file_uploader("Elige un archivo CSV", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    mostrar_datos(data)
    
    graficar_histograma(data, 'cost_of_the_order', 'Distribución del costo del pedido', 'Costo del pedido', 'Frecuencia')
    graficar_histograma(data, 'food_preparation_time', 'Distribución del tiempo de preparación de la comida', 'Tiempo de preparación', 'Frecuencia')
    graficar_histograma(data, 'delivery_time', 'Distribución del tiempo de entrega', 'Tiempo de entrega', 'Frecuencia')
    
    st.write("Frecuencia de cada restaurante")
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.countplot(y=data['restaurant_name'], order=data['restaurant_name'].value_counts().index, ax=ax)
    ax.set_title('Frecuencia de cada restaurante')
    ax.set_xlabel('Cuenta')
    ax.set_ylabel('Nombre del Restaurante')
    st.pyplot(fig)

    graficar_torta(data, 'cuisine_type', 'Proporción de tipos de cocina')
    graficar_barras(data, 'day_of_the_week', 'Frecuencia de pedidos por día de la semana', 'Día de la semana', 'Cuenta')