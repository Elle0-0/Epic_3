from pathlib import Path

import pandas as pd
from pandas import DataFrame

from . import RAW_PATH, CLEAN_PATH

FILE_NAME: str = "co2-totals.csv"
PATH_IN: Path = RAW_PATH / FILE_NAME
PATH_OUT: Path = CLEAN_PATH / FILE_NAME


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
