#!/usr/bin/env python3
"""Insert document into collection"""


def insert_school(mongo_collection, **kwargs):
    """Insert document based on kwargs"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
