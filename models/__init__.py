from pathlib import Path


class Paths:
    DATASETS: Path = Path(__file__).parents[1].joinpath("datasets")
    RAW: Path = DATASETS / "raw"
    CLEAN: Path = DATASETS / "clean"
    OHE: Path = DATASETS/ "one_hot_encoded"
    WM: Path = DATASETS / "world_map"
