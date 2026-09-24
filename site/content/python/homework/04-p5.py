# 作业五答案：enumerate、zip与多容器综合

names = ["Alice", "Bob"]
ages = (25, 30)

pairs = []
for name, age in zip(names, ages):
    pairs.append(f"{name}-{age}")
print(pairs)  # ['Alice-25', 'Bob-30']

for i, name in enumerate(names, 1):
    print(i, name)  # 1 Alice, 2 Bob

d = {}
i = 0
while i < len(names):
    if ages[i] > 20:
        d[names[i]] = ages[i]
    i += 1
print(len(d))  # 2
print(d.get("Alice"))  # 25
print(d.get("Charlie", "not found"))  # not found
