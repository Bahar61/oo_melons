from random import randint

"""Classes for melon orders."""
class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from"""
    def __init__(self, species, qty):
        """initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False

 
    def get_base_price(self):
        """Get base price"""

        base_price = randint(5,10)

        return base_price


    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "christmas_melons":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True     


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):

        super().__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):    
        if self.qty < 10:
            total = super().get_total() + 3
        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """pass a security inspection"""
    tax = 0

    def __init__(self, species, qty):
        """initialize attributes"""
        super().__init__(species,qty)
        self.passed_inspection = False


    def mark_inspection(self):
        """Mark inspection"""

        self.passed_inspection = True



