# Space Debris Analysis & Satellite Intelligence

## Project Overview
Este proyecto implementa un pipeline de datos robusto, modular y orientado a objetos (POO) diseñado para la ingesta, limpieza, enriquecimiento y modelado predictivo de la base de datos global de satélites de la **UCS (Union of Concerned Scientists)**. El sistema automatiza el procesamiento ETL de activos espaciales y basura tecnológica, transformando datos crudos semiestructurados en insights estratégicos y proyecciones visuales de alta resolución para la toma de decisiones en el sector aeroespacial.

## Objectives
* **Automatizar el Flujo ETL:** Construir un orquestador centralizado que gestione la ingesta defensiva y la transformación de datos crudos sin intervención manual.
* **Optimizar la Dimensionalidad:** Filtrar y limpiar el espectro de variables para priorizar los atributos de mayor impacto analítico y de negocio.
* **Garantizar la Resiliencia del Software:** Diseñar mecanismos de escape para decodificar archivos con estructuras complejas, encodings mixtos y registros corruptos.
* **Desplegar Inteligencia Predictiva:** Desarrollar un modelo de proyección temporal basado en tendencias analíticas para estimar el crecimiento de lanzamientos de la era *New Space*.

## Dataset
El proyecto se alimenta del dataset oficial de la **UCS Satellite Database**. Debido a su origen y entornos de actualización, el archivo crudo (`ucs_satellites.txt`) presenta desafíos de ingeniería de datos críticos:
* **Volumen:** +7,500 registros con 67 columnas iniciales.
* **Estructura:** Delimitación por tabulaciones (`\t`) combinada con líneas de metadatos o comentarios introductorios.
* **Calidad:** Presencia de caracteres especiales de Windows, tipos de datos mezclados (strings con comas en métricas numéricas) y valores nulos generalizados en variables experimentales.

## Technologies
* **Python 3.10+** (Núcleo de desarrollo y programación orientada a objetos)
* **Pandas:** Ingeniería de características, filtrado matricial y transformaciones de esquemas.
* **NumPy:** Computación numérica y ajuste polinomial para regresiones lineales.
* **Matplotlib & Seaborn:** Renderizado estadístico y diseño de la interfaz gráfica de reportes.

## Project Structure
```text
space-debris-datascience/
│
├── data/
│   ├── raw/                # Archivo crudo original (ucs_satellites.txt)
│   └── processed/          # Dataset limpio (demo_clean_features.csv) y PNGs exportados
│
├── src/                    # Módulos especializados de la arquitectura
│   ├── __init__.py
│   ├── cleaning.py         # Lógica de tipado, reducción y limpieza de datos
│   ├── features.py         # Lógica de ingeniería de variables derivadas
│   └── viz.py              # Laboratorio de renderizado gráfico
│
├── eda.ipynb               # Jupyter Notebook para pruebas interactivas y análisis visual
├── main.py                 # Orquestador del Pipeline (Clase Maestra POO)
└── README.md               # Documentación ejecutiva del proyecto