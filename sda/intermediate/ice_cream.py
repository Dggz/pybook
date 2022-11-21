"""
We want to simulate a small shop that has multiple ice cream machines

They will be 'installed' with certain settings:
    dairy ice cream or just sorbet
    default internal temperatures depending on the type
    the resulting ice cream temp will be a result of the initial/specified temp
        and heat loss from ingredients
            +1 degree for sorbet +2 for dairy as a result
    we might want to be able to change to internal temp for warmer or colder ice cream


"""
from datetime import datetime
from time import sleep


class IceCreamMachine:
    default_dairy_temp = 3
    default_sorbet_temp = 5
    flavours = []

    def __init__(self, ic_type, temp=None):
        self.ic_type = ic_type
        self.temp = temp if temp else getattr(self, f"default_{ic_type}_temp")
        # maybe add exception if we get a different type and/or wrong temps
        self.temp_loss = 1 if self.ic_type == 'sorbet' else 2
        self.creation_date = datetime.now()

    def make_ice_cream(self, flavour):
        return f"{flavour} {self.ic_type if self.ic_type == 'sorbet' else 'ice cream'} " \
               f"at {self.temp + self.temp_loss} degrees"


if __name__ == '__main__':
    ic = IceCreamMachine('sorbet')
    type(ic)
    vanilla_ic = ic.make_ice_cream('vanilla')  # make_ice_cream(ic, 'vanilla')
    strawberry_ic = ic.make_ice_cream('strawberry')

    # sleep(5)

    ic2 = IceCreamMachine('dairy', 10)
    choc_ic = ic2.make_ice_cream('chocolate')
    print()
    # print(isinstance(ic, IceCreamMachine))

















    # dairy_machine = IceCreamMachine('dairy')
    # sb_ic = dairy_machine.make_ice_cream('strawberry')
    # print(sb_ic)
