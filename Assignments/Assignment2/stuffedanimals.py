from abc import ABC, abstractmethod


class StuffedAnimals(ABC):
    """Stuffed animals parent abstract class for items"""

    @property
    @abstractmethod
    def stuffing(self):
        """Defines property and getter for extending classes"""
        pass

    @property
    @abstractmethod
    def size(self):
        """Defines property and getter for extending classes"""
        pass

    @property
    @abstractmethod
    def fabric(self):
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
