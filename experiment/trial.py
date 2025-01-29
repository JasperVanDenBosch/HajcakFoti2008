from __future__ import annotations
from typing import TYPE_CHECKING, Optional
from dataclasses import dataclass
if TYPE_CHECKING:
    from experiment.engine import PsychopyEngine
    from experiment.timer import Timer
    from experiment.triggers import Triggers
    from experiment.conditions import Phase, Direction, Compatibility


@dataclass()
class Trial:

    phase: Phase
    direction: Direction
    compatible: Compatibility 
    
    ## determined after participant choice
    correct: Optional[bool]
    rt: Optional[float]

    def run(self, engine: PsychopyEngine, timer: Timer, triggers: Triggers):
        """Present this trial

        Args:
            engine (PsychopyEngine): This is a wrapper for the experiment software
        """
        engine.displayFixCross(timer.inter_trial_interval)

        ## flankers
        (self.choice, self.rt) = engine.displayCardsAndAwaitChoice(
            self.card_left,
            self.card_right,
            triggers.get_number('options')
        )

        ## wait for response 
        self.registerChoice()

        ## startle wait period (does this happen on non-startle trials?)

        ## startle (break on non-startle trials?)



        engine.flush()

