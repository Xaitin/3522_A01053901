from transaction import Transaction


class UserAccount:

    def __init__(self, name, age, t, account_num, bank_name, bank_bal, list_budgets):
        self._name = name
        self._age = age
        self._user_type = t
        self._account_num = account_num
        self._bank_name = bank_name
        self._bank_bal = bank_bal
        self._budgets = list_budgets
        self._transactions = []

    # Amount, Category, Name of store
    def record_transaction(self, am, ty, na):
        self._bank_bal -= am
        self._transactions.append(Transaction(am, ty, na))

    def show_transactions(self):
        for x in self._transactions:
            print(x)

