#!/usr/bin/env python3
""" returns all students sorted by average score """

from pymongo import MongoClient


def top_students(mongo_collection):
    """ main function """
    aggre = [
        {"$project": {
            "name": "$name", "averageScore": {"$avg": "$topics.score"}
            }},
        {"$sort": {"averageScore": -1}}
    ]
    return mongo_collection.aggregate(aggre)
