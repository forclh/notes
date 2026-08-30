# 作业三答案：字典与遍历综合

d = {"x": 10, "y": 20}
d["z"] = 30
d.update({"x": 15})
print(len(d))  # 3
print("x" in d, 20 in d)  # True False
print(d.get("w", 0))  # 0

keys = []
for k in d:
    keys.append(k)
print(keys)  # ['x', 'y', 'z']

i = 0
while i < len(keys):
    k = keys[i]
    if d[k] > 15:
        print(k)  # y, z
    i += 1
