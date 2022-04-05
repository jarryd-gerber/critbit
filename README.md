# critbit
Search objects based on criteria, fast.


## Usage

Eg.

Given a collection of required Features, find the Vehicle that most closely matches those requirements.
```
In [51]:     @dataclass
    ...:     class Feature:
    ...:         feature_id: str
    ...:         name: str
    ...:
    ...:     @dataclass
    ...:     class Vehicle:
    ...:         vehicle_id: str
    ...:         make: str
    ...:         features: list
    ...:
    ...:     features = [
    ...:         Feature(feature_id=1, name='satnav'),
    ...:         Feature(feature_id=2, name='leather seats'),
    ...:         Feature(feature_id=3, name='heated seats'),
    ...:         Feature(feature_id=4, name='reverse camera'),
    ...:         Feature(feature_id=5, name='bluetooth'),
    ...:         Feature(feature_id=6, name='remote start'),
    ...:         Feature(feature_id=7, name='parking sensors'),
    ...:         Feature(feature_id=8, name='apple carplay/android auto'),
    ...:         Feature(feature_id=9, name='sun roof'),
    ...:         Feature(feature_id=10, name='cruise control'),
    ...:     ]
    ...:
    ...:     vehicles = [
    ...:         Vehicle(
    ...:             vehicle_id=1,
    ...:             make='Ford',
    ...:             features=[
    ...:                 Feature(feature_id=4, name='reverse camera')
    ...:             ]
    ...:         ),
    ...:         Vehicle(
    ...:             vehicle_id=2,
    ...:             make='BMW',
    ...:             features=[
    ...:                 Feature(feature_id=1, name='satnav'),
    ...:             ]
    ...:         ),
    ...:         Vehicle(
    ...:             vehicle_id=3,
    ...:             make='Mercedes',
    ...:             features=[
    ...:                 Feature(feature_id=1, name='satnav'),
    ...:                 Feature(feature_id=4, name='reverse camera'),
    ...:                 Feature(feature_id=9, name='sun roof'),
    ...:             ]
    ...:         )
    ...:     ]
    
In [52]: criteria = critbit.create_criteria(features, 'feature_id')
In [53]: applicants = critbit.create_applicants(vehicles, 'features.feature_id', criteria)
In [54]: critbit.closest(applicants, criteria)

Out[54]: Applicant(key='features.feature_id', value=265, object=Vehicle(vehicle_id=3, make='Mercedes', features=[Feature(feature_id=1, name='satnav'), Feature(feature_id=4, name='reverse camera'), Feature(feature_id=9, name='sun roof')]))
```
