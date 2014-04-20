__author__ = 'tyler'

import json

class PizzaOrder:

    def __init__(self):
        self.crust = None
        self.sauce = None
        self.toppings = list()


    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)