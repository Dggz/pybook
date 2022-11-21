"""
We want to simulate a kitchen with two mincers and ovens
One of each for veggies meat

"""


def mincer(food):
    return f"minced {food}"


def oven(temp, food):
    return f"cooked {food} at {temp} degrees Celsius"


veggies = ['spinach', 'carrots', 'cabbage', 'potatoes']
meat = ['beef', 'chicken', 'turkey']


if __name__ == '__main__':
    beef = 'beef'
    minced_beef = mincer(beef)
