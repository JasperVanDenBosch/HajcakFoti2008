"""Design-time parameters of the experiment
"""


class Constants(object):

    """These are the durations in ms as reported in the manuscript.
    """

    ## librayr ptb
    ## audio latency priority = 4

    block_trials = 30
    total_trials = 2*30 #8*30

    dur_stimulus = 200 ## 
    dur_resp = 1800 ## additional response window
    dur_delay_startle = 300 ## startle delay
    inter_trial_interval_min = 500
    inter_trial_interval_jitter = 500

    # size of stimuli in degrees of visual angle
    instruction_text_size = 1
    fix_size = 0.2
    img_size = 10 ## width and height in degrees

    eego_start_trigger = 123  # start eego recording
    eego_stop_trigger= 127  # stop eego recording

    ready_msg = 'Training starts.\n\nClick to proceed...'
    exp_msg = 'Training done.\n\nClick when ready to start main experiment...'
    thank_msg = 'Done! Thank you.'
    low_acc_msg = "Please try to be more accurate"
    high_acc_msg = "Please try to respond faster"
    mid_acc_msg = "You’re doing a great job"
