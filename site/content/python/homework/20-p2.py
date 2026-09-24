from typing import Dict, Generic, Optional, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class Cache(Generic[K, V]):
    """泛型缓存类"""

    def __init__(self) -> None:
        self._data: Dict[K, V] = {}

    def set(self, key: K, value: V) -> None:
        """设置缓存"""
        self._data[key] = value

    def get(self, key: K) -> Optional[V]:
        """获取缓存，不存在返回 None"""
        return self._data.get(key)

    def clear(self) -> None:
        """清空缓存"""
        self._data.clear()


# 测试
cache: Cache[str, int] = Cache()
cache.set("a", 1)
cache.set("b", 2)
print(cache.get("a"))  # 1
print(cache.get("c"))  # None
cache.clear()
print(cache.get("a"))  # None
