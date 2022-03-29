"""A module for all critbit related logic."""

from dataclasses import dataclass

@dataclass
class Criteria:
    key: str
    value: int
    specification: dict


def create_criteria(objects: set, key: str):
    """Given a list of objects, generate criteria from a specified attribute."""
    specification = {}
    value = 0

    try:
        for index, obj in enumerate(objects):
            specification[getattr(obj, key)] = index
            if obj.enabled:
                value += 1 << index
    except AttributeError:
        raise Exception(f'key does not exist: {key}')

    return Criteria(
        key=key,
        value=value,
        specification=specification
    )

def create_submission(objects: set, criteria: Criteria):
    """Given a list of objects, generate a submission to match against criteria."""
    submission = 0

    for obj in objects:
        key = getattr(obj, criteria.key)
        if key not in criteria.specification.keys():
            raise Exception(f'specification does not support submission key: {key}')
        submission += (1 << criteria.specification[key])

    return submission

def match(submission: int, criteria: Criteria):
    """Check if submission satisfies criteria"""
    return (criteria.value & submission) == submission