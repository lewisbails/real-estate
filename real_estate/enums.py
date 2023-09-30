"""Enum objects"""
from enum import Enum

from real_estate.util import SUBURB_COUNCIL_MAPPING


class Council(str, Enum):
    """Australian council"""

    pass


for council in SUBURB_COUNCIL_MAPPING.values():
    setattr(Council, council.upper(), council.lower())


class Suburb(str, Enum):
    """Australian suburb"""

    pass


for suburb in SUBURB_COUNCIL_MAPPING:
    setattr(Suburb, suburb.upper(), suburb.lower())


class State(str, Enum):
    """Australian state code"""

    SA = "sa"
    WA = "wa"
    NSW = "nsw"
    NT = "nt"
    QLD = "qld"
    VIC = "vic"
    TAS = "tas"
    ACT = "act"


class Provider(str, Enum):
    """Australian property portal"""

    DOMAIN = "domain"
    REALESTATE = "realestate"
