from real_estate.enums import Dwelling
from real_estate.util import STREET_TYPES, STREET_SUFFIXES, STREET_TYPES_ABBREVIATIONS, STREET_SUFFIXES_ABBREVIATIONS


def address(address: str) -> str:
    # check for abbreviated endings
    # if a type exists, check its allowed
    # maybe break it down into street number, unit number, street name, street type?
    return address


def dwelling(name: str) -> str:
    if "house" in name or "home" in name:
        return Dwelling.HOUSE
    if "apartment" in name or "unit" in name or "flat" in name:
        return Dwelling.APARTMENT
    if "townhouse" in name:
        return Dwelling.TOWNHOUSE
    raise ValueError(f"Unknown dwelling type '{name}'")
