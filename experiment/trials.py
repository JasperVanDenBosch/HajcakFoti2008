from __future__ import annotations
from typing import List
from experiment.trial import Trial
from random import shuffle
from typing import TYPE_CHECKING
from math import ceil
if TYPE_CHECKING:
    from experiment.conditions import Phase


def generate_trials(phase: Phase) -> List[Trial]:
    n = 30 if phase == 'training' else 240
    stimuli = (
        dict(compatibility='compatible', direction='left'),
        dict(compatibility='compatible', direction='right'),
        dict(compatibility='incompatible', direction='left'),
        dict(compatibility='incompatible', direction='right')
    )
    N_STIMS = len(stimuli)
    SPAN = 4
    REPS = ceil(n/(SPAN*N_STIMS))
    condition_vector = []
    for _ in range(REPS):
        segment = list(range(N_STIMS))*SPAN
        shuffle(segment)
        condition_vector += segment
    condition_vector = condition_vector[:n]

    trials = []
    preceding = None
    for c in condition_vector:
        trials.append(
            Trial(
                phase=phase,
                compatible=stimuli[c]['compatibility'],
                direction=stimuli[c]['direction'],
                preceding=preceding,
                correct=None,
                rt=None,
                startles=None,
                startleReason=None
            )
        )
        preceding = trials[-1]

    return trials
