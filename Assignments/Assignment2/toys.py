from abc import ABC, abstractmethod


class Toys(ABC):
    """Toys abstract base class"""
    @property
    @abstractmethod
    def is_battery_operated(self):
        """Defines property and getter for extending classes"""
        pass

    @property
    @abstractmethod
    def min_rec_age(self):
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
