"""A module for all of critbit related tests."""

from dataclasses import dataclass
import critbit


@dataclass
class Ingredient:
    name: str
    enabled: bool = None

@dataclass
class Recipe:
    name: str
    ingredients: set


def test_match_successful():
    """Test when a match is successful"""
    in_kitchen = (
        Ingredient(name='milk', enabled=True),
        Ingredient(name='eggs', enabled=True),
        Ingredient(name='flower', enabled=True),
        Ingredient(name='oil', enabled=True),
        Ingredient(name='steak', enabled=True),
        Ingredient(name='butter', enabled=True),
        Ingredient(name='salt', enabled=True),
        Ingredient(name='pepper', enabled=True)
    )

    recipe = Recipe(
        name='pancakes', 
        ingredients=(
            Ingredient(name='milk'),
            Ingredient(name='eggs'),
            Ingredient(name='flower'),
            Ingredient(name='oil')
        )
    )

    criteria = critbit.create_criteria(in_kitchen, 'name')
    submission = critbit.create_submission(recipe.ingredients, criteria)

    assert critbit.match(submission, criteria)

def test_match_unsuccessful():
    """Test when a match is successful"""
    in_kitchen = (
        Ingredient(name='milk', enabled=True),
        Ingredient(name='eggs', enabled=False),
        Ingredient(name='flower', enabled=True),
        Ingredient(name='oil', enabled=True),
        Ingredient(name='steak', enabled=True),
        Ingredient(name='butter', enabled=True),
        Ingredient(name='salt', enabled=True),
        Ingredient(name='pepper', enabled=True)
    )

    recipe = Recipe(
        name='pancakes', 
        ingredients=(
            Ingredient(name='milk'),
            Ingredient(name='eggs'),
            Ingredient(name='flower'),
            Ingredient(name='oil')
        )
    )

    criteria = critbit.create_criteria(in_kitchen, 'name')
    submission = critbit.create_submission(recipe.ingredients, criteria)

    assert not critbit.match(submission, criteria)