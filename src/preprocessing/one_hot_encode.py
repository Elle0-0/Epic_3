"""
This script takes the cleaned combined-data.csv file 
and one-hot encodes the Country column.
"""

from os import path

DATASETS_DIR = path.join(path.dirname(__file__), "..", "datasets")

DATA_PATH = path.join(DATASETS_DIR, "clean", "combined-data.csv")
print(DATA_PATH)

from pathlib import Path
import pandas as pd 


def one_hot_encode() -> None:
    # Create clean directory if not exists
    Path(path.join(DATASETS_DIR, "one_hot_encoded")).mkdir(parents=True, exist_ok=True)

    df: pd.DataFrame = pd.read_csv(DATA_PATH)
    print(df.head())

    # One-hot encode the Country column
    df = pd.get_dummies(df, columns=["Country"])
    print(df.head())


    # Our data currently has 2 columns for each year from 1970 to 2021, one for co2 and one for temperature
    # We want to combine these into a single column for each year, and a column for co2 and a column for temperature

    # Create a new dataframe to store the combined data
    new_df = pd.DataFrame()

    # Iterate through the years from 1970 to 2021

    for year in range(1970, 2022):
        # Get the co2 and temperature columns for the current year
        co2_col = f"{year}_co2_total"
        temp_col = f"{year}_surface_temperature"

        # Create a new dataframe with the year, co2 and temperature columns
        # we also add all the encoded country columns to the new dataframe
        # so we end up with
        # Year | Co2 | Temperature | Country_X | Country_Y | ...

        new = df[[temp_col, co2_col] + [col for col in df.columns if col.startswith("Country_")]]

        new.rename(columns={temp_col: "Temperature", co2_col: "Co2"}, inplace=True)
        new.insert(0, "Year", year)

        # year_df = df[[co2_col, temp_col] + [col for col in df.columns if col.startswith("Country_")]]
        # year_df["Year"] = year
        new_df = pd.concat([new_df, new])

    print(new_df.head())

    new_df.to_csv(path.join(DATASETS_DIR, "one_hot_encoded", "combined-data.csv"), index=False)
    print("Successfully created and saved: 'one-hot-encoded.csv'")


if __name__ == "__main__":
    one_hot_encode()