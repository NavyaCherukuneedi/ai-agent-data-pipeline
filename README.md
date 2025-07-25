AI Agent-Driven Finance Data Pipeline & Dashboard
This project demonstrates how to build an end-to-end data pipeline using AI agents, focused on real-time financial data. The architecture includes data ingestion via Yahoo Finance, validation with Great Expectations, local storage using DuckDB, and interactive visualization through Streamlit.

Table of Contents
Project Overview

Architecture Diagram

Tools and Technologies Used

How It Works

Agent Workflow

Setup Instructions

Running the Project

Stock Data Visualization

Sample Dashboard

Contribution

Project Overview
This project simulates a multi-agent data pipeline that:

Ingests real-time stock data (AAPL, GOOGL, MSFT)

Cleans, validates, and stores the data

Displays an interactive Streamlit dashboard for analysis

Demonstrates AI agent collaboration in an ETL workflow

It showcases how AI-driven automation can be applied to financial data engineering pipelines for better scalability, reusability, and observability.

Architecture Diagram

Tools and Technologies Used
Python: Core scripting language

Pandas: Data manipulation and cleaning

DuckDB: In-process analytical SQL engine

Great Expectations: For data validation

yFinance: Real-time stock market data API

Streamlit: Dashboard UI for visualization

Plotly: Interactive charts in Streamlit

CrewAI (optional): For LLM-agent orchestration (future work)

How It Works
The pipeline mimics how AI agents can coordinate to automate a traditional ETL process:

StockIngestionAgent fetches 5 days of hourly price data using yfinance.

DataCleanerAgent removes missing rows and corrects any anomalies.

DataValidatorAgent applies expectations like checking that "transaction_type" is either "BUY" or "SELL".

DataLoaderAgent stores the cleaned data into a DuckDB table.

A Streamlit Dashboard reads from DuckDB and lets users:

View stock performance

Filter by symbol

Explore volume vs OHLC

Compare symbols and % price changes

Agent Workflow
StockIngestionAgent: Calls Yahoo Finance API and returns a unified dataframe

DataCleanerAgent: Drops nulls and duplicates

DataValidatorAgent: Uses Great Expectations to enforce schema expectations

DataLoaderAgent: Writes the result to DuckDB in a table called transactions

Setup Instructions
Prerequisites:
Python 3.10 (not 3.12+ due to dependency issues with Great Expectations)

pip, streamlit, duckdb installed

Optional: VS Code

Clone the Repo
git clone https://github.com/NavyaCherukuneedi/ai-agent-data-pipeline.git
cd ai-agent-data-pipeline
Install Requirements
bash
pip install -r requirements.txt
Or manually:
pip install pandas duckdb yfinance streamlit plotly great_expectations
Running the Project
1. Run the ETL Pipeline

export PYTHONPATH=.
python orchestration/run_pipeline.py

2. Run the Streamlit Dashboard

streamlit run stock_dashboard.py
Make sure no other process is locking data_pipeline.duckdb


Stock Data Visualization
The dashboard lets you:

Select stock symbols (AAPL, GOOGL, MSFT)

View % change over time

Plot line charts or candlestick (OHLC) graphs

Analyze volume overlaid with price action



