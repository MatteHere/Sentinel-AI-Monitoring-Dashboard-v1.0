from database.connection import get_connection


def log_error(
    request_id: str,
    error_type: str,
    severity: str,
    message: str,
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO errors
        (
            request_id,
            error_type,
            severity,
            message
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            request_id,
            error_type,
            severity,
            message,
        ),
    )

    conn.commit()
    conn.close()