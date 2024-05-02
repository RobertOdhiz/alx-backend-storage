#!/usr/bin/env python3
"""  returns the list of school having a specific topic """

import pymongo


def schools_by_topic(mongo_collection, topic):
    """ main function """
    return mongo_collection.find({"topics": topic})
