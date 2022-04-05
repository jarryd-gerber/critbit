"""A module for all critbit related logic."""
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Criteria:
    key: str
    value: int
    options: Dict[str, int]
    objects: List[object]


@dataclass
class Applicant:
    key: str
    value: int
    object: object
    

class KeyNotFound(Exception):
    pass


def create_criteria(objects: List[object], key_attr: str) -> Criteria:
    """Create a criteria from a specified attribute.
    
    Args:
        objects: A collection of Python objects.
        key_attr: The attribute of each object used for a criteria key.
    """
    value = 0
    options = {}

    try:
        for index, obj in enumerate(objects):
            key = getattr(obj, key_attr)
            options[key] = index
            value += 1 << options[key]
    except AttributeError:
        raise KeyNotFound(f'key not found: {key_attr}')

    return Criteria(
        key=key_attr,
        value=value,
        options=options,
        objects=objects
    )

def create_applicant(parent: object, key_attr: str, criteria: Criteria) -> Applicant:
    """Create an applicant from a list of criterion.

    Args:
        objects: A collection of Python objects.
        key_attr: The attribute of each object used for a criterion.
        criteria: A criteria object to evaluate against.   
    """
    value = 0
    attrs = key_attr.split('.')
    children = getattr(parent, attrs[0])

    try:
        for obj in children:
            key = getattr(obj, attrs[1])
            if key not in criteria.options.keys():
                continue
            value += (1 << criteria.options[key])
    except AttributeError:
        raise KeyNotFound(f'key not found: {key_attr}')

    return Applicant(
        key=key_attr,
        value=value,
        object=parent
    )

def create_applicants(objects: List[object], key_attr: str, criteria: Criteria) -> List[Applicant]:
    """Create a collection of applicants from input objects.

    Args:
        objects: A collection of Python objects.
        key_attr: The object attribute to match against criteria.
        criteria: A criteria object to evaluate against.   
    """
    applicants = []

    for obj in objects:
        applicants.append(
            create_applicant(obj, key_attr, criteria)) 

    return applicants

def closest(applicants: List[Applicant], criteria: Criteria) -> Applicant:
    """Find an applicant with the closest match for a given criteria.

    Args:
        applicants: Collection of Applicant objects.
        criteria: Criteria object to evaluate against.
    """
    most = 0
    closest = None

    # Brian Kernighan bit counting
    def count_set_bits(n):
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count

    for applicant in applicants:
        matches = count_set_bits(applicant.value & criteria.value)
        if matches and matches > most:
            most = matches
            closest = applicant

    return closest