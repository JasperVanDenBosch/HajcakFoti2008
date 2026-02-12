"""Design-time parameters of the experiment
"""


class Constants(object):

    """These are the durations in ms as reported in the manuscript.
    """

    data_dir = '~/data/YeungSanfey2004/'

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
    img_size = 20 ## width and height in degrees

    eego_start_trigger = 123  # start eego recording
    eego_stop_trigger= 127  # stop eego recording

    ready_msg = dict(
        en="""
Welcome! In this experiment, you will see 5 arrows appear in the middle of the screen.
Some arrows will point left and others right. Your task is to identify the direction
of the MIDDLE arrow. Press the left mouse button if it points left, and the right mouse 
button if it points right. Do this as fast as possible. 

First, a practice block will follow.""",
        fr="""Bienvenue au test de Flanker,
Vous allez voir une série de 5 flèches apparaitre au milieu de l’écran. Certaines sont dirigées vers la gauche et d’autres vers la droite.

Votre objectif est d’identifier le sens de la flèche du MILIEU.

Si la fleche centrale pointe vers la gauche, appuyez sur le bouton de gauche.
Si la fleche centrale pointe vers la droite, appuyez sur le bouton de droite.
Répondez le plus vite possible.

Pour commencer, vous allez réaliser un test d’entraînement.""")
    exp_msg = dict(
        en='Training done.\n\nClick when ready to start main experiment...',
        fr='Entrainement terminé.\n\nCliquer quand vous êtes prêt à commencer le test principal')
    thank_msg = dict(
        en='Done! Thank you.',
        fr='Test terminé ! Merci.')
    low_acc_msg = dict(
        en="Please try to be more accurate",
        fr='Essayez d’être plus précis')
    high_acc_msg = dict(
        en="Please try to respond faster",
        fr='Essayez de répondre plus rapidement')
    mid_acc_msg = dict(
        en="You’re doing a great job",
        fr='Vous faites du bon travail')
