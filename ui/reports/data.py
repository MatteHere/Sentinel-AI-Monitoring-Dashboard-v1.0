import pandas as pd


def get_report_data():
    return pd.DataFrame(
        {
            "date": ["May 12", "May 13", "May 14", "May 15", "May 16", "May 17", "May 18"],
            "reports": [4, 6, 5, 8, 7, 5, 7],
            "exports": [10, 14, 12, 18, 16, 13, 17],
        }
    )