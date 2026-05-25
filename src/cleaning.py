import pandas as pd


class DataCleaner:
    """
    Clase encargada de limpieza de datos del dataset UCS Satellites.
    """

    def __init__(self):
        pass

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        
        df = df.copy()

        # 1. Normalizar nombres de columnas
        df.columns = df.columns.str.strip()

        # 2. Limpieza de strings con comas (ej: "1,000")
        object_cols = df.select_dtypes(include="object").columns

        for col in object_cols:
            df[col] = df[col].astype(str).str.replace(",", "", regex=False)

        # 3. Intentar conversión a numérico cuando sea posible
        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        # 4. Eliminar duplicados
        df = df.drop_duplicates()

        # -----------------------------
        # FORZAR TIPOS NUMÉRICOS CLAVE
        # -----------------------------

        numeric_columns = [
            "Launch Mass (kg.)",
            "Apogee (km)",
            "Perigee (km)"
        ]

        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")
        # asegurar consistencia en fechas si existen
        date_cols = [col for col in df.columns if "date" in col.lower()]

        for col in date_cols:
            df[col] = pd.to_datetime(df[col], errors="coerce")
        
        df["Country of Operator/Owner"] = (
            df["Country of Operator/Owner"]
            .astype(str)
            .str.strip()
            .replace("nan", pd.NA)
        )
        
        
        
        
        return df