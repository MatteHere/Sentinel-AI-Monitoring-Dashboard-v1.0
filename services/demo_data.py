import pandas as pd

from database.connection import get_connection


def create_demo_data():
    """
    Returns dashboard data from SQLite instead of hardcoded demo data.
    """

    conn = get_connection()

    query = """
    SELECT
        created_at,
        latency,
        tokens,
        cost,
        status
    FROM requests
    ORDER BY created_at
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    if df.empty:
        return pd.DataFrame(
            columns=[
                "date",
                "requests",
                "p50",
                "p95",
                "p99",
                "tokens",
                "errors",
            ]
        )

    df["created_at"] = pd.to_datetime(df["created_at"])

    grouped = (
        df.groupby(df["created_at"].dt.date)
        .agg(
            requests=("status", "count"),
            p50=("latency", "median"),
            p95=("latency", lambda x: x.quantile(0.95)),
            p99=("latency", lambda x: x.quantile(0.99)),
            tokens=("tokens", "sum"),
            errors=("status", lambda x: (x == "Failed").sum()),
        )
        .reset_index()
    )

    grouped.rename(columns={"created_at": "date"}, inplace=True)

    grouped["date"] = pd.to_datetime(grouped["date"]).dt.strftime("%b %d")

    return grouped