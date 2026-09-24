# 作业三答案：修复代码
# 场景：统计函数调用次数

call_count = 0


def process_data(data):
    result = sum(data)
    # 处理完成后递增计数器
    call_count += 1
    return result


print(process_data([1, 2, 3]))
print(process_data([4, 5, 6]))
print(f"总共调用了 {call_count} 次")
