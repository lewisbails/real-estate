import json
from enum import Enum
from pathlib import Path

SUBURB_COUNCIL_MAPPING: dict[str, str] = json.load(open(Path(__file__).parent.parent / "data/sa_suburb_to_council.json", "r"))

class Council(Enum):
    pass

for council in SUBURB_COUNCIL_MAPPING.values():
    setattr(Council, council.upper(), council.lower())

class Suburb(Enum):
    pass

for suburb in SUBURB_COUNCIL_MAPPING:
    setattr(Suburb, suburb.upper(), suburb.lower())

class State(Enum):
    SA = "sa"


class Provider(Enum):
    DOMAIN: "domain"
    REALESTATE: "realestate"


class Dwelling(Enum):
    HOUSE: "house"
    APARTMENT: "apartment"
    TOWNHOUSE: "townhouse"


STREET_TYPES: set[str] = {
    "avenue",
    "boulevard",
    "circle",
    "court",
    "drive",
    "lane",
    "parkway",
    "place",
    "road",
    "street",
    "terrace",
    "way",
    "alley",
    "crescent",
    "highway",
    "loop",
    "square",
    "trail",
    "expressway",
    "freeway",
    "path",
    "route",
    "viaduct",
    "promenade",
    "row",
    "mews",
    "close",
    "esplanade",
    "quay",
    "passage",
    "walk",
    "crossroad",
    "overpass",
    "underpass",
    "cul-de-sac"
}