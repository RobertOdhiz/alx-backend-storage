#!/usr/bin/env python3
"""
Contains the Cache Class
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a function"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output

    return wrapper


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a method is called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def replay(method: Callable):
    """ to display the history of calls of a particular function """
    method_name = method.__qualname__
    inputs_key = method_name + ":inputs"
    outputs_key = method_name + ":outputs"
    inputs = cache._redis.lrange(inputs_key, 0, -1)
    outputs = cache._redis.lrange(outputs_key, 0, -1)
    print(f"{method_name} was called {len(inputs)} times:")
    for input_data, output_data in zip(inputs, outputs):
        input_args = eval(input_data.decode("utf-8"))
        output = output_data.decode("utf-8")
        print(f"{method_name}{input_args} -> {output}")


class Cache:
    """ Cache Class Representation """
    def __init__(self):
        """ Instantiates the class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    
    @count_calls
    @call_history
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
