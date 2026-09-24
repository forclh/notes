from typing import Any, Dict, List, Optional

# 原代码的问题：
# 1. List 和 Dict 没有指定泛型参数，不够具体
# 2. 应该明确 items 是包含 id 和 value 的字典列表
# 3. 返回值应该指定键和值的类型


def process_data(items: List[Dict[str, Any]]) -> Dict[Any, Any]:
    """处理数据项"""
    result: Dict[Any, Any] = {}
    for item in items:
        result[item["id"]] = item["value"]
    return result


# 更好的写法：使用 TypedDict 或更具体的类型
# from typing import TypedDict
# class DataItem(TypedDict):
#     id: int
#     value: str
# def process_data(items: List[DataItem]) -> Dict[int, str]:


def find_max(a: int, b: int) -> Optional[int]:
    """返回较大的数"""
    if a == b:
        return None
    return a if a > b else b


# 测试
print(process_data([{"id": 1, "value": "a"}, {"id": 2, "value": "b"}]))
print(find_max(3, 5))  # 5
print(find_max(3, 3))  # None
