import pandas as pd


class FeatureEngineer:

    def __init__(self):
        pass

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:

        df = df.copy()

        df["Date of Launch"] = pd.to_datetime(
            df["Date of Launch"], 
            format='mixed',
            errors='coerce'
        )
        df["launch_year"] = df["Date of Launch"].dt.year

        if "Launch Mass (kg.)" in df.columns:

            df["Launch Mass (kg.)"] = pd.to_numeric(
                df["Launch Mass (kg.)"],
                errors="coerce"
            )

            df["mass_category"] = pd.cut(
                df["Launch Mass (kg.)"],
                bins=[0, 500, 1000, 5000, 20000, float("inf")],
                labels=["micro", "small", "medium", "large", "heavy"]
            )

        if "Perigee (km)" in df.columns and "Apogee (km)" in df.columns:
            df["Apogee (km)"] = pd.to_numeric(df["Apogee (km)"], errors="coerce")
            df["Perigee (km)"] = pd.to_numeric(df["Perigee (km)"], errors="coerce")

            df["orbit_range"] = df["Apogee (km)"] - df["Perigee (km)"]

        if "Launch Mass (kg.)" in df.columns:
            df["mass_normalized"] = (
                df["Launch Mass (kg.)"] - df["Launch Mass (kg.)"].mean()
            ) / df["Launch Mass (kg.)"].std()

        return df