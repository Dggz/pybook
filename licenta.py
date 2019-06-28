

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


def insert_descending(prod_list: list, prod: Product):
    if not len(prod_list):
        prod_list.append(prod)
        return prod_list
    for index, product in enumerate(prod_list):
        if prod.sellingPrice() > product.sellingPrice():
            prod_list.insert(index, prod)
            break
    if prod.sellingPrice() <= prod_list[-1].sellingPrice():
        prod_list.append(prod)

    return prod_list


def initialize_products():
    prod_list = []
    prod_list = insert_descending(prod_list, Product(100))
    prod_list = insert_descending(prod_list, PackagedProduct(70, 10))
    prod_list = insert_descending(prod_list, PackagedProduct(90, 15))
    return prod_list


def avg(prod_list: list):
    return sum([ x.sellingPrice() for x in prod_list ])/len(prod_list)


def main():
    prod_list = initialize_products()
    # [print(prod.sellingPrice()) for prod in prod_list]
    print(avg(prod_list))

if __name__ == '__main__':
    main()
