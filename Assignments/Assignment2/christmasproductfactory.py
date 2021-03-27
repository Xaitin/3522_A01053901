from InvalidDataError import InvalidDataError
from productfactory import ProductFactory
from workshop import Workshop
from reindeer import Reindeer
from canes import Canes


class ChristmasProductFactory(ProductFactory):
    """Creates christmas themed items"""
    def __init__(self):
        """Initializer for the factory"""
        pass

    def create_candy(self, item):
        """Creating Candy Canes for Christmas."""
        product_id = item.get_product_id()
        name = item.get_name()
        other_info = item.get_details()
        description = other_info['description']
        has_lactose = other_info['has_lactose']
        has_nuts = other_info['has_nuts']
        color = other_info['colour']
        if has_lactose != "N":
            raise InvalidDataError("Could Not process order data corrupted, InvalidDataError "
                                   "- Candy Canes are Lactose Free")
        elif has_nuts != "N":
            raise InvalidDataError("Could Not process order data corrupted, InvalidDataError "
                                   "- Candy Canes are Nut Free")
        object_to_return = Canes(has_nuts, has_lactose, name, description, product_id, color)
        return object_to_return

    def create_toy(self, item):
        """creating Santa's Workshops for Christmas"""
        product_id = item.get_product_id()
        name = item.get_name()
        other_info = item.get_details()
        description = other_info['description']
        dimensions = str(other_info['dimensions'])
        rooms = other_info['num_rooms']
        formatted = dimensions.split(',')
        if formatted[0] == 'nan':
            raise InvalidDataError("Could Not process order data corrupted, InvalidDataError "
                                   "- Incorrect Dimensions")
        height = formatted[0]
        width = formatted[1]
        min_age = other_info['min_age']
        has_batteries = other_info['has_batteries']
        if has_batteries != "N":
            raise InvalidDataError("Could Not process order data corrupted, InvalidDataError "
                                   "- Santa's Workshop doesnt need batteries")
        object_to_return = Workshop(has_batteries, min_age, name, description, product_id, height, width, rooms)
        return object_to_return

    def create_stuffed_animal(self, item):
        """creating Reindeer for Christmas"""
        product_id = item.get_product_id()
        name = item.get_name()
        other_info = item.get_details()
        description = other_info['description']
        fabric = other_info['fabric']
        size = other_info['size']
        stuffing = other_info['stuffing']
        glow = other_info['has_glow']
        if fabric != "Cotton":
            raise InvalidDataError("Could Not process order data corrupted, InvalidDataError "
                                   "- Reindeer Fabric must be Cotton")
        elif stuffing != "Wool":
            raise InvalidDataError("Could Not process order data corrupted, InvalidDataError "
                                   "- Reindeer Stuffing must be Wool")
        elif glow != "Y":
            raise InvalidDataError("Could Not process order data corrupted, InvalidDataError "
                                   "- Reindeer have Glow in the Dark Noses")
        object_to_return = Reindeer(stuffing, size, fabric, name, description, product_id, glow)
        return object_to_return
