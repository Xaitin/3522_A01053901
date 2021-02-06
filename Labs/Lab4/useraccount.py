from transaction import Transaction
from budget import Budget


class UserAccount:

    def __init__(self, name, age, t, account_num, bank_name, bank_bal, test_budgets):
        self._name = name
        self._age = age
        self._user_type = t
        self._account_num = account_num
        self._bank_name = bank_name
        self._bank_bal = bank_bal
        self._budgets = test_budgets
        self._transactions = []

    @classmethod
    def load_test_user(cls):
        n = "Bobby Joe"
        a = 21
        t = "The Angel"
        a_num = 1101291
        b_name = "RBC"
        b_bal = 10000
        test_budget = Budget.load_test_budget()
        return UserAccount(n, a, t, a_num, b_name, b_bal, test_budget)

    def record_transaction(self, am, ty, na):
        self._transactions.append(Transaction(am, ty, na))

    def show_transactions(self):
        for x in self._transactions:
            print(x)
