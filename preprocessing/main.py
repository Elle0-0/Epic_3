from pathlib import Path

import pandas as pd
from pandas import DataFrame

from modules import co2_totals, asthma_prevalence

FILE_NAME: str = "combined-data.csv"
PATH_OUT: str = f"../datasets/processed/{FILE_NAME}"


def main() -> None:

    # Create processed directory if not exists
    Path("../datasets/processed").mkdir(parents=True, exist_ok=True)

    df1: DataFrame = co2_totals.process()
    df2: DataFrame = asthma_prevalence.process()

    print(f"Processing file: {FILE_NAME!r}...")

    # Only counts rows with matching countries
    combined: DataFrame = pd.merge(df1, df2, on="Country", suffixes=("_co2_levels", "_asthma_cases"))
    combined.to_csv(PATH_OUT, index=False)

    print(f"Successfully processed and saved: {FILE_NAME!r}")


if __name__ == "__main__":
    main()
