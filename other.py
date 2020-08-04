import math

height = 0
radius = 0
sl_height = 0
total_price_inclusive_tax = 0


def get_input():
    global height, radius, sl_height
    radius = float(input('Enter radius for tent (in meters) : '))
    sl_height = float(input('Enter slant height for tent (in meters) : '))
    height = float(input('Enter height for tent (in meters) : '))


class Tent:

    price_per_unit = 0.5

    def __init__(self, h, r, sl):
        self.h = h
        self.r = r
        self.sl = sl
        print('Generating price for this tent...')

    def show(self):
        print('Price for this tent is : $', Tent.calculate(self))

    def calculate(self):
        total_surface_area_cylinder = 2 * math.pi * self.r * (self.r + self.h)
        total_surface_area_cone = math.pi * self.r * (self.r + self.sl)
        total_surface_area_tent = total_surface_area_cylinder + total_surface_area_cone
        total_price_exclusive_tax = (
            Tent.price_per_unit * total_surface_area_tent)
        total_tax = 18 / 100 * total_price_exclusive_tax
        total_price_inclusive_tax = total_price_exclusive_tax + total_tax
        return total_price_inclusive_tax


def run():
    T1 = Tent(height, radius, sl_height)
    T1.show()
