import pandas as pd


class DataCleaner:

    def __init__(self):
        pass

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        
        df = df.copy()

        df.columns = df.columns.str.strip()

        object_cols = df.select_dtypes(include="object").columns

        for col in object_cols:
            df[col] = df[col].astype(str).str.replace(",", "", regex=False)

        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        df = df.drop_duplicates()

        numeric_columns = [
            "Launch Mass (kg.)",
            "Apogee (km)",
            "Perigee (km)"
        ]

        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

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