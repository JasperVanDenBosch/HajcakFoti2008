from __future__ import annotations
from typing import TYPE_CHECKING, List
from experiment.trial import Trial
from random import shuffle
from itertools import combinations_with_replacement
from copy import copy


def generate_trials() -> List[Trial]:
    risky_decks = [0, 1] ## TODO

    # small outcomes varied between 6 and 11¢ and 
    safe_dist = [
        -10, -9, -8, -8, -7, -7, -7, -7, -6, -6, 
        7, 8, 9, 9, 10, 10, 10, 10, 11, 11]
    # large outcomes varied between 32 and 40¢
    risky_dist = [
        -40, -38, -36, -36, -34, -34, -34, -34, -32, -32, 
        32, 34, 36, 36, 38, 38, 38, 38, 40, 40
    ]
    decks = [0, 1, 2, 3]
    card_combs_fwd = list(combinations_with_replacement(decks, 2)) ## because they say risky vs safe 50%
    card_combs_rew = list(combinations_with_replacement(reversed(decks), 2)) ## because they say risky vs safe 50%

    #24x20 values
    recipes = []
    for _ in range(24):

        risky_vals = copy(risky_dist)
        safe_vals = copy(safe_dist)
        shuffle(risky_vals)
        shuffle(safe_vals)

        card_combs = card_combs_fwd + card_combs_rew
        shuffle(card_combs) ## shuffle order of combinations for matching with values
        
        subset_recipes = []
        for (card1, card2) in card_combs:
            subset_recipes.append(dict(
                card_left=card1,
                card_right=card2,
                value_left = risky_vals.pop() if card1 in risky_decks else safe_vals.pop(),
                value_right = risky_vals.pop() if card2 in risky_decks else safe_vals.pop(),
            ))
        shuffle(subset_recipes) ## now also shuffle value order
        recipes += subset_recipes

        assert len(risky_vals) == 0
        assert len(safe_vals) == 0

    return [Trial(**recipe) for recipe in recipes]
