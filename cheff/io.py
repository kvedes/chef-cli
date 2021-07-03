import json
from cheff.recipe import Library, Recipe
from cheff.ingredients import measure_map, Ingredient
import dataclasses

class LibraryFromJson:

    def read_library(self, path: str) -> Library:
        with open(path, "r") as f:
            loaded_json = json.load(f)
        
        # Validate keys in json
        LibraryFromJson.validate_keys(loaded_json, Library.__annotations__)

        # Load recipes
        recipes = []
        for recipe in loaded_json['content']:
            LibraryFromJson.validate_keys(recipe, Recipe.__annotations__)
            
            ingredient_list = []
            for ingredient in recipe['ingredients']:
                
                # Get the measure type
                ingredient_keys = [key for key in ingredient.keys() if key != 'name']
                assert len(ingredient_keys) == 1, f"Too many keys for ingredient {ingredient_keys}"
                
                measure_type_str = ingredient_keys[0]
                measure_type = measure_map[measure_type_str]

                ingredient_list.append(

                    Ingredient(
                        name=ingredient['name'],
                        measure=measure_type(ingredient[measure_type_str])
                    )
                )
            recipes.append(
                Recipe(name=recipe['name'], ingredients=ingredient_list)
            )

        return Library(name=loaded_json['name'], content=recipes)

    @staticmethod
    def validate_keys(dictionary: dict, target_dict: dict):
        if set(dictionary) != set(target_dict):
            raise ValueError(
                "Keys are not matching between Recipe and json:"
                f" {set(dictionary)}, {set(target_dict)}"
            )

class DataclassToJson:

    @staticmethod
    def to_json(dataclass_obj, file_path: str):
        with open(file_path, "w") as f:
            json.dump(
                dataclasses.asdict(dataclass_obj), 
                f
            )

class LibraryAppendWriter:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def append(self, recipe: Recipe):
        library = LibraryFromJson().read_library(self.file_path)

        library['content'].append(recipe)
        DataclassToJson.to_json(library, self.file_path)
