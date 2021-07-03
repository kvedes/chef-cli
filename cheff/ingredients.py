from dataclasses import dataclass
from typing import Union

class Measure:

    def __init__(
        self,
        si_prefix: str,
        dimension: str,
        size: Union[float, int],
        symbol: str
    ):
        self.si_prefix = si_prefix
        self.dimension = dimension
        self.size = size
        self.symbol = symbol
    
    def __add__(self, other):
        if isinstance(other, type(self)):
            return self.size + other.size
        elif isinstance(other, int):
            return self.size + other
        elif isinstance(other, float):
            return self.size + other
        else:
            raise ValueError(
                f"Cannot add objects of types {type(self)} and {type(other)}"
            )

    def __mul__(self, other):
        if isinstance(other, type(self)):
            return self.size * other.size
        elif isinstance(other, int):
            return self.size * other
        elif isinstance(other, float):
            return self.size * other
        else:
            raise ValueError(
                f"Cannot add objects of types {type(self)} and {type(other)}"
            )

    __radd__ = __add__
    __rmul__ = __mul__

class Kilograms(Measure):

    def __init__(self, size: float):
        super().__init__("kilo", "weight", size, "kg")


class Liter(Measure):

    def __init__(self, size: float):
        super().__init__(None, "volume", size, "L")

class TableSpoon(Measure):
    def __init__(self, size: float):
       super().__init__(None, "volume", size, "tbsp")

measure_map = {
    "kilogram": Kilograms,
    "liter": Liter,
    "tablespoon": TableSpoon
}

@dataclass
class Ingredient:
    name: str
    measure: Measure
