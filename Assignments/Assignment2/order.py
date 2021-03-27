class Order:
    """Order items utilized by our order processor"""
    def __init__(self, ord_num, prod_id, quantity, item_type, name, details, factory):
        """Order initializer"""
        self._ord_num = ord_num
        self._prod_id = prod_id
        self._type = item_type
        self._quantity = quantity
        self._name = name
        self._details = details
        self._factory = factory

    def get_order_number(self):
        """Grabs order number"""
        return self._ord_num

    def get_product_id(self):
        """Grabs product id"""
        return self._prod_id

    def get_type(self):
        """Grabs item type"""
        return self._type

    def get_name(self):
        """Grabs item name"""
        return self._name

    def get_details(self):
        """Grabs item details"""
        return self._details

    def factory(self):
        """Grabs factory of item"""
        return self._factory

    def get_quantity(self):
        """Grabs item quantity"""
        return self._quantity
