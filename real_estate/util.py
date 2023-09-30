"""Random utils"""
from pathlib import Path
import json


SUBURB_COUNCIL_MAPPING: dict[str, str] = {k.lower(): v.lower() for k, v in json.load(open(Path(__file__).parent / "data/sa_suburb_to_council.json", "r")).items()}
