"""Test that the Triggers class provides the correct trigger numbers

## Design


should left/right be in triggers? because of laterality?
"""
import pytest

def test_triggers_flankers():
    from experiment.triggers import Triggers
    triggers = Triggers()

    assert triggers.forFlanker(phase='training', compatibility='compatible', direction='left') == 11
    assert triggers.forFlanker(phase='training', compatibility='compatible', direction='right') == 12
    assert triggers.forFlanker(phase='training', compatibility='incompatible', direction='left') == 13
    assert triggers.forFlanker(phase='training', compatibility='incompatible', direction='right') == 14
    
    assert triggers.forFlanker(phase='experiment', compatibility='compatible', direction='left') == 15
    assert triggers.forFlanker(phase='experiment', compatibility='compatible', direction='right') == 16
    assert triggers.forFlanker(phase='experiment', compatibility='incompatible', direction='left') == 17
    assert triggers.forFlanker(phase='experiment', compatibility='incompatible', direction='right') == 18


def test_triggers_response():
    from experiment.triggers import Triggers
    triggers = Triggers()

    assert triggers.forResponse(phase='training', correct=True) == 20
    assert triggers.forResponse(phase='training', correct=False) == 21
    assert triggers.forResponse(phase='training', correct=None) == 22

    assert triggers.forResponse(phase='experiment', correct=True) == 26
    assert triggers.forResponse(phase='experiment', correct=False) == 27
    assert triggers.forResponse(phase='experiment', correct=None) == 28

def test_triggers_startle():
    from experiment.triggers import Triggers
    triggers = Triggers()

    assert triggers.forStartle(condition='training') == 4
    assert triggers.forStartle(condition='correct_predictable') == 5
    assert triggers.forStartle(condition='correct_unpredictable') == 6
    assert triggers.forStartle(condition='error') == 7
