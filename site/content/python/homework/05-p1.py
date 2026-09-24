# 作业一答案：函数参数与列表操作综合


def add_items(base, items=None, *tags):
    if items is None:
        items = []
    items.append(base)
    for tag in tags:
        items.append(tag)
    return items


result1 = add_items(10)
print(result1)  # [10]

result2 = add_items(20, [1, 2], 30, 40)
print(result2)  # [1, 2, 20, 30, 40]

print(result1)  # [10]
