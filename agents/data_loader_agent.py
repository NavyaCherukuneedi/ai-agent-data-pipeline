import duckdb

class DataLoaderAgent:
    def run(self, df):
        con = duckdb.connect("data_pipeline.duckdb")
        # Load dataframe using DuckDB's relation API
        con.register("temp_df", df)
        con.execute("CREATE OR REPLACE TABLE transactions AS SELECT * FROM temp_df")
        con.unregister("temp_df")
        print("[LoaderAgent] Loaded data into DuckDB table 'transactions'")

