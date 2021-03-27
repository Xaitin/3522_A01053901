from abc import ABC, abstractmethod


class Candy(ABC):
    """Candy abstract class for candy objects"""
    @property
    @abstractmethod
    def has_nuts(self):
        """Defines property and getter for extending classes"""
        pass

    @property
    @abstractmethod
    def lactose_free(self):
        """Defines property and getter for extending classes"""
        pass

    @property
    @abstractmethod
    def name(self):
        """Defines property and getter for extending classes"""
        pass

    @property
    @abstractmethod
    def description(self):
        """Defines property and getter for extending classes"""
        pass

    @property
    @abstractmethod
    def product_id(self):
        """Defines property and getter for extending classes"""
        pass
