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


def create_criteria(objects: set, key: str):
    """Create a criteria from a specified attribute."""
    specification = {}
    value = 0

    try:
        for index, obj in enumerate(objects):
            specification[getattr(obj, key)] = index
            if obj.enabled:
                value += 1 << index
    except AttributeError:
        raise CriteriaKeyNotFound(f'key not found: {key}')

    return Criteria(
        key=key,
        value=value,
        specification=specification
    )

def create_applicant(objects: set, criteria: Criteria):
    """Create an applicant to evaluate against criteria."""
    value = 0

    for obj in objects:
        key = getattr(obj, criteria.key)
        if key not in criteria.specification.keys():
            raise InvalidApplicant(
                f'criteria does not have applicant key: {key}')
        value += (1 << criteria.specification[key])

    return Applicant(value=value)

def evaluate(applicant: Applicant, criteria: Criteria):
    """Check if applicant satisfies criteria"""
    return (criteria.value & applicant.value) == applicant.value