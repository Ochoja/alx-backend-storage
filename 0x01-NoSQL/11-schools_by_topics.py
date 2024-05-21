#!/usr/bin/env python3
"""Returns a list of schools having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Return list of document having topic in topics array"""
    collection = mongo_collection.find({"topics": topic})
    return collection
