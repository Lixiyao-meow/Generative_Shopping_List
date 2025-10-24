import generative_shopping_list.dish_to_list as gen_shop
import pytest


def test_does_not_crash():
    """Test that the function does not crash with an empty list."""
    assert gen_shop.dishes_to_shopping_list([]) == {}


@pytest.mark.parametrize("dish", ["teriyaki_chicken"])
def test_works_for_example(dish: str):
    assert gen_shop.dishes_to_shopping_list([dish]) is not None
