from intermediate.pizza import DoughFactory, Pizza


class OrganicDoughFactory(DoughFactory):
    def get_dough(self):
        return "organic dough"


class OrganicPizza(Pizza, OrganicDoughFactory): pass


if __name__ == '__main__':
    bio_pizza = OrganicPizza()
    bio_pizza.order_pizza('Tomatoes', 'Prosciutto')
    # help(OrganicPizza)
