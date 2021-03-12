"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""
import re


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """
    def __init__(self):
        self.text = None

    def read_data(self, src="House of Usher.txt"):
        # read lines
        with open(src, mode='r', encoding='utf-8') as book_file:
            text = book_file.read(-1)
        # convert list of lines to list of words
        self.text = set(re.split('[*:;,.!?\(\)\[\]\"\'\n\-\s]+', text.lower()))
        return self.text


def main():
    book_analyzer = BookAnalyzer()
    unique_words = book_analyzer.read_data()
    print("-" * 50)
    print('\n'.join(unique_words))
    print("-" * 50)
    print(f"List of unique words (Count: {len(unique_words)})")
    print("-" * 50)
    list_1 = ["A", "B"]
    list_2 = ["C", "D"]
    result = map(lambda x, y: x + y, list_2, list_1)
    print(list(result))


if __name__ == '__main__':
    main()
