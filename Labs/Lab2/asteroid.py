import random
import math


class Asteroid:
    """This class embodies the functions and attributes of a asteroid"""
    ast_id = 0

    @classmethod
    def assign_id(cls):
        """
        This is a helper method to assign id's to the asteroids and increment an id counter
        :return: unused. no return
        """
        cls.ast_id += 1
        return cls.ast_id

    def __init__(self, circum, pos, vel):
        """
        Initialize an asteroids circumference, position, and velocity
        :param circum: an int
        :param pos: list of x y and z coords for positions
        :param vel: tuple
        """
        self._circumference = circum
        self._position = pos
        self._velocity = vel
        self._id = Asteroid.assign_id()

    def __str__(self):
        """
        To string method
        :return: String representation of our asteroid
        """
        return "Asteroid {0} is currently at {1}, {2}, {3} and moving at {4}, {5}, {6} metres per second. It has a " \
               "circumference of {7} ".format(self._id, self._position[0], self._position[1], self._position[2],
                                              self._velocity[0], self._velocity[1], self._velocity[2],
                                              self.get_ast_circum())

    def get_ast_circum(self):
        """
        Grabs asteroid circumference
        :return: circumference value
        """
        return self._circumference

    def get_ast_pos(self):
        """
        Grabs list of asteroid position coordinates
        :return: list of coordinates
        """
        return self._position

    def get_ast_vel(self):
        """
        Grabs list of asteroid velocity coordinates
        :return: list of velocity coordinates
        """
        return self._velocity

    def set_ast_pos(self, new_pos):
        """
        Sets the asteroid position during moving
        :param new_pos:
        :return: unused. no return
        """
        self._position = new_pos

    def get_ast_id(self):
        """
        Grabs asteroid id
        :return: int of id
        """
        return self._id

    def move(self):
        """
        Handles movement for the asteroids
        :return: returns a tuple of the last position
        """
        old_position = (self._position[0], self._position[1], self._position[2])
        new_position = [a+b for a, b in zip(self.get_ast_pos(), self.get_ast_vel())]
        self.set_ast_pos(new_position)
        return old_position

    @classmethod
    def generate_list(cls, num):
        """
        Generates and returns of list of asteroids
        :param num: number of asteroids to generate
        :return: list containing asteroids
        """
        count = 0
        my_list = []
        while count <= num:
            radius = random.randrange(1, 4, 1) * random.random()
            x1 = random.randrange(0, 100, 1)
            x2 = random.randrange(0, 5, 1)
            y1 = random.randrange(0, 100, 1)
            y2 = random.randrange(0, 5, 1)
            z1 = random.randrange(0, 100, 1)
            z2 = random.randrange(0, 5, 1)
            my_list.append(Asteroid(radius*math.pi*2, [x1, y1, z1], [x2, y2, z2]))
            count += 1
        return my_list
