from dataclasses import dataclass
from typing import List, Optional, Mapping
from datetime import timedelta
from cheff.ingredients import Ingredient

@dataclass
class Recipe:
    name: str
    ingredients: List[Ingredient]
    #metadata: Optional[Mapping[str, str]]
    #effort: str
    #time: timedelta

    def to_string(self):
        res = []
        res.append(
            f"\n------ Recipe: {self.name} -----"
        )
        for ingredient in self.ingredients:
            res.append(
                f"{ingredient.name:<20}\t{ingredient.measure.size:<3}"
                f" {ingredient.measure.symbol}"
            )
        return "\n".join(res)

@dataclass
class Library:
    name: str
    content: List[Recipe]