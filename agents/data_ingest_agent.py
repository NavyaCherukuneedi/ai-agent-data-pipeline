import pandas as pd

class DataIngestAgent:
    def run(self):
        df = pd.read_csv("finance_data.csv", parse_dates=["timestamp"])
        print("[IngestAgent] Loaded finance data:", df.shape)
        return df

