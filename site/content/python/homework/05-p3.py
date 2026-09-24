# 作业三答案：多返回值与容器遍历综合


def split_data(data):
    mid = len(data) // 2
    return data[:mid], data[mid:]


nums = [1, 2, 3, 4, 5, 6]
first, second = split_data(nums)
print(first, second)  # [1, 2, 3] [4, 5, 6]


def find_indices(items, target):
    indices = []
    for i, item in enumerate(items):
        if item == target:
            indices.append(i)
    return indices


scores = [85, 92, 85, 78, 85]
positions = find_indices(scores, 85)
print(positions)  # [0, 2, 4]

result = second + [len(positions)]
print(result)  # [4, 5, 6, 3]
