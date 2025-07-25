# 📊 AI Agent-Driven Finance Data Pipeline & Dashboard

This project is a complete, real-time **stock monitoring and data engineering pipeline**, built using Python, DuckDB, Streamlit, and AI-style modular agents. It showcases how a modern data stack can be assembled with free, open-source tools — all orchestrated locally.

 ⚡️ Real-time stock data → Cleaned → Validated → Stored → Visualized → Future-ready with LLM agents!

---

## 🧠 What's Inside

### ✅ Modular Agents:
- `DataIngestAgent` – loads local CSV transaction data
- `DataCleanerAgent` – drops nulls and fixes values
- `DataValidatorAgent` – runs schema and value checks
- `DataLoaderAgent` – loads to DuckDB
- `StockIngestionAgent` – fetches real-time stock prices using `yfinance`

### ✅ Storage:
- Uses **DuckDB**, a lightweight but powerful columnar database stored as a local file

### ✅ Visualization:
- **Streamlit dashboard** with:
  - Live data filtering
  - Interactive candlestick charts
  - Volume bar charts
  - % change tracker

---


## ⚙️ Run Pipeline
```bash
python orchestration/run_pipeline.py
```

Enjoy building AI-powered data workflows!
