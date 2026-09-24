def paginated_query(total_items, page_size):
    """
    模拟分页查询
    total_items: 总数据量
    page_size: 每页大小
    每次 yield 返回一页数据（列表）
    """
    for start in range(0, total_items, page_size):
        end = min(start + page_size, total_items)
        yield list(range(start, end))


for page in paginated_query(25, 10):
    print(page)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# [20, 21, 22, 23, 24]
