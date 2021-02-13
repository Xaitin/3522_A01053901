import json
from enum import Enum
import ast


class file_handler:
    @staticmethod
    def load_data(path, file_extension):
        if file_extension == FileExtensions.TXT.value:
            file = open(path, "r")
            contents = file.read()
            txt_dictionary = ast.literal_eval(contents)
            file.close()
            return txt_dictionary
        elif file_extension == FileExtensions.JSON.value:
            with open(path) as json_file:
                data = json.load(json_file)
                return data
        else:
            raise InvalidTypeError



    @staticmethod
    def write_lines(path, lines):
        with open(path, "a") as my_file:
            my_file.write(lines)


class FileExtensions(Enum):
    TXT = ".txt"
    JSON = ".json"


class InvalidTypeError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'InvalidTypeError, {0} '.format(self.message)
        else:
            return 'InvalidTypeError raise'
