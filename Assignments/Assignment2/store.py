from InvalidDataError import InvalidDataError
from orderprocessor import OrderProcessor
from enum import Enum
from datetime import datetime


class Stock(Enum):
    """Enumeration for stock values"""
    OUT_OF_STOCK = 0
    IN_STOCK = 9
    LOW = 10
    VERY_LOW = 3


class Store:
    """Store object for running the store"""
    def __init__(self):
        self._inventory = list()
        self._order_processor = OrderProcessor()
        self._order_list = None
        self._transaction_list = list()

    def display_menu(self):
        """Displays menu for the store"""
        user_input = None
        while user_input != 3:
            print("\nWelcome to Cloud9 Superstore Terminal")
            print("-----------------------")
            print("1. Process Web Orders")
            print("2. Check Inventory")
            print("3. Exit and print daily transactions")
            string_input = input("Please enter your choice (1-3)")

            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                self.execute_order_processor()
            elif user_input == 2:
                self.check_inventory()
            elif user_input == 3:
                self.print_transactions_to_file()
            else:
                print("Incorrect input. Displaying menu.")

        print("Thank you for using the Cloud9 Superstore Terminal")

    def add_to_inventory(self, param):
        """Adds items to the store inventory"""
        self._inventory.append(param.product_id)

    def execute_order_processor(self):
        """Executes the order processor"""
        correct_file = False
        try:
            file_name = input("Please enter the name of the excel file to process (without extension)")
            self._order_list = self._order_processor.read_order_file(file_name + ".xlsx")
            correct_file = True
            for order in self._order_list:
                product_id = order.get_product_id()
                num_in_stock = 0
                factory = order.factory()
                item_type = order.get_type()
                for item in self._inventory:
                    if product_id == item:
                        num_in_stock += 1
                qty_to_order = int(order.get_quantity())
                if qty_to_order > num_in_stock:
                    try:
                        for i in range(100):
                            if item_type == "Toy":
                                toy = factory.create_toy(order)
                                self.add_to_inventory(toy)
                            elif item_type == "Candy":
                                candy = factory.create_candy(order)
                                self.add_to_inventory(candy)
                            else:
                                animal = factory.create_stuffed_animal(order)
                                self.add_to_inventory(animal)
                        for i in range(qty_to_order):
                            if item_type == "Toy":
                                toy = factory.create_toy(order)
                                self.remove_from_inventory(toy)
                            elif item_type == "Candy":
                                candy = factory.create_candy(order)
                                self.remove_from_inventory(candy)
                            else:
                                animal = factory.create_stuffed_animal(order)
                                self.remove_from_inventory(animal)
                    except InvalidDataError as e:
                        self._transaction_list.append("Order #" + str(order.get_order_number()) + ', ' + e.message)
                else:
                    try:
                        for i in range(qty_to_order):
                            if item_type == "Toy":
                                toy = factory.create_toy(order)
                                self.remove_from_inventory(toy)
                            elif item_type == "Candy":
                                candy = factory.create_candy(order)
                                self.remove_from_inventory(candy)
                            else:
                                animal = factory.create_stuffed_animal(order)
                                self.remove_from_inventory(animal)
                    except InvalidDataError as e:
                        self._transaction_list.append("Order #" + str(order.get_order_number()) + ', ' + e.message)
                name = order.get_name()
                order_num = order.get_order_number()
                self._transaction_list.append("Order #{0}, Item: {1}, Product ID: {2}, Name: {3}, Quantity: {4}".format(
                    order_num, item_type, product_id, name, qty_to_order
                ))

        except FileNotFoundError:
            print("File name not found")
        return correct_file

    def check_inventory(self):
        """Checks the inventory of the store"""
        list_of_ids = list()
        list_of_counters = list()
        for item in self._inventory:
            if item not in list_of_ids:
                list_of_ids.append(item)
                list_of_counters.append(1)
            else:
                index_to_increment = list_of_ids.index(item)
                list_of_counters[index_to_increment] += 1
        output = ""
        for i in range(len(list_of_ids)):
            qty = list_of_counters[i]
            item_id = list_of_ids[i]
            if qty == Stock.OUT_OF_STOCK.value:
                output += item_id + " is Out of Stock\n"
            elif qty < Stock.VERY_LOW.value:
                output += item_id + " is Very Low in Stock\n"
            elif qty < Stock.LOW.value:
                output += item_id + " is Low in Stock\n"
            elif qty > Stock.IN_STOCK.value:
                output += item_id + " is in Stock\n"
        if output == "":
            print("Inventory is empty")
        else:
            print(output)

    def print_transactions_to_file(self):
        """Prints transaction details to file"""
        timestamp = datetime.today().strftime('%d%m%y_%H%M')
        filename = 'DTR_' + timestamp + '.txt'
        file = open(filename, 'w')
        file.write('CLOUD9 SUPERSTORE - DAILY TRANSACTION REPORT\n')
        file.write(datetime.today().strftime('%d-%m-%Y %H:%M\n'))
        file.writelines('\n%s' % transaction for transaction in self._transaction_list)
        file.close()
        print(self._transaction_list)

    def remove_from_inventory(self, param):
        """Removes items from inventory"""
        self._inventory.remove(param.product_id)
