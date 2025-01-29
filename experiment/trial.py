from __future__ import annotations
from typing import TYPE_CHECKING, Optional
from dataclasses import dataclass
from experiment.conditions import alternative
if TYPE_CHECKING:
    from experiment.engine import PsychopyEngine
    from experiment.timer import Timer
    from experiment.triggers import Triggers
    from experiment.conditions import CardPos, Magnitude, Outcome


@dataclass()
class Trial:

    card_left: int
    card_right: int
    value_left: int
    value_right: int
    
    ## determined after participant choice
    outcome: Outcome
    choice: Optional[CardPos]
    rt: Optional[float]
    magnitude: Optional[Magnitude]
    result: Optional[float]

    def __init__(self, card_left: int, card_right: int, value_left: int, value_right: int):
        self.card_left = card_left
        self.card_right = card_right
        self.value_left = value_left
        self.value_right = value_right
    
    def registerChoice(self):
        value = self.value_left if self.choice == 'left' else self.value_right
        self.magnitude = 'risky' if abs(value) > 20 else 'safe'
        self.result = self.valueChosen()
        self.outcome = 'win' if value > 0 else 'loss'
    
    def valueChosen(self) -> int:
        return self.value_left if self.choice == 'left' else self.value_right

    def valueAlternative(self) -> int:
        return self.value_left if self.choice == 'right' else self.value_right

    def run(self, engine: PsychopyEngine, timer: Timer, triggers: Triggers):
        """Present this trial

        Args:
            engine (PsychopyEngine): This is a wrapper for the experiment software
        """
        engine.displayFixCross(timer.inter_trial_interval)

        (self.choice, self.rt) = engine.displayCardsAndAwaitChoice(
            self.card_left,
            self.card_right,
            triggers.get_number('options')
        )

        ## update Trial properties 
        self.registerChoice()

        engine.displayCards(
            self.card_left,
            self.card_right,
            timer.dur_display_no_value,
            triggerNr=0,
            highlight=self.choice,
        )

        engine.displayCards(
            self.card_left,
            self.card_right,
            timer.dur_display_value,
            triggers.get_number('feedback_chosen', self.magnitude, self.outcome),
            highlight=self.choice,
            showValue=self.choice,
            value=self.valueChosen(),
        )

        engine.displayCards(
            self.card_left,
            self.card_right,
            timer.dur_display_no_value,
            triggerNr=0,
            highlight=self.choice,
        )

        engine.displayCards(
            self.card_left,
            self.card_right,
            timer.dur_display_value,
            triggers.get_number('feedback_alternative', self.magnitude, self.outcome),
            highlight=self.choice,
            showValue=alternative(self.choice),
            value=self.valueAlternative(),
        )

        engine.flush()

