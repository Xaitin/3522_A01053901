from datetime import date


class Transaction:
    def __init__(self, a, t, n):
        self._transaction_amount = a
        self._transaction_category = t
        self._transaction_time = date.today().strftime("%d/%m/%Y")
        self._transaction_location = n

    def __str__(self):
        return "Transaction Amount: {0}, Transaction Category: {1}, " \
              "Time of Transaction: {2}, Store Name: {3}".format(self._transaction_amount,
                                                                 self._transaction_category,
                                                                 self._transaction_time,
                                                                 self._transaction_location)
