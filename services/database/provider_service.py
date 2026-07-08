import pandas as pd

from database.connection import get_connection


def get_provider_stats():
    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT
            provider,
            avg_latency,
            success_rate,
            total_requests
        FROM providers
        ORDER BY total_requests DESC
        """,
        conn,
    )

    conn.close()
    return df