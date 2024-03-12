"""
Do not run this file directly.
"""

import pandas as pd
from pandas import DataFrame

FILE_NAME: str = "asthma-prevalence.csv"
PATH_IN: str = f"../datasets/raw/{FILE_NAME}"
PATH_OUT: str = f"../datasets/processed/{FILE_NAME}"


def process() -> DataFrame:

    print(f"Processing file: {FILE_NAME!r}...")

    # Columns required
    col_names: list[str] = [
        "Entity",
        "Year",
        "Current number of cases of asthma per 100 people, in both sexes aged age-standardized"
    ]

    df: DataFrame = pd.read_csv(PATH_IN, usecols=col_names)

    # Restructure rows/columns to match "co2-totals.csv" format
    new_rows: list[dict] = []

    for country in df["Entity"].unique():
        row_dict: dict = {
            "Country": country
        }

        for _, row in df.loc[df["Entity"] == country].iterrows():  # For each row that has that country
            year: str = str(row["Year"])
            number_cases: int = row[col_names[2]]
            row_dict[year] = number_cases  # Map year to number of cases

        new_rows.append(row_dict)

    new_dataframe: DataFrame = DataFrame(new_rows)
    new_dataframe.to_csv(PATH_OUT, index=False)

    print(f"Successfully processed and saved: {FILE_NAME!r}\n")

    return new_dataframe
