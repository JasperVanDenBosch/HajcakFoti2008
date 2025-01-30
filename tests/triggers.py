"""Test that the Triggers class provides the correct trigger numbers

## Design


should left/right be in triggers? because of laterality?
"""
import pytest

@pytest.mark.skip()
def test_triggers():
    from experiment.triggers import Triggers
    triggers = Triggers()

    ## first phase; magnitude unknown, outcome irrelevant
    assert triggers.get_number(phase='options') == 1

    ## second phase
    assert triggers.get_number(phase='feedback_chosen', outcome='loss', magnitude='safe') == 10
    assert triggers.get_number(phase='feedback_chosen', outcome='loss', magnitude='risky') == 11
    assert triggers.get_number(phase='feedback_chosen', outcome='win', magnitude='safe') == 12
    assert triggers.get_number(phase='feedback_chosen', outcome='win', magnitude='risky') == 13

    ## third phase
    assert triggers.get_number(phase='feedback_alternative', outcome='loss', magnitude='safe') == 20
    assert triggers.get_number(phase='feedback_alternative', outcome='loss', magnitude='risky') == 21
    assert triggers.get_number(phase='feedback_alternative', outcome='win', magnitude='safe') == 22
    assert triggers.get_number(phase='feedback_alternative', outcome='win', magnitude='risky') == 23
