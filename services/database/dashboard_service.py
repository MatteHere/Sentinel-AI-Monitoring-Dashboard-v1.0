from database.connection import get_connection


def get_dashboard_metrics():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM requests")
    total_requests = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(latency) FROM requests")
    avg_latency = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(tokens) FROM requests")
    total_tokens = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(cost) FROM requests")
    total_cost = cursor.fetchone()[0] or 0

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM requests
        WHERE status='Failed'
        """
    )
    failed_requests = cursor.fetchone()[0]

    success_rate = 100

    if total_requests > 0:
        success_rate = (
            (total_requests - failed_requests)
            / total_requests
        ) * 100

    conn.close()

    return {
        "total_requests": total_requests,
        "avg_latency": round(avg_latency, 1),
        "total_tokens": total_tokens,
        "total_cost": round(total_cost, 2),
        "success_rate": round(success_rate, 2),
        "failed_requests": failed_requests,
    }