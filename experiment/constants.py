"""Design-time parameters of the experiment
"""


class Constants(object):

    """These are the durations in ms as reported in the manuscript.
    """

    ## librayr ptb
    ## audio latency priority = 4

    block_trials = 30
    total_trials = 8*30

    dur_stimulus = 200 ## 
    dur_resp = 1800 ## additional response window
    dur_delay_startle = 300 ## startle delay
    inter_trial_interval_min = 500
    inter_trial_interval_jitter = 500

    # size of stimuli in degrees of visual angle
    instruction_text_size = 1
    fix_size = 0.2

    """ conditions.csv
    stimulus,condition,direction,correct_resp,event_marker,event_hex
    stimuli/All_left.jpg,compatible,left,0,101::CL,3D
    stimuli/All_Right.jpg,compatible,right,1,102::CR,3E
    stimuli/Center_Left.jpg,incompatible,left,0,103::IL,3F
    stimuli/Center_Right.jpg,incompatible,right,1,104::IR,40
    """

    """ blocks xlsx
    blockOrder	block1_nReps	block2_nReps	block3_nReps
    A	1	0	0
    B	0	1	0
    C	0	0	1
    """
    """
    'Ready for the real thing?\n\n\n\n\nClick anywhere to proceed...'
    'Click to continue...'
    'Fin.'
    'This is just a test.\n\n\n\n\nClick anywhere to proceed...'
    'stimuli/startle2_reencoded.wav'
    """

    ready_msg = 'This is just a test.\n\nClick anywhere to proceed...'
    thank_msg = 'Done! Thank you.'

    '''
    If performance was 75% correct or lower, the message
    ‘‘Please try to be more accurate’’ was displayed; performance
    above 90% correct was followed by ‘‘Please try to respond
    faster’’; if performance was between these levels, the message
    ‘‘You’re doing a great job’’ was displayed.
    '''

    low_acc_msg = "Please try to be more accurate"
    high_acc_msg = "Please try to respond faster"
    mid_acc_msg = "You’re doing a great job"
