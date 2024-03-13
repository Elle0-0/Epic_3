"""
Do not run this file directly.
"""

import pandas as pd
from pandas import DataFrame

FILE_NAME: str = "co2-totals.csv"
PATH_IN: str = f"../datasets/raw/{FILE_NAME}"
PATH_OUT: str = f"../datasets/clean/{FILE_NAME}"


def process() -> DataFrame:

    print(f"Cleaning file: {FILE_NAME!r}...")

    df: DataFrame = pd.read_csv(PATH_IN)

    # Remove irrelevant columns
    df.drop(columns=["Substance", "EDGAR Country Code"], inplace=True)

    # Remove unnecessary/problematic rows
    df.drop(df.tail(3).index, inplace=True)

    df.to_csv(PATH_OUT, index=False)
    print(f"Successfully cleaned and saved: {FILE_NAME!r}\n")

    return df
