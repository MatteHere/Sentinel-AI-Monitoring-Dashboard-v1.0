import pandas as pd


def get_error_data():
    return pd.DataFrame(
        {
            "time": [
                "10:00",
                "10:05",
                "10:10",
                "10:15",
                "10:20",
                "10:25",
                "10:30",
            ],
            "errors": [4, 8, 6, 11, 7, 5, 9],
            "critical": [1, 2, 2, 3, 2, 1, 2],
            "timeouts": [2, 4, 3, 5, 3, 2, 4],
            "provider_errors": [1, 2, 1, 3, 2, 2, 3],
        }
    )