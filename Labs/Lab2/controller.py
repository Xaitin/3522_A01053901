import datetime
import time
import math
from asteroid import Asteroid


class Controller:
    """Controller class to control our asteroids"""

    # Num designates the number of asteroids to be created
    num = 100

    def __init__(self):
        """Constructor for our controller class. Generates asteroids in a list corresponding to the num value"""
        self._asteroid_list = Asteroid.generate_list(Controller.num)

    def simulate(self, seconds):
        """
        Method to simulate movements on the asteroids within our controller.
        Waits till a full second has passed for the first iteration, then iterates
        on each whole second afterward.
        :param seconds: Number of seconds to simulate
        :return: unused. no return
        """
        print("Simulation Start Time: " + str(datetime.datetime.fromtimestamp(time.time())) + "\n")
        size = len(self._asteroid_list)
        print("Moving Asteroids!\n-----------------")
        for z in range(0, seconds, 1):
            time_to_sleep = math.ceil(time.time()) - time.time()
            time.sleep(time_to_sleep)
            for x in range(0, size - 1, 1):
                old_pos = self._asteroid_list[x].move()
                cur_ast = self._asteroid_list[x]
                print("Asteroid {0} Moved! Old Pos: {1}, {2}, {3} -> New Pos: {4}, {5}, {6}".format(
                    cur_ast.get_ast_id(), old_pos[0], old_pos[1], old_pos[2], cur_ast.get_ast_pos()[0],
                    cur_ast.get_ast_pos()[1], cur_ast.get_ast_pos()[2]))
                print(cur_ast.__str__())


def main():
    """
    Main method for execution.
    :return: unused. no return
    """
    my_controller = Controller()
    secs_to_sim = 10
    my_controller.simulate(secs_to_sim)


if __name__ == '__main__':
    main()
