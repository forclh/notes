def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


nested = [1, [2, [3, 4], 5], 6, [7, 8]]
print(list(flatten(nested)))
# [1, 2, 3, 4, 5, 6, 7, 8]
