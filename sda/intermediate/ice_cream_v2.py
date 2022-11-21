''''''
from copy import copy, deepcopy

"""
We want to simulate a small shop that has multiple ice cream machines

They will be 'installed' with certain settings:
    dairy ice cream or just sorbet - instance attributes
    default internal temperatures depending on the type - class attrs
    default flavour is vanilla, the machine can accept other flavours as well - default as class attr
    the resulting ice cream temp will be a result of the initial/specified temp
        and heat loss from ingredients
            +1 degree for sorbet +2 for dairy as a result
        - class attrs
    we might want to be able to change the internal temp for warmer or colder ice cream - instance attr
    Internal settings can be changed after installation
    
    The flavours panel might not work as expected in case of electrical failures
    instance =~ object
    
    Exercitiu:
    ---
    Implementati mecanismul care goleste tuburile pe masura ce se face inghetata
        ex: instalam masina cu un tub de vanilie capabil sa produca 5 inghetate
            apelam machine.make_ice_cream('vanilie') de 5 ori => output 5 inghetate
                a 6a oara: EmptyMachineException.
    Instantiati 3 masini de inghetata si folositi-le pana la epuizare, tratati exceptiile
    ---
"""
import json


class UnavailableFlavourException(Exception):
    """Exception raised when requesting unavailable flavour"""
    def __init__(self, message):
        super().__init__(message)


class IceCreamMachine(object):
    flavours = {'vanilla': 1}
    default_dairy_temp, default_sorbet_temp, default_vegan_temp = 3, 5, 7
    dairy_temp_loss, sorbet_temp_loss, vegan_temp_loss = 1, 2, 5

    def __init__(self, ic_type, temp=None, flavours=()):
        self.ic_type = ic_type
        self.temp = temp if temp else getattr(self, f"default_{self.ic_type}_temp")
        self.temp_loss = getattr(self, f"{self.ic_type}_temp_loss")
        self.flavours = flavours

    def make_ice_cream(self, flavour):
        if flavour not in self.flavours:
            raise UnavailableFlavourException(f"{flavour} is not available on this machine!"
                                              f"Please choose one of the following: {self.flavours}")
        # tub
        return f"{flavour} {self.ic_type if self.ic_type == 'sorbet' else 'ice cream'} " \
               f"at {self.temp + self.temp_loss} degrees"


if __name__ == '__main__':
    sorbet_machine = IceCreamMachine('sorbet', flavours={'vanilla': 4, 'strawberry': 3, 'chocolate': 15})

    # numbers = [1, 2, 3]
    # assigned = numbers
    # copied = copy(numbers)
    # deep_copied = deepcopy(numbers)
    print("Available flavours: ", sorbet_machine.flavours)
    nums = [45, 435, 345, 4567, 456, 756, 6745, 456, 7]
    sorted(nums)
    command = input("Choose a flavour: ")
    stop_code = 'stop'
    while command != stop_code:
        try:
            ice_cream = sorbet_machine.make_ice_cream(command)
            print(ice_cream)
        except UnavailableFlavourException as fl_exc:
            print(fl_exc)
            command = input("Choose another flavour: ")
            ice_cream = sorbet_machine.make_ice_cream(command)
            print(ice_cream)
        command = input("Choose another flavour: ")
    print("End of day, cleaning machine!")
