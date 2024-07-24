
---
title: "Visualización de Datos con Seaborn esteba navarro"
author: "Tu Nombre"
date: "Fecha"
format: pdf
---

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



# Cargar los datos
file_path = r'C:\Users\f\Documents\avdata\nayib\base sns.xlsx'
data = pd.read_excel(file_path, sheet_name='Hoja1')

# Calcular el total de ventas por categoría y ordenar por tamaño
ventas_por_categoria = data.groupby('Categoria')['Venta'].sum().sort_values(ascending=False).reset_index()

# Ordenar las categorías según el total de ventas
ordered_data = data.copy()
ordered_data['Categoria'] = pd.Categorical(ordered_data['Categoria'], categories=ventas_por_categoria['Categoria'], ordered=True)

# Calcular las dos categorías con mayores ventas
top_categories = ventas_por_categoria.nlargest(2, 'Venta')['Categoria']

# Definir la paleta de colores con colores específicos para 'Vinos', 'Platos Fuertes', y las dos categorías con mayores ventas
default_color = 'lightgray'
highlight_color = 'darkorange'
palette = {cat: default_color for cat in ordered_data['Categoria'].unique()}
palette.update({
    'Vinos': 'darkred',
    'Platos Fuertes': 'darkblue',
    top_categories.iloc[0]: highlight_color,
    top_categories.iloc[1]: highlight_color
})

# Crear el gráfico categórico ordenado y con colores específicos
plt.figure(figsize=(10, 6))
cat_plot = sns.barplot(
    x='Categoria', 
    y='Venta', 
    data=ordered_data, 
    estimator=sum, 
    ci=None, 
    palette=palette,
    order=ventas_por_categoria['Categoria']
)
cat_plot.set_title('Total de Ventas por Categoría de Producto')
cat_plot.set_xlabel('Categoría')
cat_plot.set_ylabel('Total de Ventas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico relacional: Relación entre el precio y el importe de la venta
plt.figure(figsize=(8, 5))
rel_plot = sns.scatterplot(x='Precio', y='Venta', data=ordered_data, hue='Categoria', palette='muted')
rel_plot.set_title('Relación entre el Precio y el Importe de la Venta')
rel_plot.set_xlabel('Precio')
rel_plot.set_ylabel('Venta')
plt.xlim(0, ordered_data['Precio'].max() + 1)
plt.ylim(0, ordered_data['Venta'].max() + 10)
plt.tight_layout()
plt.show()

# Gráfico de distribución: Distribución del importe de las ventas
plt.figure(figsize=(10, 6))
dist_plot = sns.histplot(ordered_data['Venta'], kde=True, color='skyblue')
dist_plot.set_title('Distribución del Importe de las Ventas')
dist_plot.set_xlabel('Venta')
dist_plot.set_ylabel('Frecuencia')
plt.tight_layout()
plt.show()