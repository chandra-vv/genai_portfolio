import os
import mysql.connector
from mysql.connector import pooling
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# ── Connection pool (avoids dirty-connection "Unread result" errors) ──────────
_pool = None

def _get_pool():
    global _pool
    if _pool is None:
        _pool = pooling.MySQLConnectionPool(
            pool_name="text2sql_pool",
            pool_size=3,
            pool_reset_session=True,       # resets session state on each checkout
            host=os.getenv("MYSQL_HOST", "localhost"),
            port=int(os.getenv("MYSQL_PORT", 3306)),
            database=os.getenv("MYSQL_DATABASE"),
            user=os.getenv("MYSQL_USER") or os.getenv("MYSQL_USERNAME"),
            password=os.getenv("MYSQL_PASSWORD"),
            connection_timeout=10,
            autocommit=True,
        )
    return _pool


def get_connection():
    """Return a pooled connection. Each call gets a clean connection from the pool."""
    return _get_pool().get_connection()


def get_schema(conn) -> str:
    """
    Return a compact schema description for all tables in the connected database,
    including column names, types, nullability, and primary key markers.
    """
    db_name = os.getenv("MYSQL_DATABASE")

    # Use buffered=True so all results are fetched immediately — prevents dirty state
    cursor = conn.cursor(buffered=True)

    cursor.execute(
        "SELECT table_name FROM information_schema.tables "
        "WHERE table_schema = %s AND table_type = 'BASE TABLE' "
        "ORDER BY table_name",
        (db_name,),
    )
    tables = [row[0] for row in cursor.fetchall()]

    schema_parts = []
    for table in tables:
        cursor.execute(
            "SELECT column_name, column_type, is_nullable, column_key "
            "FROM information_schema.columns "
            "WHERE table_schema = %s AND table_name = %s "
            "ORDER BY ordinal_position",
            (db_name, table),
        )
        cols = cursor.fetchall()
        col_defs = []
        for col_name, col_type, is_nullable, col_key in cols:
            parts = f"{col_name} {col_type}"
            if col_key == "PRI":
                parts += " PK"
            if is_nullable == "NO":
                parts += " NOT NULL"
            col_defs.append(parts)
        schema_parts.append(f"{table}({', '.join(col_defs)})")

    cursor.close()
    return "\n".join(schema_parts)


def run_query(conn, sql: str) -> pd.DataFrame:
    """
    Execute a SELECT query and return results as a DataFrame (capped at 500 rows).
    Uses a buffered cursor so all results are consumed immediately,
    preventing 'Unread result found' errors on the next query.
    """
    # buffered=True fetches ALL rows into memory at once — connection stays clean
    cursor = conn.cursor(buffered=True)
    try:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchmany(500)
        return pd.DataFrame(rows, columns=columns)
    finally:
        # Always close cursor and return connection to pool cleanly
        cursor.close()
        try:
            conn.close()   # returns to pool, does NOT drop the connection
        except Exception:
            pass
