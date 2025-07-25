from agents.data_ingest_agent import DataIngestAgent
from agents.data_cleaner_agent import DataCleanerAgent
from agents.data_validator_agent import DataValidatorAgent
from agents.data_loader_agent import DataLoaderAgent
from agents.stock_ingestion_agent import StockIngestionAgent

import duckdb

def main():
    print("🚀 Starting Finance Data Pipeline")

    
    ingest_agent = DataIngestAgent()
    cleaner_agent = DataCleanerAgent()
    validator_agent = DataValidatorAgent()
    loader_agent = DataLoaderAgent()

    df = ingest_agent.run()
    df = cleaner_agent.run(df)
    df = validator_agent.run(df)
    loader_agent.run(df)

    #Real-Time Stock
    print("\n📈 Starting Stock Ingestion Agent")
    stock_agent = StockIngestionAgent(symbols=["AAPL", "MSFT", "GOOGL"])
    stock_df = stock_agent.run(period="1d", interval="30m")

    
    con = duckdb.connect("data_pipeline.duckdb")
    con.register("stock_df", stock_df)
    con.execute("CREATE OR REPLACE TABLE stock_prices AS SELECT * FROM stock_df")
    con.unregister("stock_df")

    print("✅ Stock data loaded into DuckDB table: stock_prices")
    print("✅ All pipelines completed successfully!")

if __name__ == "__main__":
    main()
