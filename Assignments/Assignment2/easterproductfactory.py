from InvalidDataError import InvalidDataError
from productfactory import ProductFactory
from eggs import Eggs
from eBunny import EBunny
from rbunny import RBunny


class EasterProductFactory(ProductFactory):
    """Factory for creating easter related items"""
    def __init__(self):
        """Initializer for easter product factories"""
        pass

    def create_candy(self, item):
        """Creating creme eggs for easter."""
        product_id = item.get_product_id()
        name = item.get_name()
        other_info = item.get_details()
        description = other_info['description']
        has_lactose = other_info['has_lactose']
        has_nuts = other_info['has_nuts']
        pack_size = other_info['pack_size']
        if has_lactose != "Y":
            raise InvalidDataError("Could Not process order data corrupted, InvalidDataError "
                                   "- Creme Eggs must not be Lactose Free")
        elif has_nuts != "Y":
            raise InvalidDataError("Could Not process order data corrupted, InvalidDataError "
                                   "- Creme Eggs may have nuts")
        object_to_return = Eggs(has_nuts, has_lactose, name, description, product_id, pack_size)
        return object_to_return

    def create_toy(self, item):
        """creating Robot Bunnies for easter"""
        product_id = item.get_product_id()
        name = item.get_name()
        other_info = item.get_details()
        description = other_info['description']
        color = other_info['colour']
        num_effects = other_info['num_sound']
        min_age = other_info['min_age']
        has_batteries = other_info['has_batteries']
        if has_batteries != 'Y':
            raise InvalidDataError("Could Not process order data corrupted, InvalidDataError "
                                   "- Robot Bunnies need Batteries")
        if color != 'Orange' and color != 'Blue' and color != 'Pink':
            raise InvalidDataError("Could Not process order data corrupted, InvalidDataError "
                                   "- Robot Bunnies must be Orange Blue or Pink")
        object_to_return = RBunny(has_batteries, min_age, name, description, product_id, num_effects, color)
        return object_to_return

    def create_stuffed_animal(self, item):
        """creating Easter Bunnies for easter"""
        product_id = item.get_product_id()
        name = item.get_name()
        other_info = item.get_details()
        description = other_info['description']
        fabric = other_info['fabric']
        size = other_info['size']
        stuffing = other_info['stuffing']
        color = other_info['colour']
        if fabric != "Linen":
            raise InvalidDataError("Could Not process order data corrupted, InvalidDataError - "
                                   "Easter Bunnies must be made out of Linen")
        if stuffing != "Polyester Fibrefill":
            raise InvalidDataError("Could Not process order data corrupted, InvalidDataError - "
                                   "Easter Bunnies must be stuffed with Polyester Fibrefill")
        object_to_return = EBunny(stuffing, size, fabric, name, description, product_id, color)
        return object_to_return
