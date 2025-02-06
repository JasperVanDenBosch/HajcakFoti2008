from __future__ import annotations
from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from experiment.conditions import Phase, Direction, Compatibility, StartleCondition

class Triggers:

    def forFlanker(self, phase: Phase, compatibility: Compatibility, direction: Direction) -> int:
        offset = 11 if phase == 'training' else 15
        return offset + 2*int(compatibility=='incompatible') + int(direction=='right')

    def forResponse(self, phase: Phase, correct: Optional[bool]) -> int:
        offset = 20 if phase == 'training' else 26
        if correct is None:
            return offset + 2
        elif correct is True:
            return offset + 0
        else:
            return offset + 1

    def forStartle(self, condition: StartleCondition) -> int:
        match condition:
            case 'training': return 4
            case 'correct_predictable': return 5
            case 'correct_unpredictable': return 6
            case 'error': return 7
            case _: raise ValueError('unknown StartleCondition')
