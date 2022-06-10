from enum import Enum
from random import randint, shuffle
from typing import List


class Color(Enum):
    blue = "Синий"
    green = "Зелёный"
    red = "Красный"


# We've got 100 items. Blue is most frequently used. Green is more than red.
# So there can be this variant:
# B=5/10;G=3/10;R=2/10
# That's why B is around 50, G is around 30, R is around 20
def guess_number(number: int) -> str:
    colors_list = gen_list()

    return colors_list[number].value


# We will try to generate list only to our number
# This could save some memory and because of frequency we will get same result
def gen_list() -> List[Color]:
    # Quantity
    b = randint(49, 55)  # Blue
    g = randint(29, 35)  # Green
    r = 100 - b - g  # Red

    colors_frequency = [Color.blue]*b + [Color.green]*g + [Color.red]*r
    shuffle(colors_frequency)

    return colors_frequency
