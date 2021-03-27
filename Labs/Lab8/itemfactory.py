from item import Item
from book import Book
from journal import Journal
from dvd import Dvd


class ItemFactory:

    @staticmethod
    def create_item():
        item_types = [cls.__name__ for cls in Item.__subclasses__()]
        item_type = input("The supported items are: {0} Which would you like to create?".format(item_types))
        item_type = item_type.lower()
        if item_type in (string.lower() for string in item_types):
            n_call_num = input("Enter book call number:")
            n_copies = input("Enter number of copies to create:")
            n_title = input("Enter the book title:")
            if item_type == "book":
                n_author = input("Enter the author:")
                return Book(n_call_num, n_copies, n_title, n_author)
            elif item_type == "dvd":
                n_release_date = input("Enter the release date:")
                n_region_code = input("Enter the region code:")
                return Dvd(n_call_num, n_copies, n_title, n_release_date, n_region_code)
            elif item_type == "journal":
                n_issue_num = input("Enter the issue number:")
                n_publisher = input("Enter the publisher:")
                return Journal(n_call_num, n_copies, n_title, n_issue_num, n_publisher)
        else:
            print("Invalid item type")

    @staticmethod
    def generate_test_items():
        return [
            Book("102.721.333", 3, "Harry Potter 1", "J.K Rowling"),
            Book("111.121.111", 4, "The Gunslinger", "Stephen King"),
            Journal("000.000.000", 1, "Journal test", 42, "Publish Guy"),
            Journal("123.456.789", 2, "Test Journal", 21, "Guy Publish"),
            Dvd("987.654.321", 1, "The tooth ferry", "Jan 21", 412),
            Dvd("333.333.333", 1, "Harry Potter M1", "IDK", 222)
        ]
