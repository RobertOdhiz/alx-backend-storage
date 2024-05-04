#!/usr/bin/env python3
"""
Contains the Cache Class
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ get method that takes a key string argument and an optional Callable argument named fn """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ get_str method that automatically parametrizes
        Cache.get with the correct conversion function for strings """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """ get_int method that automatically parametrizes
        Cache.get with the correct conversion function for integers """
        return self.get(key, fn=int)
