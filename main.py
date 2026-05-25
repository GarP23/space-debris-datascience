# main.py
import os
import sys
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from src.cleaning import limpieza_datos
from src.features import construccion_caracteristicas_de_satelites
from src.viz import satelite_distribucion_graf, exentricidad_orbita_graf, plot_geopolitica, proyeccion_tiempo_graf

class PipelineAnalisisSatelites:
    def __init__(self, nombre_archivo='ucs_satellites.txt', es_crudo=True):
        subcarpeta = 'raw' if es_crudo else 'processed'
        self.ruta_origen = os.path.join(BASE_DIR, 'data', subcarpeta, nombre_archivo)
        self.carpeta_destino = os.path.join(BASE_DIR, 'data', 'processed')
        self.df = None
        os.makedirs(self.carpeta_destino, exist_ok=True)

    def ejecutar_pipeline(self):
        print("=" * 60)
        print("🚀 INICIANDO PIPELINE DE DATOS (ARQUITECTURA CLASE POO)")
        print("=" * 60)
        
        try:
            if not os.path.exists(self.ruta_origen):
                raise FileNotFoundError(f"No se encontró el archivo en: {self.ruta_origen}")
            
            print(f"[INFO] Cargando registros desde: {self.ruta_origen}")
            
            # Carga directa y segura usando latin-1 y tabulador que dio éxito en tu consola
            self.df = pd.read_csv(self.ruta_origen, sep='\t', on_bad_lines='skip', low_memory=False, encoding='latin-1')
                
            print(f"[ÉXITO] Datos base cargados. Dimensiones crudas: {self.df.shape}")
            
            # 2. LIMPIEZA PROFUNDA (Aquí reduce automáticamente a tus 35 columnas)
            print("[INFO] Ejecutando módulo de limpieza y reducción a 35 columnas...")
            self.df = limpieza_datos(self.df)
            print(f"[ÉXITO] Estructura limpia alineada al Notebook. Dimensiones: {self.df.shape}")
            
            # 3. INGENIERÍA DE CARACTERÍSTICAS
            print("[INFO] Construyendo variables derivadas...")
            self.df = construccion_caracteristicas_de_satelites(self.df)
            
            # 4. EXPORTACIÓN DE RESULTADOS
            archivo_salida = os.path.join(self.carpeta_destino, 'demo_clean_features.csv')
            self.df.to_csv(archivo_salida, index=False, encoding='utf-8')
            print(f"[ÉXITO] Dataset exportado a: {archivo_salida}")
            
            # 5. GENERACIÓN Y GUARDADO DE GRÁFICOS
            print("[INFO] Renderizando laboratorio gráfico analítico y predictivo...")
            
            fig1 = satelite_distribucion_graf(self.df)
            fig1.savefig(os.path.join(self.carpeta_destino, '01_distribucion_orbitas.png'))
            
            fig2 = exentricidad_orbita_graf(self.df)
            fig2.savefig(os.path.join(self.carpeta_destino, '02_analisis_excentricidad.png'))
            
            fig3 = plot_geopolitica(self.df)
            fig3.savefig(os.path.join(self.carpeta_destino, '03_geopolitica_espacial.png'))
            
            fig4 = proyeccion_tiempo_graf(self.df)
            fig4.savefig(os.path.join(self.carpeta_destino, '04_proyeccion_tendencias.png'))
            
            print(f"[ÉXITO] Todos los gráficos se guardaron en: {self.carpeta_destino}")
            print("\n" + "=" * 60)
            print("🎯 ¡EJECUCIÓN DEL PIPELINE FINALIZADA CON ÉXITO!")
            print("=" * 60)
            
        except Exception as e:
            print(f"\n❌ [ERROR CRÍTICO CONTROLADO]: {str(e)}")

if __name__ == '__main__':
    pipeline = PipelineAnalisisSatelites(nombre_archivo='ucs_satellites.txt', es_crudo=True)
    pipeline.ejecutar_pipeline()