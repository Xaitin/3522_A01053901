from abc import ABC, abstractmethod


class ProductFactory(ABC):
    """Product factory that is the abstract base class for all our other factories"""

    @abstractmethod
    def create_candy(self, item):
        """Candy creation method"""
        pass

    @abstractmethod
    def create_toy(self, item):
        """Toy creation method for extension"""
        pass

    @abstractmethod
    def create_stuffed_animal(self, item):
        """Stuffed Animal creation method"""
        pass
