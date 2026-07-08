from database.connection import get_connection
from database.schema import create_tables


def initialize_database():
    create_tables()

    conn = get_connection()
    cursor = conn.cursor()

    # Prevent duplicate demo data
    cursor.execute("SELECT COUNT(*) FROM requests")
    request_count = cursor.fetchone()[0]

    if request_count == 0:
        requests = [
            ("REQ-1001", "Ollama", "llama3", 342, 1250, 0.021, "Success"),
            ("REQ-1002", "Groq", "mixtral", 214, 980, 0.015, "Success"),
            ("REQ-1003", "Gemini", "gemini-1.5-flash", 487, 1670, 0.033, "Success"),
            ("REQ-1004", "Ollama", "llama3", 615, 2015, 0.041, "Failed"),
            ("REQ-1005", "Groq", "mixtral", 298, 1345, 0.019, "Success"),
        ]

        cursor.executemany(
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
            requests,
        )

    cursor.execute("SELECT COUNT(*) FROM errors")
    error_count = cursor.fetchone()[0]

    if error_count == 0:
        errors = [
            (
                "REQ-1004",
                "Timeout",
                "High",
                "Provider response exceeded timeout.",
            ),
            (
                "REQ-1010",
                "Rate Limit",
                "Medium",
                "Too many requests sent.",
            ),
            (
                "REQ-1013",
                "Validation Error",
                "Low",
                "Invalid request payload.",
            ),
        ]

        cursor.executemany(
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
            errors,
        )

    cursor.execute("SELECT COUNT(*) FROM alerts")
    alert_count = cursor.fetchone()[0]

    if alert_count == 0:
        alerts = [
            (
                "Latency Spike",
                "Critical",
                "Open",
            ),
            (
                "Provider Failure",
                "High",
                "Investigating",
            ),
            (
                "High Cost Warning",
                "Medium",
                "Resolved",
            ),
        ]

        cursor.executemany(
            """
            INSERT INTO alerts
            (
                title,
                severity,
                status
            )
            VALUES (?, ?, ?)
            """,
            alerts,
        )

    cursor.execute("SELECT COUNT(*) FROM providers")
    provider_count = cursor.fetchone()[0]

    if provider_count == 0:
        providers = [
            (
                "Ollama",
                352,
                99.1,
                8421,
            ),
            (
                "Groq",
                228,
                99.8,
                6352,
            ),
            (
                "Gemini",
                472,
                98.4,
                3647,
            ),
        ]

        cursor.executemany(
            """
            INSERT INTO providers
            (
                provider,
                avg_latency,
                success_rate,
                total_requests
            )
            VALUES (?, ?, ?, ?)
            """,
            providers,
        )

    conn.commit()
    conn.close()