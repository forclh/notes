class InsufficientFundsError(Exception):
    """余额不足"""

    pass


class AccountFrozenError(Exception):
    """账户已冻结"""

    pass


class BankAccount:
    def __init__(self, balance=0, frozen=False):
        self.balance = balance
        self.frozen = frozen

    def withdraw(self, amount):
        """
        取款
        1. 如果 frozen=True，抛出 AccountFrozenError
        2. 如果 amount > balance，抛出 InsufficientFundsError
        3. 如果 amount <= 0，抛出 ValueError
        """
        if self.frozen:
            raise AccountFrozenError("账户已冻结，无法取款")
        if amount <= 0:
            raise ValueError("取款金额必须大于零")
        if amount > self.balance:
            raise InsufficientFundsError("余额不足")
        self.balance -= amount

    def deposit(self, amount):
        """
        存款
        1. 如果 frozen=True，抛出 AccountFrozenError
        2. 如果 amount <= 0，抛出 ValueError
        """
        if self.frozen:
            raise AccountFrozenError("账户已冻结，无法存款")
        if amount <= 0:
            raise ValueError("存款金额必须大于零")
        self.balance += amount


# 测试
account = BankAccount(100)
account.deposit(50)  # balance = 150
account.withdraw(30)  # balance = 120
print(f"余额: {account.balance}")  # 120

# account.withdraw(200)       # InsufficientFundsError
# account.deposit(-10)        # ValueError

frozen_account = BankAccount(100, frozen=True)
# frozen_account.withdraw(10)  # AccountFrozenError
