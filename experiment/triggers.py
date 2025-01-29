from __future__ import annotations
from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from experiment.conditions import CardPos, Phase, Magnitude, Outcome
OFFSET = True


class Triggers:


    """Original:
        Left / SAFE &H40 --> 64
        Left / Risky &H50 --> 80
        right / safe -> &H48  --> 72
        right / risky -> &H58  -> 88
    """

    def get_number(self, phase: Phase, magnitude: Optional[Magnitude]=None, outcome: Optional[Outcome]=None) -> int:
        if phase == 'options':
            return 1
        else:
            assert magnitude
            assert outcome
            mag_offset = dict(safe=0, risky=1)[magnitude]
            out_offset = dict(loss=0, win=1)[outcome]
            if phase == 'feedback_chosen':
                return 10 + out_offset*2 + mag_offset
            elif phase == 'feedback_alternative':
                return 20 + out_offset*2 + mag_offset
            else:
                raise ValueError('[Triggers.get_number()] Unknown Phase value')
        return 0
