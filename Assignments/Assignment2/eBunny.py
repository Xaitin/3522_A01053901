from stuffedanimals import StuffedAnimals


class EBunny(StuffedAnimals):
    """Easter Bunny extending stuffed animals"""
    def __init__(self, stuffing, size, fabric, name, description, p_id, color):
        self._stuffing = stuffing
        self._size = size
        self._fabric = fabric
        self._name = name
        self._description = description
        self._product_id = p_id
        self._color = color

    @property
    def stuffing(self):
        """Defines property and getter from extending classes"""
        return self._stuffing

    @property
    def size(self):
        """Defines property and getter from extending classes"""
        return self._size

    @property
    def fabric(self):
        """Defines property and getter from extending classes"""
        return self._fabric

    @property
    def name(self):
        """Defines property and getter from extending classes"""
        return self._name

    @property
    def description(self):
        """Defines property and getter from extending classes"""
        return self._description

    @property
    def product_id(self):
        """Defines property and getter from extending classes"""
        return self._product_id
