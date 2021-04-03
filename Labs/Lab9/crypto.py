import des
import argparse
import abc
import enum
from request_input_handler import RequestInputHandler as rih
from request_output_handler import RequestOutputHandler as roh
from request_encryption_handler import RequestEncryptionHandler as reh
from request_decryption_handler import RequestDecryptionHandler as rdh


class CryptoMode(enum.Enum):
    """
    Lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class Request:
    """
    The request object represents a request to either encrypt or decrypt
    certain data. The request object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a file.
        - input_file: The text file that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a file and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the request.

    """
    def __init__(self):
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self):
        return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
               f", Input file: {self.input_file}, Output: {self.output}, " \
               f"Key: {self.key}"


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        req = Request()
        req.encryption_state = CryptoMode(args.mode)
        req.data_input = args.string
        req.input_file = args.file
        req.output = args.output
        req.key = args.key
        print(req)
        return req
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class Crypto:

    def __init__(self, en, de):
        self.encryption_start_handler = en
        self.decryption_start_handler = de

    def execute_request(self, req: Request):
        if req.encryption_state == CryptoMode.EN.value:
            self.encryption_start_handler.handle(req)
        else:
            self.decryption_start_handler.handle(req)


def main(req: Request):
    en_input = rih()
    en_encrypter = reh()
    en_output = roh()
    de_input = rih()
    de_decrypter = rdh()
    de_output = roh()
    en_input.setNext(en_encrypter)
    en_encrypter.setNext(en_output)
    de_input.setNext(de_decrypter)
    de_decrypter.setNext(de_output)
    crypto = Crypto(en_input, de_input)
    crypto.execute_request(req)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
