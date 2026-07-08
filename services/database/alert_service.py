import pandas as pd

from database.connection import get_connection


def get_alerts():
    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT
            title,
            severity,
            status,
            created_at
        FROM alerts
        ORDER BY created_at DESC
        """,
        conn,
    )

    conn.close()
    return df