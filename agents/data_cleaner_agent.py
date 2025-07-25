class DataCleanerAgent:
    def run(self, df):
        df = df.dropna()
        df = df[df["quantity"] > 0]
        print("[CleanerAgent] Cleaned finance data. Shape:", df.shape)
        return df
