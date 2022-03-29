"""A module for all of critbit related tests."""
import pytest
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
    submission = critbit.create_applicant(recipe.ingredients, criteria)

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
    submission = critbit.create_applicant(recipe.ingredients, criteria)

    assert not critbit.match(submission, criteria)

def test_invalid_applicant():
    """Test when a applicant key doesn't exist in the criteria."""
    with pytest.raises(critbit.InvalidApplicant):
        in_kitchen = (
            Ingredient(name='milk', enabled=True),
        )

        recipe = Recipe(
            name='pancakes', 
            ingredients=(
                Ingredient(name='oil'),
            )
        )

        criteria = critbit.create_criteria(in_kitchen, 'name')
        critbit.create_applicant(recipe.ingredients, criteria)

def test_criteria_key_not_found():
    """Test when a submission key doesn't exist in the criteria."""
    with pytest.raises(critbit.CriteriaKeyNotFound):
        in_kitchen = (
            Ingredient(name='milk', enabled=True),
        )

        critbit.create_criteria(in_kitchen, 'namezzz')