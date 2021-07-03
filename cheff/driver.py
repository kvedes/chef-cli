import os
from typing import List
from random import randint
import typer
from cheff.recipe import Library, Recipe
from cheff.ingredients import Ingredient
from cheff.io import DataclassToJson, LibraryFromJson, LibraryAppendWriter

app = typer.Typer()
LIBRARY = os.environ["CHEFF_LIBRARY_PATH"]

# @app.command()
# def add_recipe(name: str, ingredients: List[Ingredient]):
#     recipe = Recipe(name=name, ingredients=ingredients)
#     lib_append = LibraryAppendWriter(LIBRARY)
#     lib_append.append(recipe)

@app.command()
def recipes():
    library = LibraryFromJson().read_library(LIBRARY)
    typer.echo(f"------ Content of library {LIBRARY} ------")
    for recipe in library.content:
        typer.echo(recipe.name)

@app.command()
def get(name: str):
    library = LibraryFromJson().read_library(LIBRARY)
    for recipe in library.content:
        if recipe.name == name:
            typer.echo(recipe.to_string())

@app.command()
def random():
    library = LibraryFromJson().read_library(LIBRARY)
    idx = randint(0, len(library) - 1)
    typer.echo(library.content[idx].to_string())

@app.command()
def publish(name: str):
    '''Publist to ourgroceries. Get password'''
    pass