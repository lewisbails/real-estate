"""Scrape Domain.com.au listings"""
import os
import argparse
import requests
import logging
from pathlib import Path
from tqdm import tqdm

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from real_estate.scrape import domain_rental_listings

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    filename=Path(__file__).parent.parent / "logs/mongo_domain.log")

log = logging.getLogger(__name__)

DOMAIN_URL = "https://www.domain.com.au/rent/adelaide-region-sa/?sort=dateupdated-desc&page="

HEADERS: dict[str, str] = {
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


def main(args):
    """Extract listings, transform, and load to mongodb"""
    log.info("Scraping listings...")

    # Create a new client and connect to the server
    if args.uri is None:
        args.uri = os.environ["MONGODB_URI"]

    client = MongoClient(args.uri, server_api=ServerApi("1"))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception:
        log.exception("MongoDB connection problem")
        raise

    # get collection
    db = client[args.db]
    collection = db[args.collection]

    # extract listings, transform into standardised Listing form and load into db
    scraped = 0
    for i in tqdm(range(1, 5)):
        url = DOMAIN_URL + str(i)
        # get html
        html = requests.get(url, headers=HEADERS)
        if html.ok:
            for listing in tqdm(domain_rental_listings(html)):
                try:
                    collection.insert_one(listing.model_dump(by_alias=True))
                    scraped += 1
                except Exception:
                    log.exception("Couldn't insert listing")
        else:
            try:
                html.raise_for_status()
            except requests.HTTPError:
                log.exception(f"Couldn't reach {url}")
                raise

    log.info(f"Finished. Scraped {scraped} listings")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Scraper for Domain rental listings. Will look at first N list-view pages of Domain.com.au")
    parser.add_argument("--uri", type=str, help="MongoDB uri")
    parser.add_argument(
        "--db", type=str, default="real-estate", help="Database name")
    parser.add_argument("--collection", type=str,
                        default="listings", help="Collection name")
    args = parser.parse_args()
    main(args)
