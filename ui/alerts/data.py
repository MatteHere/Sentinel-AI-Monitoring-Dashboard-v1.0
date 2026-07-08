import pandas as pd


def get_alert_data():
    return pd.DataFrame(
        {
            "time": ["10:00", "10:05", "10:10", "10:15", "10:20", "10:25", "10:30"],
            "critical": [1, 2, 1, 3, 2, 2, 3],
            "warning": [4, 5, 6, 7, 5, 4, 6],
            "info": [8, 6, 7, 9, 8, 7, 10],
        }
    )