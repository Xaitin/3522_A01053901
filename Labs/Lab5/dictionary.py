from file_handler import file_handler
import pathlib


class dictionary:

    def __init__(self):
        self._data = None
        self._is_loaded = False
        self._output_path = None

    def load_dictionary(self, filepath):
        ext = pathlib.Path(filepath).suffix
        self._data = file_handler.load_data(filepath, ext)
        self._is_loaded = True
        self._output_path = input("Please enter the output file path")

    def query_definition(self, word):
        for key in self._data:
            if word.lower() == key.lower():
                word_definition = self._data[word]
                text_to_append = str(word) + ": " + str(word_definition)
                file_handler.write_lines(self._output_path, text_to_append)
                print(word_definition)
                return str(word_definition)


def main():
    my_dictionary = dictionary()
    file_to_load = input("Please enter the name of the dictionary file.")
    my_dictionary.load_dictionary(file_to_load)
    user_input = ""
    while user_input != "exitprogram":
        user_input = input("Enter a word to query. Enter 'exitprogram' when done.")
        my_dictionary.query_definition(user_input)


if __name__ == '__main__':
    main()
