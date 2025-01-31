from __future__ import annotations
from typing import TYPE_CHECKING, Optional
from dataclasses import dataclass
if TYPE_CHECKING:
    from experiment.engine import PsychopyEngine
    from experiment.constants import Constants
    from experiment.fate import Fate
    from experiment.conditions import Phase, Direction, Compatibility, StartleCondition


@dataclass()
class Trial:

    phase: Phase
    direction: Direction
    compatible: Compatibility
    preceding: Optional[Trial]
    iti: int
    
    ## determined after participant choice
    correct: Optional[bool]
    rt: Optional[float]
    startles: Optional[bool]
    startleReason: Optional[StartleCondition]

    def run(self, engine: PsychopyEngine, fate: Fate, const: Constants):
        """Present this trial

        Args:
            engine (PsychopyEngine): This is a wrapper for the experiment software
        """
        engine.displayFixCross(self.iti)

        (self.correct, self.rt) = engine.displayFlankersAndAwaitResponse(
            self.phase,
            self.direction,
            self.compatible,
            const.dur_stimulus,
            const.dur_resp
        )
        
        self.startles, self.startleReason = fate.shouldStartle(self)

        if self.startles:
            engine.delayAndStartle(self.startleReason, const.dur_delay_startle)

        engine.flush()
