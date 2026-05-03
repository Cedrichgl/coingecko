# 🪙 Crypto Data API (CoinGecko)

A simple data pipeline and API to collect, process, and expose cryptocurrency data.

Built using CoinGecko API, pandas, and FastAPI.

---

## 🚀 Overview

This project:

* fetches crypto data from CoinGecko
* cleans and processes the data
* stores it in a database
* exposes it through an API

Designed for data analysis and reusable pipelines.

---

## 🔄 Workflow

```text id="5mz8qp"
[Data Source]
(CoinGecko API)
        │
        ▼
[Data Collection]
(requests)
        │
        ▼
[Data Processing]
(pandas)
        │
        ▼
[Data Modeling]
(SQLAlchemy)
        │
        ▼
[Database]
(PostgreSQL)
        │
        ▼
[Migrations]
(Alembic)
        │
        ▼
[API Layer]
(FastAPI)
        │
        ▼
Client / Analysis / Dashboard
```

---

## 🧱 Architecture

* **Data Collection**
  Fetches raw data from CoinGecko API

* **Processing Layer (pandas)**
  Cleans and transforms data

* **Modeling Layer (SQLAlchemy)**
  Structures data into database models

* **Database (PostgreSQL)**
  Stores processed data

* **Migrations (Alembic)**
  Handles schema updates

* **API Layer (FastAPI)**
  Exposes data to clients

---

## 🧪 Example Flow

```text id="g1k7sz"
Fetch crypto prices
→ Clean data (pandas)
→ Store in database
→ Access via API endpoint
```

---

## 📦 Tech Stack

* CoinGecko API
* pandas
* SQLAlchemy
* Alembic
* PostgreSQL
* FastAPI

---

## 🎯 Use Cases

* Crypto data analysis
* Dashboards
* Data pipelines
* API for financial apps

---

## ⚙️ Installation

```bash id="r9x2dl"
git clone https://github.com/Cedrichgl/coingecko.git
cd coingecko
pip install -r requirements.txt
```

