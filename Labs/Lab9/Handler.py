from abc import ABC, abstractmethod


class Handler(ABC):

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def setNext(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass
