"""Pydantic models"""
from typing import Optional, Annotated
from datetime import datetime

from pydantic import (BaseModel, ConfigDict, StringConstraints, PositiveInt, NonNegativeInt, StrictBool)

from real_estate.enums import STREET_TYPES, Provider, State, Dwelling, Council, Suburb


STREET_RGX = rf".*(?:{'|'.join(STREET_TYPES)})$"


class Listing(BaseModel):
    """A listing"""

    model_config = ConfigDict(from_attributes=True)

    id: str
    datetime: datetime
    provider: Provider
    rental: StrictBool
    price: PositiveInt
    address: Annotated[str, StringConstraints(pattern=STREET_RGX)]
    suburb: Suburb
    state: State
    postcode: Annotated[str, StringConstraints(pattern=r"\d{4}")]
    council: Council
    beds: PositiveInt
    baths: PositiveInt
    parking: NonNegativeInt
    area: Optional[PositiveInt] = None
    dwelling: Dwelling
