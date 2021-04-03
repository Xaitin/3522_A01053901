from Handler import Handler


class RequestOutputHandler(Handler):

    def __init__(self, next_handler=None):
        super().__init__(next_handler)
        self.next_handler = next_handler

    def setNext(self, handler):
        self.next_handler = handler

    def handle(self, request):
        if request.output == 'print':
            print(request.result)
        else:
            f = open(request.output, "w")
            f.write(str(request.result))
            f.close()
