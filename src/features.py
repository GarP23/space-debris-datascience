# src/features.py
import pandas as pd
import numpy as np

def construccion_caracteristicas_de_satelites(df):
    
    df_caracteristicas = df.copy()
    
    if 'Date of Launch' in df_caracteristicas.columns:
        año_lanzamiento = pd.to_datetime(df_caracteristicas['Date of Launch']).dt.year
        df_caracteristicas['Age_In_Orbit_Years'] = 2026 - año_lanzamiento
    
    if 'Perigee (km)' in df_caracteristicas.columns:
        condiciones = [
            (df_caracteristicas['Perigee (km)'] < 2000),
            (df_caracteristicas['Perigee (km)'] >= 2000) & (df_caracteristicas['Perigee (km)'] < 35000),
            (df_caracteristicas['Perigee (km)'] >= 35000)
        ]
        opciones = ['LEO (Low Earth)', 'MEO (Medium Earth)', 'GEO (Geostationary)']
        df_caracteristicas['Orbit_Class_Extended'] = np.select(condiciones, opciones, default='Unknown')
        
    if 'Launch Mass (kg.)' in df_caracteristicas.columns:
        df_caracteristicas['Mass_Category'] = np.where(df_caracteristicas['Launch Mass (kg.)'] < 500, 'Lightweight (<500kg)', 'Heavyweight (>=500kg)')
        
    return df_caracteristicas