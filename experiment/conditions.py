"""Define some types related to the design
"""
from __future__ import annotations
from typing import Union, Literal
CardPos = Union[Literal['left'], Literal['right']]
Magnitude = Union[Literal['safe'], Literal['risky']]
Outcome = Union[Literal['win'], Literal['loss']]
Phase = Union[Literal['options'], Literal['feedback_chosen'], Literal['feedback_alternative']]


def alternative(choice: CardPos) -> CardPos:
    """Invert left vs right

    Args:
        choice (CardPos): 'left' or 'right'

    Returns:
        CardPos: the opposite choice
    """
    return 'left' if choice == 'right' else 'right'
