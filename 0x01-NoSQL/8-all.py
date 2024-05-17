#!/usr/bin/env python3
"""List all documents in collection"""


def list_all(mongo_collection):
    """List all documents in mongo_collection"""
    docs = []

    try:
        for doc in mongo_collection.find():
            docs.append(doc)
        return docs
    except Exception:
        return None
