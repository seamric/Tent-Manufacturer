import math
height = float(input('Enter height for tent (in meters) : '))
radius = float(input('Enter radius for tent (in meters) : '))
sl_height = float(input('Enter slant height for tent (in meters) : '))
price_per_unit = 0.5

total_surface_area_cylinder = 2 * math.pi * radius * (radius + height)
total_surface_area_cone = math.pi * radius * (radius + sl_height)
total_surface_area_tent = total_surface_area_cylinder + total_surface_area_cone
total_price_exclusive_tax = (price_per_unit * total_surface_area_tent)
total_tax = 18 / 100 * total_price_exclusive_tax
total_price_inclusive_tax = total_price_exclusive_tax + total_tax
print('Price for this tent is : $', total_price_inclusive_tax)
