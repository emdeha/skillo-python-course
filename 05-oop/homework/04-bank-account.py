from fee_policies import ExtremeFee
# import fee_policies as fp


class BankAccount:
    def __init__(self, balance, allow_overdraft, fee_policy):
        self.__balance = balance
        self.__allow_overdraft = allow_overdraft
        self.__fee_policy = fee_policy

    def withdraw(self, amount):
        if not self.__allow_overdraft and self.__balance - amount < 0:
            return

        self.__balance -= amount
        self.__balance -= self.__fee_policy.withdrawal_fee()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

    def add_monthly_fee(self):
        if self.__balance >= 0:
            return

        self.__balance -= self.__fee_policy.monthly_fee(self.__balance)


tsvetan_account = BankAccount(0, False, ExtremeFee())
# tsvetan_account = BankAccount(0, False, fp.ExtremeFee())
tsvetan_account.deposit(100)
print(f"Tsvetan has {tsvetan_account.get_balance()}")
tsvetan_account.withdraw(50)
print(f"Tsvetan has {tsvetan_account.get_balance()}")
tsvetan_account.withdraw(100)
print(f"Tsvetan has {tsvetan_account.get_balance()}")
tsvetan_account.deposit(-50)
print(f"Tsvetan has {tsvetan_account.get_balance()}")
tsvetan_account.withdraw(50)
print(f"Tsvetan has {tsvetan_account.get_balance()}")
tsvetan_account.withdraw(50)
print(f"Tsvetan has {tsvetan_account.get_balance()}")
