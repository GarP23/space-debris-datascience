# src/cleaning.py
import pandas as pd

def limpieza_datos(df):
    # 1. Definimos las 35 columnas exactas que tú seleccionaste en tu Notebook
    columnas_reducidas = [
        'Current Official Name of Satellite', 'Country/Org of UN Registry', 
        'Country of Operator/Owner', 'Operator/Owner', 'Users', 'Purpose', 
        'Detailed Purpose', 'Class of Orbit', 'Type of Orbit', 'Longitude of GEO (degrees)', 
        'Perigee (km)', 'Apogee (km)', 'Eccentricity', 'Inclination (degrees)', 
        'Period (minutes)', 'Launch Mass (kg.)', 'Dry Mass (kg.)', 'Power (watts)', 
        'Date of Launch', 'Expected Lifetime (yrs.)', 'Contractor', 'Country of Contractor', 
        'Launch Site', 'Launch Vehicle', 'COSPAR Number', 'NORAD Number', 'Comments', 
        'Source Used for Orbital Data', 'Source', 'Source.1', 'Source.2', 'Source.3', 
        'Source.4', 'Source.5', 'Source.6'
    ]
    
    # Nos aseguramos de limpiar espacios ocultos en los nombres de columnas que vienen del TXT
    df.columns = df.columns.str.strip()
    
    # Filtramos el DataFrame para quedarnos únicamente con tus 35 columnas
    # Si alguna columna por error del TXT no se encuentra, la ignoramos de forma segura
    columnas_presentes = [col for col in columnas_reducidas if col in df.columns]
    df_limpieza = df[columnas_presentes].copy()
    
    # 2. Tu bloque de conversión numérica exacto
    columnas_numericas_a_tratar = [
        'Perigee (km)', 'Apogee (km)', 'Eccentricity', 
        'Inclination (degrees)', 'Launch Mass (kg.)',
        'Period (minutes)', 'Dry Mass (kg.)', 'Power (watts)'
    ]
    
    for columnas in columnas_numericas_a_tratar:
        if columnas in df_limpieza.columns:
            cambio_comas = df_limpieza[columnas].astype(str).str.replace(',', '', regex=False).str.strip()
            df_limpieza[columnas] = pd.to_numeric(cambio_comas, errors='coerce')

    # 3. Tus conversiones de fechas e identificadores
    if 'Date of Launch' in df_limpieza.columns:
        df_limpieza['Date of Launch'] = pd.to_datetime(df_limpieza['Date of Launch'], errors='coerce')
        
    if 'NORAD Number' in df_limpieza.columns:
        df_limpieza['NORAD Number'] = df_limpieza['NORAD Number'].astype(str)
        
    if 'COSPAR Number' in df_limpieza.columns:
        df_limpieza['COSPAR Number'] = df_limpieza['COSPAR Number'].astype(str)
        
    # Ordenamos cronológicamente si existe la fecha
    if 'Date of Launch' in df_limpieza.columns:
        df_limpieza = df_limpieza.sort_values(by='Date of Launch', ascending=True)
        
    return df_limpieza