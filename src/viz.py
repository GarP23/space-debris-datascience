import matplotlib.pyplot as plt
import seaborn as sns


class Visualizer:

    def __init__(self):
        pass

    def plot_distributions(self, df):
        numeric_cols = df.select_dtypes(include="number").columns

        for col in numeric_cols[:5]:  # limitamos para no saturar
            plt.figure()
            sns.histplot(df[col].dropna(), kde=True)
            plt.title(f"Distribución de {col}")
            plt.savefig("data/processed/plot.png")
            plt.close()

    def plot_trends(self, df):

        if "launch_year" in df.columns:
            plt.figure()
            df["launch_year"].value_counts().sort_index().plot(kind="line")
            plt.title("Lanzamientos por año")
            plt.xlabel("Año")
            plt.ylabel("Cantidad")
            plt.savefig("data/processed/plot.png")
            plt.close()

    def plot_geopolitical_analysis(self, df):

        if "Country of Operator/Owner" in df.columns:
            plt.figure()
            top_countries = df["Country of Operator/Owner"].dropna().value_counts().head()

            if len(top_countries) > 0:
                top_countries.plot(kind="bar")
            else:
                print("⚠️ No hay datos suficientes para plot de países")


            plt.title("Top países por número de satélites")
            plt.xticks(rotation=45)
            plt.savefig("data/processed/plot.png")
            plt.close()