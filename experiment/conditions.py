"""Define some types related to the design
"""
from __future__ import annotations
from typing import Literal
Compatibility = Literal['compatible', 'incompatible']
Direction = Literal['left', 'right']
Phase = Literal['training', 'experiment']
StartleCondition = Literal[
    'training',
    'error',
    'correct_predictable',
    'correct_unpredictable',
    'no_response',
]
