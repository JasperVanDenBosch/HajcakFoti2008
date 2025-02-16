"""Define some types related to the design
"""
from __future__ import annotations
from typing import Union, Literal
Compatibility = Union[Literal['compatible'], Literal['incompatible']]
Direction = Union[Literal['left'], Literal['right']]
Phase = Union[Literal['training'], Literal['experiment']]
StartleCondition = Union[Literal['training'], Literal['error'], Literal['correct_predictable'], Literal['correct_unpredictable']]
