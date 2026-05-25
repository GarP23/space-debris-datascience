# Space Debris Analysis

## Descripción General

Este proyecto explora y analiza datos orbitales de satélites utilizando la base de datos de la UCS (Union of Concerned Scientists). El objetivo principal es construir un pipeline completo de análisis de datos capaz de limpiar, transformar, enriquecer y visualizar información relacionada con satélites activos y basura espacial.

El proyecto combina análisis exploratorio de datos (EDA), ingeniería de características y procesamiento automatizado mediante una arquitectura modular en Python. El resultado final es un flujo de trabajo reproducible que transforma registros satelitales crudos en datasets estructurados y visualizaciones analíticas.

---

## Objetivos

* Construir un pipeline para el procesamiento de datos satelitales.
* Limpiar y estandarizar datasets orbitales en formato crudo.
* Detectar inconsistencias, valores nulos y problemas de formato.
* Generar variables derivadas útiles para el análisis.
* Explorar tendencias relacionadas con lanzamientos y actividad orbital.
* Crear visualizaciones que permitan comprender mejor la evolución del ecosistema espacial.

---

## Dataset

El proyecto utiliza la base de datos oficial de satélites de la UCS.

El dataset original contiene más de 7.500 registros y más de 60 variables relacionadas con:

* información de lanzamiento,
* parámetros orbitales,
* operadores y países,
* propósito de los satélites,
* estado operativo,
* métricas de masa y altitud.

El dataset presenta además varios desafíos de calidad de datos, incluyendo:

* tipos de datos mezclados,
* valores nulos,
* inconsistencias de formato,
* columnas numéricas almacenadas como texto,
* problemas de codificación de caracteres especiales.

---

## Tecnologías Utilizadas

* Python 3.10+
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Estructura del Proyecto

```text
space-debris-datascience/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── __init__.py
│   ├── cleaning.py
│   ├── features.py
│   └── viz.py
│
├── notebooks/
│   └── eda.ipynb
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Pipeline de Datos

El pipeline está organizado en varias etapas:

1. Ingesta de datos crudos
2. Limpieza y preprocesamiento
3. Ingeniería de características
4. Análisis exploratorio de datos
5. Generación de visualizaciones
6. Exportación de datasets procesados

El proyecto sigue una estructura modular para mejorar la legibilidad, el mantenimiento y la reproducibilidad.

---

## Análisis Exploratorio de Datos (EDA)

El análisis exploratorio se centra en:

* evaluación de calidad de datos,
* análisis de valores nulos,
* distribución de variables,
* tendencias de lanzamientos a lo largo del tiempo,
* características orbitales,
* actividad por países y operadores.

Se generaron distintas visualizaciones para apoyar el análisis e identificar patrones relevantes dentro del dataset.

---

## Ingeniería de Características

Se crearon variables derivadas para aumentar el valor analítico del dataset, incluyendo:

* antigüedad de satélites en órbita,
* clasificación orbital,
* métricas numéricas normalizadas,
* variables derivadas de lanzamiento.

---

## Principales Hallazgos

Algunos resultados relevantes del análisis incluyen:

* Crecimiento significativo de lanzamientos durante la era New Space.
* Alta concentración de satélites en órbita baja terrestre (LEO).
* Incremento de operadores comerciales en la última década.
* Presencia de registros incompletos o inconsistentes en variables experimentales.

---

## Cómo Ejecutar el Proyecto

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar el pipeline principal:

```bash
python main.py
```

---

## Posibles Mejoras Futuras

Algunas extensiones futuras del proyecto podrían incluir:

* modelos de machine learning para predicción de tendencias,
* detección de anomalías,
* dashboards interactivos,
* visualizaciones geoespaciales orbitales,
* generación automática de reportes.
