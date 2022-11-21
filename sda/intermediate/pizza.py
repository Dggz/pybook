"""
Inheritance, Polymorphism, MRO, Dependency Injection
"""


class DoughFactory:
    def get_dough(self):
        return "standard dough"


class Pizza(DoughFactory):
    def order_pizza(self, *toppings):
        print("Getting dough")
        dough = super().get_dough()
        print("Making pizza with {}".format(dough))
        for topping in toppings:
            print(f"Adding {topping}")


if __name__ == '__main__':
    pizza = Pizza()
    pizza.order_pizza('Mozzarella', 'Basil')
    help(Pizza)
