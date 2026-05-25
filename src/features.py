import pandas as pd


class FeatureEngineer:
    """
    Generación de variables derivadas para análisis de satélites.
    """

    def __init__(self):
        pass

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Pipeline de feature engineering.
        """

        df = df.copy()

        # 1. Feature: edad del satélite (si existe año de lanzamiento)
        if "Date of Launch" in df.columns:
            df["Date of Launch"] = pd.to_datetime(
                df["Date of Launch"],
                errors="coerce",
                infer_datetime_format=True
            )
            df["launch_year"] = df["Date of Launch"].dt.year

        # 2. Feature: clasificación simple por masa
        if "Launch Mass (kg.)" in df.columns:

            # 1. Forzar conversión a numérico (limpieza defensiva)
            df["Launch Mass (kg.)"] = pd.to_numeric(
                df["Launch Mass (kg.)"],
                errors="coerce"
            )

            # 2. Crear categorías solo con valores válidos
            df["mass_category"] = pd.cut(
                df["Launch Mass (kg.)"],
                bins=[0, 500, 1000, 5000, 20000, float("inf")],
                labels=["micro", "small", "medium", "large", "heavy"]
            )

        # 3. Feature: ratio orbital simple (si existen columnas)
        if "Perigee (km)" in df.columns and "Apogee (km)" in df.columns:
            # Convertir ambas columnas a numérico de forma segura
            df["Apogee (km)"] = pd.to_numeric(df["Apogee (km)"], errors="coerce")
            df["Perigee (km)"] = pd.to_numeric(df["Perigee (km)"], errors="coerce")

            # Crear feature solo con valores válidos
            df["orbit_range"] = df["Apogee (km)"] - df["Perigee (km)"]

        # 4. Normalización simple de masa (si existe)
        if "Launch Mass (kg.)" in df.columns:
            df["mass_normalized"] = (
                df["Launch Mass (kg.)"] - df["Launch Mass (kg.)"].mean()
            ) / df["Launch Mass (kg.)"].std()

        return df