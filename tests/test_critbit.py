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


def test_no_matches():
    """Test when a match is successful"""
    in_kitchen = (
        Ingredient(name='steak'),
        Ingredient(name='butter'),
        Ingredient(name='salt'),
        Ingredient(name='pepper')
    )

    recipes = [
        Recipe(
            name='pancakes', 
            ingredients=(
                Ingredient(name='milk'),
                Ingredient(name='eggs'),
                Ingredient(name='flower'),
                Ingredient(name='oil')
            )
        )
    ]

    criteria = critbit.create_criteria(in_kitchen, 'name')
    applicants = critbit.create_applicants(recipes, 'ingredients.name', criteria)
    assert not critbit.closest(applicants, criteria)

def test_criteria_key_not_found():
    """Test when specified attribute key doesnt exist for criteria."""
    with pytest.raises(critbit.KeyNotFound):
        fridge = (
            Ingredient(name='milk'),
        )

        critbit.create_criteria(fridge, 'namezzz')

def test_closest():
    """"""
    @dataclass
    class Feature:
        feature_id: str
        name: str

    @dataclass
    class Vehicle:
        vehicle_id: str
        make: str
        features: list

    features = [
        Feature(feature_id=1, name='satnav'),
        Feature(feature_id=2, name='leather seats'),
        Feature(feature_id=3, name='heated seats'),
        Feature(feature_id=4, name='reverse camera'),
        Feature(feature_id=5, name='bluetooth'),
        Feature(feature_id=6, name='remote start'),
        Feature(feature_id=7, name='parking sensors'),
        Feature(feature_id=8, name='apple carplay/android auto'),
        Feature(feature_id=9, name='sun roof'),
        Feature(feature_id=10, name='cruise control'),
    ]

    vehicles = [
        Vehicle(
            vehicle_id=1, 
            make='Ford', 
            features=[
                Feature(feature_id=4, name='reverse camera')
            ]
        ),
        Vehicle(
            vehicle_id=2, 
            make='BMW', 
            features=[
                Feature(feature_id=1, name='satnav'),
            ]
        ),
        Vehicle(
            vehicle_id=3, 
            make='Mercedes', 
            features=[
                Feature(feature_id=1, name='satnav'),
                Feature(feature_id=4, name='reverse camera'),
                Feature(feature_id=9, name='sun roof'),
            ]
        )
    ]

    criteria = critbit.create_criteria(features, 'feature_id')
    applicants = critbit.create_applicants(vehicles, 'features.feature_id', criteria)
    closest = critbit.closest(applicants, criteria)

    assert closest.object.vehicle_id == 3