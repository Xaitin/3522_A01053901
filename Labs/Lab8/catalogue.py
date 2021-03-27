from libraryitemgenerator import LibraryItemGenerator
import difflib


class Catalogue:
    """
    The Catalogue consists of a list of books
    """

    def __init__(self):
        """
        Catalogue initializer.
        """
        self._item_list = LibraryItemGenerator.generate_test_items()

    def check_out(self, call_number):
        """
        Check out an book with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        library_item = self._retrieve_item_by_call_number(call_number)
        if library_item.check_availability():
            status = self.reduce_item_count(call_number)
            if status:
                print("Checkout complete!")
            else:
                print(f"Could not find book with call number {call_number}"
                      f". Checkout failed.")
        else:
            print(f"No copies left for call number {call_number}"
                  f". Checkout failed.")

    def return_item(self, call_number):
        """
        Return an book with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        status = self.increment_item_count(call_number)
        if status:
            print("book returned successfully!")
        else:
            print(f"Could not find book with call number {call_number}"
                  f". Return failed.")

    def _retrieve_item_by_call_number(self, call_number):
        """
        A private method that encapsulates the retrieval of an book with
        the given call number from the library.
        :param call_number: a string
        :return: book object if found, None otherwise
        """
        found_item = None
        for catalogue_item in self._item_list:
            if catalogue_item.call_number == call_number:
                found_item = catalogue_item
                break
        return found_item

    def find_items(self, title):
        """
        Find books with the same and similar title.
        :param title: a string
        :return: a list of titles.
        """
        title_list = [x.get_title() for x in self._item_list]
        results = difflib.get_close_matches(title, title_list,
                                            cutoff=0.5)
        return results

    def add_item(self):
        """
        Add a brand new book to the library with a unique call number.
        """
        new_book = LibraryItemGenerator.create_item()
        found_book = self._retrieve_item_by_call_number(
            new_book.call_number)
        if found_book:
            print(f"Could not add item with call number "
                  f"{new_book.call_number}. It already exists. ")
        else:
            self._item_list.append(new_book)
            print("item added successfully! item details:")
            print(new_book)

    def remove_item(self, call_number):
        """
        Remove an existing item from the library
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        found_item = self._retrieve_item_by_call_number(call_number)
        if found_item:
            self._item_list.remove(found_item)
            print(f"Successfully removed {found_item.get_title()} with "
                  f"call number: {call_number}")
        else:
            print(f"item with call number: {call_number} not found.")

    def display_available_items(self):
        """
        Display all the items in the library.
        """
        print("Books List")
        print("--------------", end="\n\n")
        [print(x) for x in self._item_list]

    def reduce_item_count(self, call_number):
        """
        Decrement the item count for an book with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the book was found and count decremented, false
        otherwise.
        """
        library_item = self._retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.decrement_number_of_copies()
            return True
        else:
            return False

    def increment_item_count(self, call_number):
        """
        Increment the book count for an book with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the book was found and count incremented, false
        otherwise.
        """
        library_item = self._retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.increment_number_of_copies()
            return True
        else:
            return False
