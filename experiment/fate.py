"""
dekiru toki ni dekiru koto
"""
from __future__ import annotations
from typing import TYPE_CHECKING, Tuple, List
from random import shuffle
from math import ceil
if TYPE_CHECKING:
    from experiment.conditions import StartleCondition
    from experiment.trial import Trial


class Fate:
    
    def __init__(self, n=1000):
        self.future = {
            'training': self.decide(0.1, 10, n),
            'error': self.decide(0.5, 4, n),
            'correct_predictable': self.decide(0.5, 4, n),
            'correct_unpredictable': self.decide(0.04, 25, n),
        }

    def decide(self, frac: float, span: int, n: int) -> List[bool]:
        reps = ceil(n/span)
        decisions = []
        for _ in range(reps):
            segment = [False]*span
            for i in range(int(frac*span)):
                segment[i] = True
            shuffle(segment)
            decisions += segment
        return decisions

    def shouldStartle(self, trial: Trial) -> Tuple[bool, StartleCondition]:
        if trial.phase == 'training':
            reason = 'training'
        elif not trial.correct:
            reason = 'error'
        elif not trial.preceding_correct:
            reason = 'correct_predictable'
        else:
            reason = 'correct_unpredictable'
        decision = self.future[reason].pop(0)
        return decision, reason
