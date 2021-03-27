from candy import Candy


class Eggs(Candy):
    """Eggs class for creme eggs extending candy"""
    def __init__(self, nuts, lactose, name, description, p_id, pack_size):
        """Initializer for eggs"""
        self._has_nuts = nuts
        self._lactose_free = lactose
        self._name = name
        self._description = description
        self._product_id = p_id
        self._pack_size = pack_size

    @property
    def has_nuts(self):
        """Defines property and getter from extending classes"""
        return self._has_nuts

    @property
    def lactose_free(self):
        """Defines property and getter from extending classes"""
        return self._lactose_free

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
