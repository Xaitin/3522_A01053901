from useraccount import UserAccount


class UserMenu:

    def __init__(self):
        self._user_account = UserAccount.load_test_user()

    def display_user_menu(self):
        user_input = None
        while user_input != 5:
            print("\nWelcome to the F.A.M menu")
            print("--------------------")
            print("1. View Budgets")
            print("2. Record a Transaction")
            print("3. View Transactions")
            print("4. View Bank Account Details")
            print("5. Quit")
            my_input = input("Please enter your choice (1-5)")

            if my_input == '':
                continue

            user_input = int(my_input)

            if user_input == 1:
                # self._user_account.get_budgets()
                pass
            elif user_input == 2:
                print("\nWelcome to the Transaction menu")
                print("------------------")
                print("Please select the budget category for this transaction")
                print("1. Games and Entertainment")
                print("2. Clothing and Accessories")
                print("3. Grocery and Dining out")
                print("4. Miscellaneous Spending")
                transaction_type = input("Please enter your choice (1-4)")
                if transaction_type == "1":
                    transaction_type = "Games"
                elif transaction_type == "2":
                    transaction_type = "Clothing"
                elif transaction_type == "3":
                    transaction_type = "Food"
                elif transaction_type == "4":
                    transaction_type = "Misc"
                transaction_amount = input("Please enter the cost of your transaction: ")
                transaction_location = input("Please enter the name of the store this purchase took place: ")
                self._user_account.record_transaction(transaction_amount, transaction_type,
                                                      transaction_location)
                self._user_account.show_transactions()
            elif user_input == 3:
                self._user_account.show_transactions()
            elif user_input == 4:
                # self._user_account.get_account_details()
                pass
            elif user_input == 5:
                pass
            else:
                print("Your input was not accepted. Please enter a number from 1 - 5.")

        print("Thank you for using F.A.M")


def main():
    my_epic_bank = UserMenu()
    my_epic_bank.display_user_menu()


if __name__ == '__main__':
    main()
