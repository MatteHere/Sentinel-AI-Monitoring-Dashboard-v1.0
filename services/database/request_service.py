from database.connection import get_connection

import pandas as pd


def get_all_requests():
    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT *
        FROM requests
        ORDER BY created_at DESC
        """,
        conn,
    )

    conn.close()

    return df