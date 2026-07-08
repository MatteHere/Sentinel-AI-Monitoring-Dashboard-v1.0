from database.connection import get_connection


def log_request(
    request_id: str,
    provider: str,
    model: str,
    latency: float,
    tokens: int,
    cost: float,
    status: str,
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO requests
        (
            request_id,
            provider,
            model,
            latency,
            tokens,
            cost,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            request_id,
            provider,
            model,
            latency,
            tokens,
            cost,
            status,
        ),
    )

    conn.commit()
    conn.close()