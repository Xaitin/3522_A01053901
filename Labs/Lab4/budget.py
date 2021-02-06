class Budget:
    """
    Budget class to represent the users budget
    """

    def __init__(self, name, m):
        """
        Stores budget type and values
        :param name: budget type
        :param m: max budget value
        """
        self._budget_type = name
        self._budget_limit = m
        self._is_locked = False
        self._budget_balance = 0

    @classmethod
    def load_test_budget(cls):
        t1 = "Games"
        t2 = "Clothing"
        t3 = "Food"
        t4 = "Misc"
        max_value = 500
        my_budgets = [Budget(t1, max_value), Budget(t2, max_value), Budget(t3, max_value), Budget(t4, max_value)]
        return my_budgets
