from typing import Optional

from difflib import SequenceMatcher

SIMILARITY_THRESHOLD: float = 0.73


def most_similar_country(country: str, countries: tuple[str]) -> Optional[str]:
    """
    Finds the most similar match given a country and a tuple of countries to match from.

    :param country: Country name.
    :param countries: Tuple of countries to find similar match from.

    :return: None if there are no sufficient matches, otherwise the most
             similar match greater than or equal to the given threshold.
    """

    matches: dict[float, str] = {}

    for _country in countries:
        similarity: float = SequenceMatcher(isjunk=None, a=country, b=_country).ratio()
        if similarity >= SIMILARITY_THRESHOLD:
            matches[similarity] = _country

    if not matches:
        return None

    return matches[max(matches)]


def get_similar_countries(countries_a: set[str], countries_b: set[str]) -> dict[str, str]:
    """
    Maps each country in the first set of countries to the most similar
    country in the second set of countries and returns as a dictionary.

    :param countries_a: First set of countries.
    :param countries_b: Second set of countries.
    """

    similarities: dict[str, str] = {}
    countries_b_unique: tuple[str] = tuple(country for country in countries_b if country not in countries_a)

    for country in countries_a:
        if country not in countries_b:

            corresponding_country: str | None = most_similar_country(country, countries_b_unique)

            if corresponding_country is not None:
                similarities[country] = corresponding_country

    return similarities
