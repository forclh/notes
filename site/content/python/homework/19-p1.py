import json
import os
from abc import ABC, abstractmethod


class Cache(ABC):
    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def delete(self, key):
        pass


class MemoryCache(Cache):
    def __init__(self):
        self._data = {}

    def get(self, key):
        return self._data.get(key)

    def set(self, key, value):
        self._data[key] = value

    def delete(self, key):
        if key in self._data:
            del self._data[key]


class FileCache(Cache):
    def __init__(self, directory="cache"):
        self._directory = directory
        os.makedirs(directory, exist_ok=True)

    def _get_path(self, key):
        return os.path.join(self._directory, f"{key}.json")

    def get(self, key):
        path = self._get_path(key)
        if not os.path.exists(path):
            return None
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def set(self, key, value):
        path = self._get_path(key)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(value, f)

    def delete(self, key):
        path = self._get_path(key)
        if os.path.exists(path):
            os.remove(path)


# 使用
memory_cache = MemoryCache()
memory_cache.set("name", "Alice")
print(memory_cache.get("name"))  # Alice
memory_cache.delete("name")
print(memory_cache.get("name"))  # None

file_cache = FileCache()
file_cache.set("name", "Bob")
print(file_cache.get("name"))  # Bob
file_cache.delete("name")
print(file_cache.get("name"))  # None
