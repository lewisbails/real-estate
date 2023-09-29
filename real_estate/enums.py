"""Enum objects"""
from enum import Enum

from real_estate.util import SUBURB_COUNCIL_MAPPING


class Council(str, Enum):
    pass


for council in SUBURB_COUNCIL_MAPPING.values():
    setattr(Council, council.upper(), council.lower())


class Suburb(str, Enum):
    pass


for suburb in SUBURB_COUNCIL_MAPPING:
    setattr(Suburb, suburb.upper(), suburb.lower())


class State(str, Enum):
    SA = "sa"


class Provider(str, Enum):
    DOMAIN = "domain"
    REALESTATE = "realestate"


class Dwelling(str, Enum):
    HOUSE = "house"
    APARTMENT = "apartment"
    TOWNHOUSE = "townhouse"
