import pytest
from unittest.mock import Mock


@pytest.mark.skip()
def test_trial():
    from experiment.trial import Trial

    timer = Mock()
    triggers = Mock()
    engine = Mock()

    engine.displayCardsAndAwaitChoice.return_value = ('left', 0.234)
    trial = Trial(0, 1, 10, -15)
    trial.run(engine, timer, triggers)
    assert trial.choice == 'left'
    assert trial.rt == 0.234
    assert trial.magnitude == 'safe'
    assert trial.result == 10
    assert trial.outcome == 'win'

    engine.displayCardsAndAwaitChoice.return_value = ('right', 0.456)
    trial = Trial(3, 2, 10, -50)
    trial.run(engine, timer, triggers)
    assert trial.magnitude == 'risky'
    assert trial.result == -50
    assert trial.outcome == 'loss'

    engine.displayCardsAndAwaitChoice.return_value = ('left', 0.567)
    trial = Trial(2, 1, -40, 50)
    trial.run(engine, timer, triggers)
    assert trial.magnitude == 'risky'
    assert trial.result == -40
    assert trial.outcome == 'loss'
