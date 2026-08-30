# 作业二答案：关键字参数与字典操作综合


def merge_data(base, **extra):
    result = base.copy()  # 浅拷贝
    for key, value in extra.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result


data = {"a": 10, "b": [1, 2]}
merged = merge_data(data, a=5, b=[3], c="hello")
print(merged)  # {'a': 15, 'b': [1, 2, 3], 'c': 'hello'}

print(len(merged))  # 3
print(merged.get("d", "not found"))  # not found
