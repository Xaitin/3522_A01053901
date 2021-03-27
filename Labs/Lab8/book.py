from item import Item


class Book(Item):
    """
    Represents a single book in a library which is identified through
    it's call number.
    """

    def __init__(self, call_num, num_copies, title, author):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        self._call_num = call_num
        self._num_copies = num_copies
        self._title = title
        self._author = author

    def get_author(self):
        return self._author

    def increment_number_of_copies(self):
        self._num_copies += 1

    def decrement_number_of_copies(self):
        self._num_copies -= 1

    def get_num_copies(self):
        return self._num_copies

    def call_number(self):
        return self._call_num

    def get_title(self):
        return self._title.title()

    def check_availability(self):
        if self._num_copies > 0:
            return True
        else:
            return False

    def __str__(self):
        return f"---- Book: {self.get_title()} ----\n" \
               f"Call Number: {self._call_num}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Author: {self._author}"

