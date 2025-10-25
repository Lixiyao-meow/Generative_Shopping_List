import logging
from typing import Any, Dict, List

from generative_shopping_list.storage import StorageBackend, YamlFileStorage

LOGGER = logging.getLogger(__name__)


def dishes_to_shopping_list(
    dishes: List[str], storage_backend: StorageBackend | None = None
) -> Dict[str, Dict[str, str | int | float]]:
    # NOTE: We make a big assumption that all units of a given ingredient are the same across all recipes.

    # read yaml file
    if storage_backend is None:
        storage_backend = YamlFileStorage("./ingredients/recipe.yaml")
    recipes: Dict[str, Any] = storage_backend.read()

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
