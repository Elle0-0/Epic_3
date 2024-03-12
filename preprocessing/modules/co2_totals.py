"""
Do not run this file directly.
"""

import pandas as pd
from pandas import DataFrame

FILE_NAME: str = "co2-totals.csv"
PATH_IN: str = f"../datasets/raw/{FILE_NAME}"
PATH_OUT: str = f"../datasets/processed/{FILE_NAME}"


def process() -> DataFrame:

    print(f"Processing file: {FILE_NAME!r}...")

    # Columns required: "Country", "1990", ..., "2019"
    col_names: list[str] = ["Country"]
    col_names.extend(str(year) for year in range(1990, 2020))

    df: DataFrame = pd.read_csv(PATH_IN, usecols=col_names)

    # Remove unnecessary rows
    df.drop(df.tail(3).index, inplace=True)

    # Save to output location
    df.to_csv(PATH_OUT, index=False)

    print(f"Successfully processed and saved: {FILE_NAME!r}\n")

    return df
