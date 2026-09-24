# 作业三：BMI 计算器

# 获取用户输入
height = float(input("请输入您的身高（米）："))
weight = float(input("请输入您的体重（千克）："))

# 计算 BMI
bmi = weight / (height**2)

# 判断分类
if bmi < 18.5:
    category = "偏瘦"
    advice = "建议适当增加营养摄入，多吃富含蛋白质的食物，进行适量力量训练。"
elif bmi < 24:
    category = "正常"
    advice = "保持良好的生活习惯，均衡饮食，适量运动，继续保持！"
elif bmi < 28:
    category = "超重"
    advice = "建议控制饮食，减少高热量食物摄入，增加有氧运动，如慢跑、游泳等。"
else:
    category = "肥胖"
    advice = "建议咨询专业医生或营养师，制定科学的减重计划，注意饮食控制和规律运动。"

# 输出结果
print(f"\n您的 BMI 值为：{bmi:.2f}")
print(f"身体状况：{category}")
print(f"建议：{advice}")
