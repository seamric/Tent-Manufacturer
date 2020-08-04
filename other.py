import math
price_per_unit = 0.5
height = 0
radius = 0
sl_height = 0
total_price_inclusive_tax = 0


def get_input():
    global height, radius, sl_height
    radius = float(input('Enter radius for tent (in meters) : '))
    sl_height = float(input('Enter slant height for tent (in meters) : '))
    height = float(input('Enter height for tent (in meters) : '))


def calculate():
    global total_price_inclusive_tax
    total_surface_area_cylinder = 2 * math.pi * radius * (radius + height)
    total_surface_area_cone = math.pi * radius * (radius + sl_height)
    total_surface_area_tent = total_surface_area_cylinder + total_surface_area_cone
    total_price_exclusive_tax = (price_per_unit * total_surface_area_tent)
    total_tax = 18 / 100 * total_price_exclusive_tax
    total_price_inclusive_tax = total_price_exclusive_tax + total_tax


def show():
    global total_price_inclusive_tax
    print('Price for this tent is : $', total_price_inclusive_tax)


def run():
    get_input()
    calculate()
    show()
