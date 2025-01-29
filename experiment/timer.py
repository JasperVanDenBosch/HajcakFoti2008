from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from experiment.constants import Constants


class Timer:

    ## durations in frames
    dur_display_no_value = 0
    dur_display_value = 0
    inter_trial_interval = 0

    flipRate = 0.0

    def optimizeFlips(self, flipRate: float, consts: Constants) -> None:
        self.flipRate = flipRate
        self.dur_display_no_value = round(consts.dur_display_no_value * flipRate)
        self.dur_display_value = round(consts.dur_display_value * flipRate)
        self.inter_trial_interval = round(consts.inter_trial_interval * flipRate)

    def secsToFlips(self, secs: float) -> int:
        return round(secs*self.flipRate)
    
    def flipsToSecs(self, flips: int) -> float:
        return flips * (1/self.flipRate)
