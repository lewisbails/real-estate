"""Pydantic models"""
from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Listing(BaseModel):
    """A listing"""

    model_config = ConfigDict(from_attributes=True)

    id: str
    datetime: datetime
    provider: str
    rental: bool
    price: int
    street_address: str
    suburb: str
    state: str
    postcode: str
    beds: int
    baths: int
    parking: int
    area: Optional[int] = None
    dwelling: str
