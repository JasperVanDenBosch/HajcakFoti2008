from unittest.mock import Mock
from pytest import approx
from statistics import mean


def test_startle_picker_training():
    from experiment.fate import Fate

    fate = Fate()

    trial = Mock()
    trial.phase = 'training'

    startles = []
    reasons = []
    for _ in range(30):
        startle, reason = fate.shouldStartle(trial)
        startles.append(startle)
        reasons.append(reason)
    
    assert set(reasons) == {'training'}
    assert mean(startles) == approx(0.1)

def test_startle_picker_error():
    from experiment.fate import Fate

    fate = Fate()

    trial = Mock()
    trial.phase = 'experiment'
    trial.correct = False

    startles = []
    reasons = []
    for _ in range(5*30):
        startle, reason = fate.shouldStartle(trial)
        startles.append(startle)
        reasons.append(reason)
    
    assert set(reasons) == {'error'}
    assert mean(startles) == approx(0.5, abs=0.01)

def test_startle_picker_correct_predict():
    from experiment.fate import Fate

    fate = Fate()

    preceding_trial = Mock()
    preceding_trial.phase = 'experiment'
    preceding_trial.correct = False

    trial = Mock()
    trial.phase = 'experiment'
    trial.correct = True
    trial.preceding = preceding_trial

    startles = []
    reasons = []
    for _ in range(5*30):
        startle, reason = fate.shouldStartle(trial)
        startles.append(startle)
        reasons.append(reason)
    
    assert set(reasons) == {'correct_predictable'}
    assert mean(startles) == approx(0.5, abs=0.01)

def test_startle_picker_correct_no_prec():
    from experiment.fate import Fate

    fate = Fate()

    trial = Mock()
    trial.phase = 'experiment'
    trial.correct = True
    trial.preceding = None

    startle, reason = fate.shouldStartle(trial)
    
    assert reason == 'correct_unpredictable'
    assert startle == False

def test_startle_picker_correct_unpredict():
    from experiment.fate import Fate

    fate = Fate()

    preceding_trial = Mock()
    preceding_trial.phase = 'experiment'
    preceding_trial.correct = True

    trial = Mock()
    trial.phase = 'experiment'
    trial.correct = True
    trial.preceding = preceding_trial

    startles = []
    reasons = []
    for _ in range(5*30):
        startle, reason = fate.shouldStartle(trial)
        startles.append(startle)
        reasons.append(reason)
    
    assert set(reasons) == {'correct_unpredictable'}
    assert mean(startles) == approx(0.04, abs=0.001)
