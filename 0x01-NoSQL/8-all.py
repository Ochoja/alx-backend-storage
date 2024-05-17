#!/usr/bin/env python3
"""List all documents in collection"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """List all documents in mongo_collection"""
    client = MongoClient()
    docs = []

    for doc in mongo_collection:
        docs.append(doc)

    if docs == []:
        return None

    return docs
