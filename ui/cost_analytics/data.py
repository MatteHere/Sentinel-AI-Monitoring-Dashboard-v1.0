import pandas as pd


def get_cost_data():
    return pd.DataFrame(
        {
            "date": [
                "May 12",
                "May 13",
                "May 14",
                "May 15",
                "May 16",
                "May 17",
                "May 18",
            ],
            "daily_cost": [18, 25, 31, 29, 34, 41, 46],
            "requests": [1480, 2490, 2910, 3070, 2840, 3390, 3810],
            "tokens": [620000, 1180000, 890000, 1320000, 1210000, 1670000, 1820000],
        }
    )