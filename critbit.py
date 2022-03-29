"""A module for all critbit related logic."""

from dataclasses import dataclass


@dataclass
class Criteria:
    key: str
    value: int
    specification: dict


@dataclass
class Submission:
    value: int
    

class CriteriaKeyNotFound(Exception):
    pass


class InvalidSubmission(Exception):
    pass


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
        raise CriteriaKeyNotFound(f'key not found: {key}')

    return Criteria(
        key=key,
        value=value,
        specification=specification
    )

def create_submission(objects: set, criteria: Criteria):
    """Given a list of objects, generate a submission to match against criteria."""
    value = 0

    for obj in objects:
        key = getattr(obj, criteria.key)
        if key not in criteria.specification.keys():
            raise InvalidSubmission(f'Criteria does not own key: {key}')
        value += (1 << criteria.specification[key])

    return Submission(value=value)

def match(submission: Submission, criteria: Criteria):
    """Check if submission satisfies criteria"""
    return (criteria.value & submission.value) == submission.value