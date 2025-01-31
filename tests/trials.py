"""Unit tests for trial generation distribution
"""

def test_trials_basics():
    from experiment.trials import generate_trials
    trials = generate_trials('experiment')
    assert len(trials) == 240
    assert set([t.phase for t in trials]) == {'experiment'}


def test_trials_training():
    from experiment.trials import generate_trials
    trials = generate_trials('training')
    assert len(trials) == 30
    assert set([t.phase for t in trials]) == {'training'}


def test_trials_flankers_equiprobable():
    ## each possible condition occurred with equal frequency
    from experiment.trials import generate_trials
    trials = generate_trials('experiment')
    comb_counts = dict()
    for trial in trials:
        comb = tuple(sorted([trial.compatible, trial.direction]))
        if comb in comb_counts:
            comb_counts[comb] += 1
        else:
            comb_counts[comb] = 1
    assert len(comb_counts) == 4 ## total unique combinations
    ## each combination occurs exactly 60 times
    assert set(comb_counts.values()) == {60} ## combination counts


def test_trials_preceding():
    from experiment.trials import generate_trials
    trials = generate_trials('experiment')

    assert trials[0].preceding is None
    assert trials[1].preceding is trials[0]
    assert trials[2].preceding is trials[1]
