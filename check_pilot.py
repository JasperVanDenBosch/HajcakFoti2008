"""Sense check on pilot data

- do triggers make sense wrt stim code
- what is in .mat file?
- what does neuroscan data look like?
"""
from os.path import expanduser, join
from scipy.io import loadmat
import mne

data_dir = expanduser('~/data/eegmanylabs/HajcakFoti2008/biotrialValeryPilot')
sub_01_dir = join(data_dir, 'EEG Many Labs', 'S01_VISIT 1_230608_101455')
fname_mat = 'S01_ERN_originalmethod.mat'
fname_cdt = 'S01_VISIT 1.cdt'
fpath = join(sub_01_dir, fname_mat)
data = loadmat(fpath)
## conclusion: this is EEG data (maybe from the matlab package eeglab)


"""
.clog: text file with output log

.cdb: The Database structure allows for the easy organization and access to all files (data, parameter, results, configuration) needed for CURRY operation

.dpa: Parameters and sensor locations are written to the accompanying .dpa file.

.ceo: events / annotations
"""
raw = mne.io.read_raw_curry(join(sub_01_dir, fname_cdt))

events, event_dict = mne.events_from_annotations(raw)

"""
In [12]: numpy.unique(events[:, 2])
Out[12]: array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

In [13]: event_dict
Out[13]:
{np.str_('10'): 1,
 np.str_('140'): 2,
 np.str_('160'): 3,
 np.str_('170'): 4,
 np.str_('175'): 5,
 np.str_('180'): 6,
 np.str_('182'): 7,
 np.str_('185'): 8,
 np.str_('20'): 9,
 np.str_('50'): 10,
 np.str_('70'): 11}
"""

