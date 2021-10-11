from enum import Enum

class PizzaSize(Enum):
    # Enum members written as: name = value
    small = 120
    medium = 200
    large = 280
    jumbo = 450

    def __str__(self):
        return self.name

    @property
    def price(self):
        return self.value


class Pizza:
    """A pizza with a size and optional toppings."""

    def __init__(self, size: PizzaSize):
        if not isinstance(size, PizzaSize):
            raise TypeError('Size must be a PizzaSize')
        self.size = size
        self.toppings = []

    def get_price(self):
        """Price of pizza depends on size and number of toppings."""
        #Introduce explanatory variable
        price = self.size.price + 20*len(self.toppings)
        return price

    def add_topping(self, topping):
        """Add a topping to the pizza"""

        if topping not in self.toppings:
            self.toppings.append(topping)

    def __str__(self):
        # create printable description of the pizza such as
        # "small pizza with muschroom" or "small plain pizza"
        description = self.size.name
        if self.toppings:
            description += " pizza with "+ ", ".join(self.toppings)
        else:
            description += " plain pizza"
        return description

