# src/viz.py
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def satelite_distribucion_graf(df):
    plt.figure(figsize=(10, 5))
    
    # Sincronizamos con las etiquetas reales creadas en features.py
    orden_orbitas = ['LEO (Low Earth)', 'MEO (Medium Earth)', 'GEO (Geostationary)', 'Unknown']
    
    ax = sns.countplot(
        data=df,
        x='Orbit_Class_Extended',
        hue='Orbit_Class_Extended',
        palette='viridis',
        order=orden_orbitas,
        legend=False
    )

    plt.title('Distribución Global de Objetos Espaciales por Tipo de Órbita', pad=15, fontweight='bold')
    plt.xlabel('Clasificación Física de la Órbita')
    plt.ylabel('Cantidad Total de Satélites')
    
    for p in ax.patches:
        height = p.get_height()
        if not np.isnan(height) and height > 0:
            ax.annotate(f'{int(height)}', (p.get_x() + p.get_width()/2. , height),
                        ha='center', va='center', xytext=(0, 8), textcoords='offset points', fontweight='bold')

    plt.tight_layout()
    return plt.gcf()


def exentricidad_orbita_graf(df):
    plt.figure(figsize=(10, 5))
    
    # Sincronizamos con los nombres de columna reales post-limpieza
    x_col = 'Perigee (km)'
    y_col = 'Apogee (km)'
    
    # Filtramos la órbita LEO de forma segura evitando romper si hay nulos
    df_leo = df[df[x_col] <= 2000].dropna(subset=[x_col, y_col, 'Mass_Category'])
    
    sns.scatterplot(
        data=df_leo, 
        x=x_col, 
        y=y_col, 
        hue='Mass_Category', 
        palette='magma', 
        alpha=0.6
    )
    
    plt.title('Análisis de Excentricidad en Órbita Baja (LEO)', pad=15, fontweight='bold')
    plt.xlabel('Perigeo (km)')
    plt.ylabel('Apogeo (km)')
    plt.legend(title='Categoría de Masa')
    plt.tight_layout()
    return plt.gcf()


def plot_geopolitica(df):
    plt.figure(figsize=(10, 5))
    
    top_paises = df['Country of Operator/Owner'].value_counts().head(10)

    ax = sns.barplot(
        x=top_paises.values, 
        y=top_paises.index, 
        hue=top_paises.index,
        palette='plasma',
        legend=False
    )

    plt.title('Top 10 Países con Mayor Presencia en el Espacio', pad=15, fontweight='bold')
    plt.xlabel('Cantidad Total de Satélites Activos / Chatarra')
    plt.ylabel('País del Operador/Dueño')

    for index, value in enumerate(top_paises.values):
        plt.text(value, index, f' {int(value)}', va='center', fontweight='bold')

    plt.tight_layout()
    return plt.gcf()


def proyeccion_tiempo_graf(df):
    df_copy = df.copy()
    
    # Convertimos la fecha de lanzamiento de forma segura para extraer el año
    df_copy['Launch_Year'] = pd.to_datetime(df_copy['Date of Launch'], errors='coerce').dt.year
    conteo_anual = df_copy.groupby('Launch_Year').size().reset_index(name='Lanzamientos')
    
    # Ventana temporal del New Space (2019-2026)
    df_trend = conteo_anual[(conteo_anual['Launch_Year'] >= 2019) & (conteo_anual['Launch_Year'] <= 2026)].dropna()
    
    X = df_trend['Launch_Year'].values
    y = df_trend['Lanzamientos'].values
    
    # Modelo predictivo por regresión lineal
    m, c = np.polyfit(X, y, 1)
    
    anios_proyeccion = np.array(list(range(2019, 2037)))
    valores_proyectados = m * anios_proyeccion + c

    plt.figure(figsize=(12, 6))
    plt.plot(conteo_anual['Launch_Year'], conteo_anual['Lanzamientos'], marker='o', label='Histórico Real', color='#1f77b4', linewidth=2)
    plt.plot(anios_proyeccion, valores_proyectados, linestyle='--', color='red', label='Proyección Predictiva (Tendencia New Space)', linewidth=2)
    
    # Hito matemático para la defensa de tu perfil analítico
    hito_anio = 2035
    hito_prediccion = m * hito_anio + c
    plt.scatter(hito_anio, hito_prediccion, color='black', s=100, zorder=5)
    plt.axvline(x=hito_anio, color='gray', linestyle=':', alpha=0.7)
    plt.text(hito_anio - 0.5, hito_prediccion + 100, f'Hito 2035:\n~{int(hito_prediccion)} lanzamientos/año', ha='right', fontweight='bold')

    plt.title('Modelo de Proyección Temporal: Crecimiento de Lanzamientos Futuros', pad=15, fontweight='bold')
    plt.xlabel('Año de Lanzamiento')
    plt.ylabel('Cantidad de Satélites Lanzados al Año')
    plt.xlim(2010, 2036)
    plt.legend(loc='upper left')
    plt.tight_layout()
    return plt.gcf()