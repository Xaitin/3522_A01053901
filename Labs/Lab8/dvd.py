from item import Item


class Dvd(Item):

    def __init__(self, call_num, num_copies, title, release_date, region_code):
        self._call_num = call_num
        self._num_copies = num_copies
        self._title = title
        self._release = release_date
        self._region_code = region_code

    @staticmethod
    def create_item():
        n_call_num = input("Enter dvd call number:")
        n_copies = input("Enter number of copies to create:")
        n_title = input("Enter the dvd title:")
        n_release_date = input("Enter the release date:")
        n_region_code = input("Enter the region code:")
        return Dvd(n_call_num, n_copies, n_title, n_release_date, n_region_code)

    def get_release_date(self):
        return self._release

    def get_region_code(self):
        return self._region_code

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
        return f"---- Dvd: {self.get_title()} ----\n" \
               f"Call Number: {self._call_num}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Release Date: {self._release}\n" \
               f"Region Code: {self._region_code}"
