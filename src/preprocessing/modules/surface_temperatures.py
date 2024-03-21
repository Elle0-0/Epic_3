from pathlib import Path

import pandas as pd
from pandas import DataFrame

from . import RAW_PATH, CLEAN_PATH

FILE_NAME: str = "surface-temperatures.csv"
PATH_IN: Path = RAW_PATH / FILE_NAME
PATH_OUT: Path = CLEAN_PATH / FILE_NAME


def rename_column(column_name: str) -> str:
    """
    Removes the first character from a given column name
    if it starts with "F" and returns the new name.
    Returns the original name otherwise.

    :param column_name: Name of column.
    """

    return column_name[column_name.startswith("F"):]


def process() -> DataFrame:

    print(f"Cleaning file: {FILE_NAME!r}...")

    column_names: list[str] = ["Country"]
    column_names.extend(f"F{year}" for year in range(1970, 2022))

    df: DataFrame = pd.read_csv(PATH_IN, usecols=column_names)

    # Remove "F" from year column names
    df.rename(columns=rename_column, inplace=True)

    df.to_csv(PATH_OUT, index=False)
    print(f"Successfully cleaned and saved: {FILE_NAME!r}\n")

    return df
