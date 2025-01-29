"""Design-time parameters of the experiment
"""


class Constants(object):

    """These are the durations in ms as reported in the manuscript.
    """

    block_trials = 32
    total_trials = 480

    valid_keys = ['f', 'j']

    dur_display_no_value = 0.5 ## highlight choice (500ms)
    dur_display_value = 1.0 ## display value (1000ms)
    inter_trial_interval = 0.5 

    # size of stimuli in degrees of visual angle
    instruction_text_size = 1
    value_text_size = 1
    value_font = 'monospace'
    card_size = 4.0
    card_offset = 5.0
    card_border_thickness = 20 # pixels
    fix_size = 0.2
    ## red, green, blue, purple
    colors_rgb1 = [
        (0.486, 0.086, 0.051),
        (0.169, 0.373, 0.11),
        (0.0, 0.0, 0.482),
        (0.42, 0.071, 0.443),
    ]
    colors = [
        (124, 22, 13),
        (43, 95, 28),
        (0, 0, 123),
        (107, 18, 113 ),
    ]

    instruction_msg = """Welcome to the YeungSanfey2004 experiment
    
    In every trial you will see two colored cards displayed. 
    The cards are selected from four decks; blue, green, purple and red. 
    Your task is to select one of the two cards, 
    by pressing F for the left card, and J for the right card.
    After selecting a card, you will see how much you won or lost, 
    and how much you would have won or lost if you had chosen the other card. 
    Use any strategy you want to help you maximize your points total.

    There will be 15 blocks of 32 trials each. 
    At the end of each block you will see an update of your winnings up to that point.
    You will keep whatever money you won playing the game, in addition to your course credits.
    """
    ready_msg = 'Ready? \n\n Press [space] to start'
    block_msg = 'Your total winnings are £{:.02f}.\n\nTake a break.\n\nPress [space] to start the next block'
    thank_msg = 'Done! Thank you.'

