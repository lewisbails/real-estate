"""Scrape listings"""
import datetime
import re
import time

from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim

from real_estate.models import Listing
from real_estate.enums import Council, Suburb, State, Provider
from real_estate.util import SUBURB_COUNCIL_MAPPING

geolocator = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0")


def domain_rental_listings(html: str) -> list[Listing]:
    """
    Scrape listings information from Domain.com.au

    Parameters
    ----------
    html : str
        List view of rentals on Domain.com.au

    Returns
    -------
    list[dict]
        Listings
    """
    # Get the current date
    current_date = datetime.datetime.now().date()

    # Create a new datetime object with a time of 00:00
    midnight_datetime = datetime.datetime(current_date.year, current_date.month, current_date.day, 0, 0, 0)

    soup = BeautifulSoup(html.text, "html.parser")

    items = []
    for li in soup.find("ul", {"data-testid": "results"}).find_all("li"):
        item = {}

        if not li.get("data-testid", "").startswith("listing"):
            continue

        item["_id"] = li.get("data-testid").strip()
        item["datetime"] = midnight_datetime
        item["provider"] = Provider("domain")
        item["rental"] = True

        try:
            # listing price
            price = li.find("p", {"data-testid": "listing-card-price"})

            if price is None:
                raise Exception("price not found")

            match = re.search(r"\$?(\d+)", price.text)

            if match is None:
                raise Exception(f"weird looking price: {price.text}")

            item["price"] = int(match.group(1))

            # address
            address_1 = li.find("span", {"data-testid": "address-line1"})

            if address_1 is None:
                raise Exception("address not found")

            address_2 = li.find("span", {"data-testid": "address-line2"})

            if address_2 is None:
                raise Exception("address line 2 not found")

            item["address"] = geolocator.geocode(address_1.text + address_2.text).address.strip()
            time.sleep(1)  # Nominatim rate limit

            suburb, state, postcode = [s.text.lower().strip() for s in address_2.find_all("span")]

            item["suburb"] = Suburb(suburb)
            item["state"] = State(state)
            item["postcode"] = postcode
            item["council"] = Council(SUBURB_COUNCIL_MAPPING[suburb])

            # bed, bath, parking, area
            features = {}
            for f in li.find_all("span", {"data-testid": "property-features-text-container"}):
                fi = f.text.split()
                if len(fi) == 2:
                    try:
                        features[fi[1].lower()] = int(fi[0])
                    except ValueError:
                        features[fi[1].lower()] = 0
                else:
                    m = re.search(r"(\d+)\s?m", f.text)
                    if m:
                        features["area"] = int(m.group(1))
            item = {**item, **features}

            features_wrapper = li.find("div", {"data-testid": "listing-card-features-wrapper"})

            if features_wrapper is None:
                raise Exception("missing features")

            for div in features_wrapper.find_all("div"):
                if div.get("data-testid", "").startswith("property-features"):
                    continue
                item["dwelling"] = div.text.lower().strip()
                break
            else:
                continue

            item = Listing.model_validate(item)
            items.append(item)
        except Exception as e:
            print(e)
            # traceback.print_exc()
    return items
