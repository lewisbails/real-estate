"""Scrape Domain.com.au listings"""
import argparse
import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from real_estate.scrape import domain_rental_listings

DOMAIN_URL = "https://www.domain.com.au/rent/adelaide-region-sa/?page=1"

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
    """Extract listings and persist"""
    # Create a new client and connect to the server
    client = MongoClient(args.uri, server_api=ServerApi("1"))

    # Send a ping to confirm a successful connection
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")


    # get collection
    db = client[args.db]
    collection = db[args.collection]

    # get html
    html = requests.get(args.url, headers=HEADERS)

    # extract listings and insert into db
    if html.ok:
        listings = [listing.model_dump() for listing in domain_rental_listings(html)]
        collection.insert_many(listings)
    else:
        html.raise_for_status()


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Scraper for Domain rental listings")
    parser.add_argument("--uri", type=str, required=True, help="MongoDB uri")
    parser.add_argument("--db", type=str, required=True, help="Database name")
    parser.add_argument("--collection", type=str, required=True, help="Collection name")
    parser.add_argument("--url", type=str, default=DOMAIN_URL, help="URL for Domain.com.au rental list-view")
    args = parser.parse_args()
    main(args)
