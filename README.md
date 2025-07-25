
# AI-Agent Driven Data Engineering Pipeline 🚀

This is a GitHub-ready starter project using **CrewAI** and **LangGraph** to build a modular data pipeline with AI agents for:
- Data ingestion
- Cleaning
- Validation
- Loading
- Monitoring

## 🧱 Tech Stack
- CrewAI (LLM agent framework)
- LangGraph + LangChain
- Airbyte (data ingestion)
- DuckDB (storage)
- Great Expectations (data validation)
- Prefect (orchestration)
- Open-source LLM (Ollama, LLaMA.cpp)

## 📁 Structure
```
.
├── agents/               # LLM agent definitions (CleanerAgent, ValidatorAgent, etc.)
├── data/                 # Raw and processed data
├── pipelines/            # Modular pipeline stages
├── config/               # Agent and tool configurations
├── utils/                # Helper functions
├── orchestration/        # Prefect flows or Airflow DAGs
├── models/               # Trained models or embeddings
├── logs/                 # Logs and artifacts
└── README.md             # This file
```

## 🧠 Example Agent: CleanerAgent
Located in `agents/cleaner_agent.py`, it uses a local LLM via CrewAI to remove nulls and standardize columns.

## 📦 Setup
```bash
git clone https://github.com/yourusername/ai_agent_data_pipeline.git
cd ai_agent_data_pipeline
pip install -r requirements.txt
```

## ⚙️ Run Pipeline
```bash
python orchestration/run_pipeline.py
```

Enjoy building AI-powered data workflows!
