from useraccount import UserAccount
from budget import Budget


class UserGenerator:

    @staticmethod
    def load_test_user():
        n = "Bobby Joe"
        a = 21
        t = "The Angel"
        a_num = 1101291
        b_name = "RBC"
        b_bal = 10000
        test_budget = Budget.load_test_budget()
        return UserAccount(n, a, t, a_num, b_name, b_bal, test_budget)
    @staticmethod
    def create_user():
        print("Welcome to the User Creation Wizard.")
        print("-------------------")
        print("Please fill in the required fields:")
        user_name = input("The users name:")
        user_age = input("The users age:")
        user_type = input("The users type:")
        user_account_num = input("The users account number:")
        user_bank_name = input("Name of the users bank:")
        user_bank_balance = input("Starting bank balance:")
        user_budgets = [Budget("Games", input("Budget for games:")),
                        Budget("Clothing", input("Budget for clothes:")),
                        Budget("Food", input("Budget for food:")),
                        Budget("Misc", input("Budget for misc items:"))]
        return UserAccount(user_name, user_age, user_type, user_account_num,
                           user_bank_name, user_bank_balance, user_budgets)
