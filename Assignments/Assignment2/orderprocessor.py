import pandas as pd
from order import Order
from christmasproductfactory import ChristmasProductFactory
from easterproductfactory import EasterProductFactory
from spookyproductfactory import SpookyProductFactory


class OrderProcessor:
    """Order processor class for reading the excel files"""
    def __init__(self):
        """Initializer for order processing"""
        self._order_list = []

    def read_order_file(self, file_name):
        """Reading order files"""
        orders = pd.read_excel(file_name)
        # print('Excel Sheet to Dict:', orders.to_dict(orient='records'))
        orders = orders.to_dict(orient='records')
        for order in orders:
            if order['holiday'] == 'Christmas':
                factory = ChristmasProductFactory()
            elif order['holiday'] == 'Easter':
                factory = EasterProductFactory()
            else:
                factory = SpookyProductFactory()

            # details = orders.drop(['holiday'], ['order_number'], ['product_id'], ['item'], ['name'])
            details = order.copy()
            del details['holiday']
            del details['order_number']
            del details['product_id']
            del details['item']
            del details['name']
            new_order = Order(order['order_number'], order['product_id'], order['quantity'], order['item'],
                              order['name'], details, factory)
            self._order_list.append(new_order)
        return self._order_list
