"""
dekiru toki ni dekiru koto
"""
from __future__ import annotations
from typing import TYPE_CHECKING, Tuple
if TYPE_CHECKING:
    from experiment.conditions import StartleCondition
    from experiment.trial import Trial


class Fate:

    def shouldStartle(self, trial: Trial) -> Tuple[bool, StartleCondition]:
        return False, 'training'