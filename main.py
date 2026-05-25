from src.cleaning import DataCleaner
from src.features import FeatureEngineer
from src.viz import Visualizer

import pandas as pd
from pathlib import Path


class SpaceDebrisPipeline:

    def __init__(self, raw_path, output_path):
        self.raw_path = Path(raw_path)
        self.output_path = Path(output_path)

        self.data = None
        self.clean_data = None
        self.feature_data = None

        self.cleaner = DataCleaner()
        self.engineer = FeatureEngineer()
        self.viz = Visualizer()

        self.output_path.mkdir(parents=True, exist_ok=True)

    def load_data(self):
        print("[1/5] Loading raw dataset...")

        self.data = pd.read_csv(
            self.raw_path,
            sep=None,
            engine="python",
            encoding="latin1"
        )

        print(f"✔ Data loaded: {self.data.shape}")
        return self

    def clean(self):
        print("[2/5] Cleaning dataset...")

        self.clean_data = self.cleaner.clean(self.data)

        print(f"✔ Clean data: {self.clean_data.shape}")
        return self

    def feature_engineering(self):
        print("[3/5] Engineering features...")

        self.feature_data = self.engineer.transform(self.clean_data)

        print(f"✔ Features created: {self.feature_data.shape}")
        return self

    def run_eda(self):
        print("[4/5] Running EDA and visualizations...")

        self.viz.plot_distributions(self.feature_data)
        self.viz.plot_trends(self.feature_data)
        self.viz.plot_geopolitical_analysis(self.feature_data)

        print("✔ Visualizations generated")
        return self

    def export(self):
        print("[5/5] Exporting outputs...")

        self.feature_data.to_csv(
            self.output_path / "satellites_processed.csv",
            index=False
        )

        print(f"✔ Exported to {self.output_path}")
        return self

    def run(self):
        return (
            self.load_data()
                .clean()
                .feature_engineering()
                .run_eda()
                .export()
        )


if __name__ == "__main__":
    RAW_PATH = "data/raw/ucs_satellites.txt"
    OUTPUT_PATH = "data/processed"

    pipeline = SpaceDebrisPipeline(RAW_PATH, OUTPUT_PATH)
    pipeline.run()