"""Scrape listing information"""
import datetime
import re
import traceback
from typing import Optional

import requests
from bs4 import BeautifulSoup

from real_estate.models import Listing
from real_estate.sanitise import address, dwelling
from real_estate.util import SUBURB_COUNCIL_MAPPING

DEFAULT_HEADERS: dict[str, str] = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
}


def domain_rental_listings(url: str, headers: Optional[dict] = None) -> list[Listing]:
    """
    Scrape listings information from Domain.com.au

    Parameters
    ----------
    url : str
        Domain.com.au URL
    headers : dict | None
        Request headers

    Returns
    -------
    list[dict]
        Listings
    """
    if headers is None:
        headers = DEFAULT_HEADERS
    html = requests.get(url, headers=headers)
    items = []

    if not html.ok:
        html.raise_for_status()

    # Get the current date
    current_date = datetime.datetime.now().date()

    # Create a new datetime object with a time of 00:00
    midnight_datetime = datetime.datetime(current_date.year, current_date.month, current_date.day, 0, 0, 0)

    soup = BeautifulSoup(html.text, "html.parser")

    for li in soup.find("ul", {"data-testid": "results"}).find_all("li"):
        item = {}

        if not li.get("data-testid", "").startswith("listing"):
            continue

        item["id"] = li.get("data-testid")
        item["datetime"] = midnight_datetime
        item["provider"] = "domain"
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

            item["address"] = address_1.text.split(",")[0].lower()

            # address line 2
            address_2 = li.find("span", {"data-testid": "address-line2"})

            if address_2 is None:
                raise Exception("address line 2 not found")

            address_2_comps = [s.text.lower() for s in address_2.find_all("span")]
            item = {**item, **({"suburb": address_2_comps[0], "state": address_2_comps[1], "postcode": address_2_comps[2]})}
            item["council"] = SUBURB_COUNCIL_MAPPING[item["suburb"]]

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
                item["dwelling"] = div.text.lower()
                break
            else:
                continue

            item = Listing.model_validate(item)
            items.append(item)
        except Exception as e:
            print(e)
            # traceback.print_exc()
    return items
