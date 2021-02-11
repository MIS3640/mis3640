"""
Question 1:

Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)

Weight on Moon = weight on Earth * 0.165

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""

MOONWEIGHT_MULTIPLE = 0.165


def print_weight_on_moon():
    """Print the equivalent weight on the moon."""
    earth_weight_str = input('Please enter your weight on earth: ')
    earth_weight = float(earth_weight_str)
    moon_weight = earth_weight * MOONWEIGHT_MULTIPLE
    print(f'Your weight on moon is {moon_weight}.')


# print_weight_on_moon()


"""
Question 2:

Write a function that takes two arguments - 1. weight on earth (float), 2. planet (str) - and returns the equivalent weight on that planet. We assume Moon is a planet although it is not.

Weight on Moon = weight on Earth * 0.165
Weight on Mars = weight on Earth * 0.378
Weight on Venus = weight on Earth * 0.904

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""


MOON_MULTIPLE = 0.165
MARS_MULTIPLE = 0.378
VENUS_MULTIPLE = 0.904


def calc_weight_on_planet(weight, planet):
    """Return the equivalent weight on the PLANET based on WEIGHT on earth.

    weight: float
    planet: str
    """
    if planet == 'moon':
        return weight * MOON_MULTIPLE
    elif planet == 'mars':
        return weight * MARS_MULTIPLE
    elif planet == 'venus':
        return weight * VENUS_MULTIPLE
    else:
        return 0


print(calc_weight_on_planet(100, 'mars'))

# weight_on_earth = input("What is your weight on earth in lbs:")
# weight_on_earth = float(weight_on_earth)
# planet = input("Do you want to know your weight on the Moon, Mars, or Venus. Type exactly as is")
# # print(planet)
# planet_weight = calc_weight_on_planet(weight_on_earth, planet)
#
# print(planet_weight)
