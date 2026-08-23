import pandas as pd
import pymysql

DB_CONFIG = {
    'host': 'localhost',
    'port': 3307,
    'user': 'root',
    'password': '1qaz@WSX',
    'database': 'TESTDB',
    'charset': 'utf8mb4'
}

def get_connection():
    """Create and return a raw PyMySQL database connection."""
    return pymysql.connect(**DB_CONFIG)

def get_employee_df(name: str = None) -> pd.DataFrame:
    """Fetch employee data into a pandas DataFrame using parameterized queries."""
    conn = get_connection()
    try:
        if name:
            query = """
                SELECT ID, Name, DeptId, Age, Gender, Salary, recordDt 
                FROM Staff 
                WHERE Name = %s
            """
            df = pd.read_sql(query, conn, params=(name,))
        else:
            query = """
                SELECT ID, Name, DeptId, Age, Gender, Salary, recordDt 
                FROM Staff
            """
            df = pd.read_sql(query, conn)
        return df
    finally:
        conn.close()