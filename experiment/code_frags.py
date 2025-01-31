"""Code blocks from builder
"""

startle = sound.Sound(value='stimuli/startle2_reencoded.wav',
                                            volume=1.0,
                                            hamming=False,
                                            name='startle',
                                            autoLog=False)


## begin routine

if startled == True :
    startle.play()
    #nextFlip = win.getFutureFlipTime(clock='ptb')
    #startle.play(when=nextFlip)  # sync with screen refresh



############### code lsl

try :
    import pylsl as LSL
except :
    print(f"LSL not available.")


if expInfo['EEG connected?'] == 'y' :
    stream = LSL.StreamInfo('psychopy2eego','Markers',1,0,'string',expInfo['Experiment ID'])
    outlet = LSL.StreamOutlet(stream)
    print(f"LSL active... \
            \n{outlet}\
            \n{stream}")
    outlet.push_sample([str(123)])  # start eego recording


if expInfo['EEG connected?'] == 'y' :
    LSL_msg = [str(event_marker)]
    outlet.push_sample(LSL_msg)
    print(f"{LSL_msg}")

if expInfo['EEG connected?'] == 'y' :
    outlet.push_sample([str(accuracy)])  # mark accuracy of trial
    print([str(accuracy)])
    if startled :
        outlet.push_sample([str("5::Startled!")])

if expInfo['EEG connected?'] == 'y' :
    outlet.push_sample([str(127)])  # stop eego recording



## begin routine
block1_nReps = blockOrders[expInfo['blockOrder']]['block1'][blocks.thisRepN+1]
block2_nReps = blockOrders[expInfo['blockOrder']]['block2'][blocks.thisRepN+1]
block3_nReps = blockOrders[expInfo['blockOrder']]['block3'][blocks.thisRepN+1]

## begin exp

blockOrder = expInfo['blockOrder']

blockOrder_A = {'block1':{1:True,2:False,3:False},
                'block2':{1:False,2:True,3:False},
                    'block3':{1:False,2:False,3:True}}

blockOrder_B = {'block1':{1:True,2:False,3:False},
                'block2':{1:False,2:False,3:True},
                    'block3':{1:False,2:True,3:False}}

blockOrder_C = {'block1':{1:False,2:True,3:False},
                'block2':{1:2,2:False,3:False},
                    'block3':{1:False,2:False,3:True}}

blockOrder_D = {'block1':{1:False,2:False,3:True},
                'block2':{1:True,2:False,3:False},
                    'block3':{1:False,2:True,3:False}}

blockOrder_E = {'block1':{1:False,2:True,3:False},
                'block2':{1:False,2:False,3:True},
                    'block3':{1:True,2:False,3:False}}

blockOrder_F = {'block1':{1:False,2:False,3:True},
                'block2':{1:False,2:True,3:True},
                    'block3':{1:True,2:False,3:False}}     

blockOrders = {'A':blockOrder_A,'B':blockOrder_B,'C':blockOrder_C,
                'D':blockOrder_D,'E':blockOrder_E,'F':blockOrder_F}