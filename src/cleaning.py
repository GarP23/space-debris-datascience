import pandas as pd
def limpieza_datos(df):
    # Eliminar filas con valores faltantes
    df_limpieza = df.copy()
    df_limpieza.columns = df_limpieza.columns.strip()
    columnas_numéricas = [
        'Perigee (km)', 'Apogee (km)', 'Eccentricity', 
        'Inclination (degrees)', 'Launch Mass (kg.)',
        'Period (minutes)', 'Dry Mass (kg.)', 'Power (watts)'
    ]
    
    for columna in columnas_numéricas:
        if columna in df_limpieza.columns:
            sin_comas = df_limpieza[columna].astype(str).str.replace(',', '').str.strip()
            df_limpieza[columna] = pd.to_numeric(sin_comas, errors='coerce')

    if 'Date of Launch' in df_limpieza.columns:
        df_limpieza['Date of Launch'] = pd.to_datetime(df_limpieza['Date of Launch'], errors='coerce')
        
    for id_col in ['NORAD Number', 'COSPAR Number']:
        if id_col in df_limpieza.columns:
            df_limpieza[id_col] = df_limpieza[id_col].astype(str)
            
    if 'Date of Launch' in df_limpieza.columns:
        df_limpieza = df_limpieza.sort_values(by='Date of Launch', ascending=True)
        df_limpieza = df_limpieza.reset_index(drop=True)
        
    return df_limpieza