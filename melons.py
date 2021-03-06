"""Classes for melon orders."""

from random import randint
from datetime import datetime

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    tax = None
    order_type = None

    def __init__(self, species, qty, country_code=None):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code

    def get_base_price(self):
        """Splurge price by choosing random number between 5-9 as base price"""

        splurge_pricing = randint(5, 9)

        rush_hour = 0
        # 0-6 is mon-sunday
        today = datetime.today()
        time = datetime.time(today)
        if 0 <= today.weekday() <= 4 and 8 <= time.hour <= 11:
            rush_hour = 4

        return splurge_pricing + rush_hour

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price
        
        return total    

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class GovernmentMelonOrder(AbstractMelonOrder):
    """Melon order purchased by the US Government."""

    tax = 0
    order_type = 'government'

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.pass_inspection = False

    def mark_inspection(self, passed):
        """checks if inspection is passed.

        Takes boolean input as argument.
        """
        
        self.passed_inspection = passed

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax = 0.08
    order_type = 'domestic'


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    tax = 0.17
    order_type = "international"

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Flat fee of $3 added to order with less than 10 melons.

        If more than 10 melons then return the regular total no added fee.
        """
        if self.qty < 10:
            return super().get_total() + 3
        else:
            return super().get_total()



