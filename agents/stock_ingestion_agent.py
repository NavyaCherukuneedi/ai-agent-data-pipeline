import yfinance as yf
import pandas as pd

class StockIngestionAgent:
    def __init__(self, symbols=["AAPL", "MSFT", "GOOGL"]):
        self.symbols = symbols

    def run(self, period="5d", interval="1h"):
        all_data = []
        for symbol in self.symbols:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period=period, interval=interval)
            hist.reset_index(inplace=True)
            hist["symbol"] = symbol
            all_data.append(hist)

        df = pd.concat(all_data, ignore_index=True)
        print(f"[StockIngestionAgent] Pulled {len(df)} rows of stock data.")
        return df
