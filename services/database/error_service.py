import pandas as pd

from database.connection import get_connection


def get_errors():
    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT
            request_id,
            error_type,
            severity,
            message,
            created_at
        FROM errors
        ORDER BY created_at DESC
        """,
        conn,
    )

    conn.close()
    return df