# 作业五答案：综合练习


def create_account(initial_balance):
    """创建银行账户，返回存款和取款函数"""
    balance = initial_balance

    def dep(n):
        nonlocal balance
        balance += n
        return balance

    def draw(n):
        nonlocal balance
        if n > balance:
            return "余额不足"
        balance -= n
        return balance

    return dep, draw


# ========== 测试代码 ==========

deposit, withdraw = create_account(100)
print(deposit(50))  # 150
print(withdraw(30))  # 120
print(withdraw(200))  # 余额不足

# 验证余额变量未被暴露，且各账户相互独立
deposit2, withdraw2 = create_account(50)
print(deposit2(10))  # 60 —— 独立的账户
