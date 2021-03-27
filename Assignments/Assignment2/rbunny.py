from toys import Toys


class RBunny(Toys):
    """Robot Bunny getting extended by Toys"""
    def __init__(self, battery, min_age, name, description, p_id, num_effects, color):
        """Initializer method for robot bunnies"""
        self._is_battery_operated = battery
        self._min_rec_age = min_age
        self._name = name
        self._description = description
        self._product_id = p_id
        self._num_effects = num_effects
        self._color = color

    @property
    def is_battery_operated(self):
        """Defines property and getter from extending classes"""
        return self._is_battery_operated

    @property
    def min_rec_age(self):
        """Defines property and getter from extending classes"""
        return self._min_rec_age

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
