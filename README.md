# Retail Data ETL

A lightweight ETL pipeline for retail sales data. The project reads a CSV file, performs basic cleaning, then attempts to write the results to a MySQL database (as configured in `config/db_config.py`). If the connection fails it falls back to a local SQLite file (`retail.db`).

## Project layout

```
retail-data-etl/
├── data/
│   ├── raw/              # source CSV files
│   └── processed/        # cleaned outputs
├── scripts/              # ETL steps and orchestration
├── sql/                  # helper SQL scripts (optional)
├── config/               # configuration (not used by default)
├── logs/                 # runtime logs
├── requirements.txt      # Python dependencies
└── README.md             # this file
```

## Setup

Create a Python virtual environment and install dependencies:

```bash
python -m venv venv          # create virtual environment
venv\\Scripts\\activate       # on Windows
pip install -r requirements.txt
```

Create a `.env` file in the project root (or edit the provided one) to configure your database credentials:

```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password_here
MYSQL_DATABASE=retail_db
```

## Running

```bash
cd retail-data-etl
python scripts/pipeline.py
```

The pipeline will:
1. Read `data/raw/retail_sales.csv`.
2. Drop missing rows and compute a `revenue` column.
3. Save cleaned data to `data/processed/cleaned_sales.csv`.
4. Attempt to load the dataframe into the MySQL database described by
   `config/db_config.py` (database name `retail_db` by default).
   If the connection or load fails, it falls back to the local `retail.db`
   SQLite file in the project root.

