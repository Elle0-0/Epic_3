from typing import Optional

from difflib import SequenceMatcher


def most_similar_country(country: str, countries: tuple[str], *, similarity_threshold: float = 0.6) -> Optional[str]:
    """
    Finds the most similar match given a country and a tuple of countries to match from.

    :param country: Country name.
    :param countries: Tuple of countries to find similar match from.
    :param similarity_threshold: Minimum measure of "similarity" – a float between [0, 1].

    :return: None if there are no sufficient matches, otherwise the most
             similar match greater than or equal to the given threshold.
    """

    matches: dict[float, str] = {}

    for _country in countries:
        similarity: float = SequenceMatcher(isjunk=None, a=country, b=_country).ratio()
        if similarity >= similarity_threshold:
            matches[similarity] = _country

    if not matches:
        return None

    return matches[max(matches)]


def show_similar_countries(countries_a: set[str], countries_b: set[str], *, similarity_threshold: float = 0.6) -> None:
    """
    Displays the most similar country in the second set of countries for
    each country in the first set of countries. Ignores equal strings.

    :param countries_a: First set of countries.
    :param countries_b: Second set of countries.
    :param similarity_threshold: see `most_similar_country.__doc__`
    """

    countries_b_unique: tuple[str] = tuple(country for country in countries_b if country not in countries_a)

    for country in countries_a:
        if country not in countries_b:

            corresponding_country: str | None = most_similar_country(
                country,
                countries_b_unique,
                similarity_threshold=similarity_threshold
            )

            if corresponding_country is not None:
                print(f"    Dataframe 1: {country}".ljust(50), f"Dataframe 2: {corresponding_country}")
