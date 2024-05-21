#!/usr/bin/env python3
"""Change all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Update topics in school with name 'name'"""
    filter = {"name": name}
    update_document = {"$set": {"topics": topics}}

    # update document
    mongo_collection.update_many(filter, update_document)
