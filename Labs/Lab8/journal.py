from item import Item


class Journal(Item):
    """
    Represents a Journal item.
    """
    def __init__(self, call_num, num_copies, title, issue_num, publisher):
        self._call_num = call_num
        self._num_copies = num_copies
        self._title = title
        self._issue_num = issue_num
        self._publisher = publisher

    def get_issue_num(self):
        return self._issue_num

    def get_publisher(self):
        return self._publisher

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
        return f"---- Journal: {self.get_title()} ----\n" \
               f"Call Number: {self._call_num}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Issue number: {self._issue_num}\n" \
               f"Publisher: {self._publisher}"
