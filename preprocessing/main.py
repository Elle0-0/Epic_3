from pathlib import Path

import pandas as pd
from pandas import DataFrame

from modules import co2_totals, surface_temperatures
from modules.misc import get_similar_countries

FILE_NAME: str = "combined-data.csv"
PATH_OUT: str = f"../datasets/clean/{FILE_NAME}"


def main() -> None:

    # Create clean directory if not exists
    Path("../datasets/clean").mkdir(parents=True, exist_ok=True)

    df1: DataFrame = co2_totals.process()
    df2: DataFrame = surface_temperatures.process()

    print(f"Creating file: {FILE_NAME!r}...")

    df1_countries: set[str] = set(df1["Country"])
    df2_countries: set[str] = set(df2["Country"])
    similar_countries: dict[str, str] = get_similar_countries(df1_countries, df2_countries)

    print(f"\nNormalizing following country names:\n{similar_countries}")

    # Normalize similar country names so they are the same
    df1["Country"].replace(similar_countries, inplace=True)

    # Only counts rows with matching countries
    combined: DataFrame = pd.merge(df1, df2, on="Country", suffixes=("_co2_total", "_surface_temperature"))
    combined.to_csv(PATH_OUT, index=False)

    print(f"\nSuccessfully created and saved: {FILE_NAME!r}")


if __name__ == "__main__":
    main()
