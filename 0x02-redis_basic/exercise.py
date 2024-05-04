#!/usr/bin/env python3
"""
Contains the Cache Class
"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """ Cache Class Representation """
    def __init__(self):
        """ Instantiates the class """
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store method that takes a data argument and returns a string """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
