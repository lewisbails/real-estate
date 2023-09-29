"""Random utils"""
from pathlib import Path
import json

SUBURB_COUNCIL_MAPPING: dict[str, str] = {k.lower() : v.lower() for k, v in json.load(open(Path(__file__).parent.parent / "data/sa_suburb_to_council.json", "r")).items()}
STREET_TYPES: set[str] = set(json.load(open(Path(__file__).parent.parent / "data/street_types.json", "r")))
STREET_SUFFIXES: set[str] = set(json.load(open(Path(__file__).parent.parent / "data/street_suffixes.json", "r")))
STREET_TYPES_ABBREVIATIONS: dict[str, str] = json.load(open(Path(__file__).parent.parent / "data/street_types.json", "r"))
STREET_SUFFIXES_ABBREVIATIONS: dict[str, str] = json.load(open(Path(__file__).parent.parent / "data/street_suffixes.json", "r"))