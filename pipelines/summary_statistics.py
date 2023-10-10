"""Pull listings down from database and calculate some summary statistics"""
import logging
import os
import argparse
import re
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from real_estate.util import COUNCIL_LOWER_MAPPING

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", filename=Path(__file__).parent.parent / "logs/mongo_statistics.log")

log = logging.getLogger(__name__)


def main(args):  # noqa: D103
    log.info("Generating summary statistics...")

    # Create a new client and connect to the server
    if args.uri is None:
        args.uri = os.environ["MONGODB_URI"]

    client = MongoClient(args.uri, server_api=ServerApi("1"))

    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception:
        log.exception("MongoDB connection problem")
        raise

    db = client[args.db]
    collection = db[args.collection]

    since = datetime.now() - timedelta(days=30)

    pipeline = [
        {
            "$match": {"rental": True, "datetime": {"$gte": since}},
        },
        {
            "$group": {
                "_id": "$council",
                "count": {"$sum": 1},
                "average rent": {"$avg": "$price"},
                "max rent": {"$max": "$price"},
                "min rent": {"$min": "$price"},
                "average bedrooms": {"$avg": "$bed"},
                "max bedrooms": {"$max": "$bed"},
                "average bathrooms": {"$avg": "$bath"},
                "max bathrooms": {"$max": "$bath"},
            }
        },
    ]

    results = collection.aggregate(pipeline)

    if results:
        df = pd.DataFrame.from_records(results)
        df = df.rename(columns={"_id": "council"}).set_index("council").rename(COUNCIL_LOWER_MAPPING).sort_values("average rent").round()
        tbl = df.to_markdown(tablefmt="github")
        md = open(Path(__file__).parent.parent / "README.md", "r").read()
        md = re.sub(r"## Statistics\n[\s\S]*?\n(?=##)", lambda m: f"## Statistics\nSince {since.strftime('%d-%m-%y')}\:\n{tbl}\n", md)
        open(Path(__file__).parent.parent / "README.md", "w").write(md)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Gather summary statistics from mongodb listings collection")
    parser.add_argument("--uri", type=str, help="MongoDB uri")
    parser.add_argument("--db", type=str, default="real-estate", help="Database name")
    parser.add_argument("--collection", type=str, default="listings", help="Collection name")
    args = parser.parse_args()
    main(args)
