"""Sense check on pilot data

- do triggers make sense wrt stim code
- what is in .mat file?
- what does neuroscan data look like?
"""
from os.path import expanduser, join
from scipy.io import loadmat

data_dir = expanduser('~/data/eegmanylabs/HajcakFoti2008/biotrialValeryPilot')
sub_01_dir = join(data_dir, 'EEG Many Labs', 'S01_VISIT 1_230608_101455')
fname_mat = 'S01_ERN_originalmethod.mat'
fpath = join(sub_01_dir, fname_mat)
data = loadmat(fpath)
## conclusion: this is EEG data (maybe from the matlab package eeglab)

