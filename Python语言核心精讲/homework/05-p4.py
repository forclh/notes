# 作业四答案：函数综合编程


# 任务 1：列表扁平化
def flatten(nested_list):
    result = []
    for item in nested_list:
        if type(item) is list:
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


# 任务 2：列表/元组转链表
def to_linked_list(items):
    if not items:
        return None
    head = {"value": items[0], "next": None}
    current = head
    for item in items[1:]:
        current["next"] = {"value": item, "next": None}
        current = current["next"]
    return head


# 任务 3：字典合并
def merge_dicts(*dicts):
    result = {}
    for item in dicts:
        result.update(item)
    return result


# ========== 测试代码 ==========

# 测试 flatten
print("=== 测试 flatten ===")
nested1 = [1, [2, 3], [[4], 5]]
print(flatten(nested1))  # [1, 2, 3, 4, 5]

nested2 = [[[1]], 2, [3, [4, [5]]]]
print(flatten(nested2))  # [1, 2, 3, 4, 5]

print(flatten([]))  # []
print(flatten([1, 2, 3]))  # [1, 2, 3]

# 测试 to_linked_list
print("\n=== 测试 to_linked_list ===")
linked1 = to_linked_list((1, 2, 3))
print(linked1)
# {'value': 1, 'next': {'value': 2, 'next': {'value': 3, 'next': None}}}

linked2 = to_linked_list([10, 20])
print(linked2)
# {'value': 10, 'next': {'value': 20, 'next': None}}

print(to_linked_list([]))  # None

# 测试 merge_dicts
print("\n=== 测试 merge_dicts ===")
d1 = {"a": 1, "b": [1, 2]}
d2 = {"b": [3], "c": "hello"}
d3 = {"a": 10, "d": True}

merged = merge_dicts(d1, d2, d3)
print(merged)
# {'a': 10, 'b': [3], 'c': 'hello', 'd': True}

print(merge_dicts(d1))
# {'a': 1, 'b': [1, 2]}

print(merge_dicts())
# {}
