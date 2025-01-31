"""Code blocks from builder
"""


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


