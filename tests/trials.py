"""Unit tests for trial generation distribution

See also original.vb for original (Visual Basic) code.

15 blocks of 32 trials each.

Four colors of cards were used: red, green, blue, and purple. Two of the
colors were always associated with large outcomes, which were wins or
losses of 32– 40¢ (these colors were referred to as large decks), and two
were always associated with small outcomes, which were wins or losses of
6–11¢ (these colors were referred to as small decks). The assignment of
colors to reward magnitudes was varied across participants. 

The colors presented on any given trial were randomized with the constraint that
each possible pairing occurred with equal frequency. Pairings of identical
colored cards were allowed. 

Thus, on half of all trials, participants chose
between one large card and one small card. The other half of trials in-
volved selecting between two small cards or between two large cards.


The outcome of each trial was determined pseudorandomly with the
constraint that each participant experienced equal numbers of small wins
and small losses and equal numbers of large wins and large losses. The
ratio of small to large outcomes depended on the participants’ choices
and hence was not controlled. 

Although colors were consistently associ-
ated with either small or large outcomes for each participant, there re-
mained some degree of uncertainty about the outcome of each trial,
 because small outcomes varied between 6 and
11¢ and large outcomes varied between 32 and
40¢. Within these ranges, the frequency of pos-
sible outcomes was weighted such that the
mean expected value of each trial was 1¢ for
both small and large choices.

There were 480 trials total, divided into
15 equal blocks. Thus, participants won $4.80
on average.
"""
from unittest.mock import Mock
import random
import pytest

@pytest.mark.skip()
def test_trials_basics():
    from experiment.trials import generate_trials
    trials = generate_trials()
    assert len(trials) == 480

@pytest.mark.skip()
def test_trials_combinations_equiprobable():
    ## each possible (color) pairing occurred with equal frequency
    from experiment.trials import generate_trials
    trials = generate_trials()
    comb_counts = dict()
    for trial in trials:
        comb = tuple(sorted([trial.card_left, trial.card_right]))
        if comb in comb_counts:
            comb_counts[comb] += 1
        else:
            comb_counts[comb] = 1
    assert len(comb_counts) == 10 ## total unique combinations
    assert set(comb_counts.values()) == {48} ## combination counts

@pytest.mark.skip()
def test_outcome_equiprobable_per_condition():
    ## equal numbers of small wins and small losses
    ## equal numbers of large wins and large losses
    ## (i.e. win vs loss equal for each category)
    from experiment.trials import generate_trials
    RISKY_DECKS = [0, 1]

    def favourRisky(card1, card2, *args):
        # participant strategy to pick risky card 80%
        left_chance = 0.8 if card1 in RISKY_DECKS else 0.2
        right_chance = 0.8 if card2 in RISKY_DECKS else 0.2
        total_chance = left_chance + right_chance
        if random.random() < (left_chance / total_chance):
            return ('left', 0.123)
        else:
            return ('right', 0.123)

    timer = Mock()
    triggers = Mock()
    engine = Mock()
    engine.displayCardsAndAwaitChoice.side_effect = favourRisky

    trials = generate_trials()

    outcome_counts = dict(risky_win=0, risky_loss=0, safe_win=0, safe_loss=0)
    for trial in trials:
        trial.run(engine, timer, triggers)
        
        outcome_counts[f'{trial.magnitude}_{trial.outcome}'] += 1

    assert outcome_counts['risky_win'] == outcome_counts['risky_loss']
    assert outcome_counts['safe_win'] == outcome_counts['safe_loss']

@pytest.mark.skip()
def test_winnings_equal_per_condition():
    ## the mean expected value of each trial was 1¢ for small choices
    ## the mean expected value of each trial was 1¢ for large choices.
    ## (win vs loss not associated with color)
    from experiment.trials import generate_trials
    RISKY_DECKS = [0, 1]

    def favourRisky(card1, card2, *args):
        # participant strategy to pick risky card 80%
        left_chance = 0.8 if card1 in RISKY_DECKS else 0.2
        right_chance = 0.8 if card2 in RISKY_DECKS else 0.2
        total_chance = left_chance + right_chance
        if random.random() < (left_chance / total_chance):
            return ('left', 0.123)
        else:
            return ('right', 0.123)

    timer = Mock()
    triggers = Mock()
    engine = Mock()
    engine.displayCardsAndAwaitChoice.side_effect = favourRisky

    trials = generate_trials()

    outcome_values = {'risky':[], 'safe':[]}
    for trial in trials:
        trial.run(engine, timer, triggers)
        assert trial.magnitude is not None
        outcome_values[trial.magnitude].append(trial.result)

    ## shouldnt sum outcomes but "ecpected"; mean of all safe values

    assert sum(outcome_values['risky']) == len(outcome_values['risky'])
    assert sum(outcome_values['safe']) == len(outcome_values['safe'])
