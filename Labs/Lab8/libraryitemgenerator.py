from item import Item
from book import Book
from journal import Journal
from dvd import Dvd


class LibraryItemGenerator:

    @staticmethod
    def create_item():
        item_types = [cls.__name__ for cls in Item.__subclasses__()]
        item_type = input("The supported items are: {0} Which would you like to create?".format(item_types))
        item_type = item_type.lower()
        if item_type in (string.lower() for string in item_types):
            if item_type == "book":
                return Book.create_item()
            elif item_type == "dvd":
                return Dvd.create_item()
            elif item_type == "journal":
                return Journal.create_item()
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
