#!/usr/bin/env python3
""" nginx logs to mongo instance parser """

from pymongo import MongoClient


def temp_F():
    """ temp function to check the checker"""
    client = MongoClient()
    main = client.logs.nginx
    method_C = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    status = main.count_documents({"method": "GET", "path": "/status"})
    print(f"{main.estimated_document_count()} logs")
    print("Methods:")
    for i in method_C:
        check = main.count_documents({"method": i})
        print(f"\tmethod {i}: {check}")
    print(f"{status} status check")


if __name__ == "__main__":
    temp_F()
