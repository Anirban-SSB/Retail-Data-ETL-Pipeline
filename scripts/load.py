import os
import sqlite3

# mysql is optional; we attempt to load there first and fall back to sqlite
try:
    import mysql.connector
    from mysql.connector import Error
except ImportError:
    mysql = None
    Error = Exception

from config.db_config import db_config


def load_data(df):
    """Load data into a database.

    - If a MySQL server is reachable using `config/db_config.py`, the function
      will insert rows into a `sales` table there (creating it if necessary).
    - On any failure the routine writes to `retail.db` SQLite file instead.
    """
    # try MySQL first
    if mysql is not None:
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            # ensure sales table exists (simple column definitions)
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS sales (
                    order_id INT,
                    customer_id VARCHAR(20),
                    product VARCHAR(100),
                    category VARCHAR(50),
                    price DOUBLE,
                    quantity INT,
                    date DATETIME,
                    country VARCHAR(50),
                    revenue DOUBLE
                )
                """
            )
            insert_sql = (
                "INSERT INTO sales (order_id, customer_id, product, category, price, quantity, date, country, revenue)"
                " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            )
            for row in df.itertuples(index=False, name=None):
                cursor.execute(insert_sql, row)
            conn.commit()
            cursor.close()
            conn.close()
            print("Data loaded to MySQL database")
            return
        except Error as e:
            print(f"MySQL load failed ({e}), falling back to SQLite")
        except Exception as e:
            # any other error (e.g. connection object missing)
            print(f"MySQL load error ({e}), falling back to SQLite")

    # fallback path: SQLite
    db_path = os.path.join(os.getcwd(), "retail.db")
    conn = sqlite3.connect(db_path)
    df.to_sql('sales', conn, if_exists='replace', index=False)
    conn.close()
    print("Data loaded to SQLite database")

