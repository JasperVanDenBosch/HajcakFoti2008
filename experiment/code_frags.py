"""Code blocks from builder
"""



### code_trial (being exp)
showBreakMessage = False
blockLength = 8
stimulusDuration = 0.2
totalTrials_count = 0
totalTrials = 240
accuracyTotal = 0
runningAccuracy = 0
accuracy_lastTrial = 0
blockof30N = 0
startled_trials0 = []
startled_trials1 = []
startled_trials4 = []
startle = sound.Sound(value='stimuli/startle2_reencoded.wav',
                                            volume=1.0,
                                            hamming=False,
                                            name='startle',
                                            autoLog=False)


## begin routine

trialNofcurrentLoop = currentLoop.thisN + 1
totalTrials_count += 1
mouse_block.clickReset()
iTi_time = random.randrange(500,1000,50) / 1000

if totalTrials_count > 1 :
    accuracy_lastTrial = accuracy

if "practice" in currentLoop.name :
    trialType = 'p'
else :
    trialType = 'e'

if totalTrials_count % blockLength == 0 \
    and trialType == 'e' :
        blockof30N += 1
        showBreakMessage = True
elif totalTrials_count % blockLength == 0 \
    and trialType == 'p' :
        print("practice_trials finished...")
        practice_trials.finished = True
else :
        showBreakMessage = False

## end routine

buttons,times = mouse_block.getPressed(getTime=True)
if buttons[-1] == correct_resp :
    accuracy = 1 
else:
    accuracy = 0
accuracyTotal += accuracy
runningAccuracy = (accuracyTotal / totalTrials_count) * 100

#random.sample([1,0],1)[0]
if accuracy_lastTrial == 0 and random.randrange(0,100,1) >= 50 and len(startled_trials1) < (totalTrials/100*50) :
    startled = True
    startled_trials1.append(totalTrials_count)
elif accuracy_lastTrial == 0 and random.randrange(0,100,1) >= 50 and len(startled_trials0) < (totalTrials/100*50):
    startled = True
    startled_trials0.append(totalTrials_count)
elif random.randrange(0,100,1) >= 50 and len(startled_trials4) < (totalTrials/100*4):
    startled = True
    startled_trials4.append(totalTrials_count)
else :
    startled = False

if startled == True :
    startle.play()
    #nextFlip = win.getFutureFlipTime(clock='ptb')
    #startle.play(when=nextFlip)  # sync with screen refresh

thisExp.addData('trialType',trialType)
thisExp.addData('accuracy',accuracy)
thisExp.addData('rt',mouse_block.time[-1])
thisExp.addData('trialN',trialNofcurrentLoop)
thisExp.addData('totalTrials',totalTrials_count)
thisExp.addData('accuracyTotal',accuracyTotal)
thisExp.addData('runningAccuracy',runningAccuracy)


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