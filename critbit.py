"""A module for all critbit related logic."""
from dataclasses import dataclass


@dataclass
class Criteria:
    key: str
    value: int
    specification: dict


@dataclass
class Applicant:
    value: int
    

class CriteriaKeyNotFound(Exception):
    pass


class InvalidApplicant(Exception):
    pass


def create_criteria(objects: set, key_attr: str):
    """Create a criteria from a specified attribute.
    
    Args:
        objects: A collection of Python objects.
        key_attr: The attribute of each object used for a criteria key.
    """
    specification = {}
    value = 0

    try:
        for index, obj in enumerate(objects):
            specification[getattr(obj, key_attr)] = index
            if obj.enabled:
                value += 1 << index
    except AttributeError:
        raise CriteriaKeyNotFound(f'key not found: {key_attr}')

    return Criteria(
        key=key_attr,
        value=value,
        specification=specification
    )

def create_applicant(objects: set, key_attr: str, criteria: Criteria):
    """Create an applicant to evaluate against criteria.

    Args:
        objects: A collection of Python objects.
        key_attr: The attribute of each object used for a criteria key.
        criteria: A criteria object to evaluate against.   
    """
    value = 0

    for obj in objects:
        key = getattr(obj, key_attr)
        if key not in criteria.specification.keys():
            raise InvalidApplicant(
                f'criteria does not have applicant key: {key}')
        value += (1 << criteria.specification[key])

    return Applicant(value=value)
    
def evaluate(applicant: Applicant, criteria: Criteria):
    """Check if applicant satisfies criteria
    
    Args:
        applicant: Applicant object with value based on criteria.
        criteria: Criteria object to evaluate against.
    """
    return (criteria.value & applicant.value) == applicant.value