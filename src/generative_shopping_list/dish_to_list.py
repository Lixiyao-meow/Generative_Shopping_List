import yaml
import logging
from typing import List, Dict

LOGGER = logging.getLogger(__name__)


def dishes_to_shopping_list(
    dishes: List[str],
) -> Dict[str, Dict[str, str | int | float]]:
    # NOTE: We make a big assumption that all units of a given ingredient are the same across all recipes.

    # read yaml file
    recipe_path = "./ingredients/recipe.yaml"
    with open(recipe_path, "r") as file:
        recipes = yaml.safe_load(file)

    shopping_list = {}

    for dish in dishes:
        if dish not in recipes:
            LOGGER.warning(f"{dish} not found in recipes.")
            continue
        for ingredient, details in recipes[dish]["ingredients"].items():
            shopping_list.setdefault(
                ingredient, {"amount": 0, "unit": details["unit"]}
            )["amount"] += details["amount"]

    return shopping_list
