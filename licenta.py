

class Product:

    def __init__(self, price):
        self.__price = price

    def sellingPrice(self):
        return self.__price


class PackagedProduct(Product):

    def __init__(self, price, packagePrice):
        super().__init__(price)
        self.__packagePrice = packagePrice

    def sellingPrice(self):
        return super().sellingPrice() + self.__packagePrice


class Vehicle:
    def __init__(self, bp):
        if bp > 0:
            self.__basePrice = bp
        else:
            print("Base Price should be more than 0.")


class Car(Vehicle):
    def __init__(self, bp, model=""):
        super().__init__(bp)
        if model != "":
            self.model = model
        else:
            print("Model should not be empty.")


class AutomaticCar(Car):
    def __init__(self, bp, model="", additionalPrice=0):
        super().__init__(bp, model)
        if additionalPrice > 0:
            self.__additionalPrice = additionalPrice
        else:
            print("Additional Price should be more than 0.")


def insert_descending(prod_list: list, prod: Product):
    if not len(prod_list) or prod.sellingPrice() <= prod_list[-1].sellingPrice():
        prod_list.append(prod)
        return prod_list

    for index, product in enumerate(prod_list):
        if prod.sellingPrice() > product.sellingPrice():
            prod_list.insert(index, prod)
            return prod_list


def initialize_products():
    prod_list = []
    prod_list = insert_descending(prod_list, Product(100))
    prod_list = insert_descending(prod_list, PackagedProduct(70, 10))
    prod_list = insert_descending(prod_list, PackagedProduct(90, 15))
    return prod_list


def sort_limit(prods: list, lim: float):
    over = [prod for prod in prods if prod.sellingPrice() > lim]
    for idx in range(len(over)):
        for jdx in range(idx, len(over)):
            if over[idx].sellingPrice() <= over[jdx].sellingPrice():
                newp = over.pop(jdx)
                over.insert(idx, newp)

    for idx, prod in enumerate(over):
        prods.pop(prods.index(prod))
        prods.insert(idx, prod)

    return prods




def avg(prod_list: list):
    return sum([ x.sellingPrice() for x in prod_list ])/len(prod_list)


def main():
    import ipdb; ipdb.set_trace()

    prod_list = initialize_products()

    prod_list.reverse()
    [print(prod.sellingPrice()) for prod in prod_list]
    sorted = sort_limit(prod_list, 100)
    [print(prod.sellingPrice()) for prod in sorted]
    # print(avg(prod_list))

if __name__ == '__main__':
    main()
