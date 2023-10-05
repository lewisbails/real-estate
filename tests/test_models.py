"""Test models module"""
import pytest
from datetime import datetime
from contextlib import nullcontext as does_not_raise

from real_estate.models import Listing
from real_estate.enums import Provider, Suburb, Council, State

@pytest.fixture
def good_listing() -> dict:  # noqa: D103
    listing = {
        "_id": "a",
        "datetime": datetime.now(),
        "provider": Provider("domain"),
        "rental": True,
        "price": 650,
        "address": "123 Fake Street, Hallett Cove",
        "suburb": Suburb("hallett cove"),
        "state": State("sa"),
        "postcode": "5158",
        "council": Council("city of marion"),
        "bed": 3,
        "bath": 2,
        "parking": 2,
        "area": 600,
        "dwelling": "house"
    }
    return listing

@pytest.mark.parametrize(
        "mod,expected",
        [
            ({}, does_not_raise()),
            ({"price": 0}, pytest.raises(Exception)),
            ({"bed": 0}, pytest.raises(Exception)),
            ({"bath": 0}, pytest.raises(Exception)),
            ({"parking": -1}, pytest.raises(Exception)),
            ({"area": -1}, pytest.raises(Exception)),
            ({"postcode": "12345"}, pytest.raises(Exception)),
            ({"provider": "some website"}, pytest.raises(Exception)),
            ({"state": "some state"}, pytest.raises(Exception)),
            ({"suburb": "some suburb"}, pytest.raises(Exception)),
            ({"council": "some council"}, pytest.raises(Exception)),
        ]
)
def test_listing(good_listing, mod, expected):  # noqa: D103
    listing = {**good_listing, **mod}
    with expected:
        Listing(**listing)