# 作业四答案：字符串操作与循环综合

s = "hello"
print(s[1:4])  # ell
print("el" in s, "x" not in s)  # True True
print(s + " world", s * 2)  # hello world hellohello

i = 0
vowels = "aeiou"
count = 0
while i < len(s):
    if s[i] in vowels:
        count += 1
    i += 1
print(count)  # 2
print(f"length: {len(s)}")  # length: 5
