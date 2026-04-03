import logging
from typing import List

import click

from generative_shopping_list.dish_to_list import dishes_to_shopping_list

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


@click.group()
def main():
    """Generative Shopping List CLI"""
    pass


@main.command()
@click.argument("dishes", nargs=-1, required=True)
def generate_shopping_list(dishes: List[str]):
    shopping_list = dishes_to_shopping_list(dishes)
    LOGGER.info(shopping_list)


if __name__ == "__main__":
    main()
