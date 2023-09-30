"""Enum objects"""
from enum import Enum

from real_estate.util import SUBURB_COUNCIL_MAPPING


class StrEnum(str, Enum):
    """String Enum"""

    def __str__(self):
        """Override to return value"""
        return str(self.value)


Suburb = StrEnum("Suburb", names={k.upper(): k.lower() for k in SUBURB_COUNCIL_MAPPING})
Council = StrEnum("Council", names={v.upper(): v.lower() for v in SUBURB_COUNCIL_MAPPING.values()})


class State(StrEnum):
    """Australian state code"""

    SA = "sa"
    WA = "wa"
    NSW = "nsw"
    NT = "nt"
    QLD = "qld"
    VIC = "vic"
    TAS = "tas"
    ACT = "act"


class Provider(StrEnum):
    """Australian property portal"""

    DOMAIN = "domain"
    REALESTATE = "realestate"
