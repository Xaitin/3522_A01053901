from des import DesKey
from Handler import Handler


class RequestDecryptionHandler(Handler):

    def __init__(self, handler=None):
        super().__init__(handler)
        self.next_handler = handler

    def setNext(self, handler):
        self.next_handler = handler

    def handle(self, request):
        byte_key = bytes(request.key, 'utf-8')
        key = DesKey(byte_key)
        if request.data_input is None:
            with open(request.input_file, mode='r', encoding='utf-8') as input_file:
                text = input_file.read()
                text_to_decrypt = bytes(text, 'utf-8')
                request.result = key.decrypt(text_to_decrypt, padding=True)
        else:
            text = request.data_input
            text_to_decrypt = bytes(text, 'utf-8')
            request.result = key.decrypt(text_to_decrypt, padding=True)
        return self.next_handler.handle(request)
