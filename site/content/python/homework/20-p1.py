def calculate_bmi(weight: float, height: float) -> float:
    """计算 BMI 指数"""
    if height <= 0:
        raise ValueError("身高必须大于0")
    return weight / (height**2)


def get_grade(score: int) -> str:
    """根据分数返回等级"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# 测试
print(calculate_bmi(70, 1.75))  # 22.857...
print(get_grade(85))  # B
print(get_grade(59))  # F
