class DataValidatorAgent:
    def run(self, df):
        assert "stock_symbol" in df.columns, "Missing column: stock_symbol"
        assert df["transaction_type"].isin(["BUY", "SELL"]).all(), "Invalid transaction types"
        assert (df["quantity"] > 0).all(), "Quantity must be positive"
        print("[ValidatorAgent] Basic validation passed ✅")
        return df
