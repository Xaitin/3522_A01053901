from Handler import Handler


class RequestInputHandler(Handler):

    def __init__(self, next_handler=None):
        super().__init__(next_handler)
        self.next_handler = next_handler

    def setNext(self, handler):
        self.next_handler = handler

    def handle(self, request):
        length = len(request.key)
        if length is not 8 and length is not 16 and length is not 24:
            print("Key length must be 8 16 or 24")
            return False
        if request.data_input is None and request.input_file is None:
            print("No data provided to encrypt or decrypt")
            return False
        if request.data_input is not None and request.input_file is not None:
            print("Two forms of data provided, please provide one at a time.")
            return False
        if request.output is not "print" and ".txt" not in request.output:
            print("Output needs .txt extension")
            return False
        return self.next_handler.handle(request)
