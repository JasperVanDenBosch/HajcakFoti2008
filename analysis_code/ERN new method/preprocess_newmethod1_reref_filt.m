close all; clearvars; clc

% This script re-references to the average of both earlobes, applies a 0.1-30Hz bandpass filter,
% epochs the data from -200 to 800 msec, applies regression-based removal of blinks and eye movements
% using the method developed by Gratton et al. (1983), and removes bad trials for individual channels. 
% All following Hajcak & Foti 2008. 
rootdir = '/Users/ingmardevries/Library/CloudStorage/GoogleDrive-ingmar.devries@unitn.it/My Drive/Active projects/HajcakFoti2008/';
addpath(genpath(rootdir));
data_path = fullfile(rootdir,'data');

addpath '/Users/ingmardevries/Library/CloudStorage/GoogleDrive-ingmar.devries@unitn.it/My Drive/Active projects/Toolboxes/eeglab2024.0';
eeglab;

% parameters
chan4reref = 30;% channels to rereference (excl. EMG, EOG and TRIGGER)
chan4filt = 30;% channels to filter (excl. EMG and TRIGGER)
starttrigger = 160;% start of real experimental blocks
padding = 2;% padding before and after experiment in seconds
bpfilt = [0.1 30];% bandpass filter band
linenoise = 50;% typically 50 or 60 Hz

%% subject loop
for isub = 1:20
    
    % get folder name for this subject
    subfolder = dir(sprintf('%s%sS%02d*',data_path,filesep,isub));

    % get EEG  file name for this subject
    subfile = dir(sprintf('%s%s%s%s*.cdt',subfolder.folder,filesep,subfolder.name,filesep));
    
    %reads in EEG data for current subject
    EEG = loadcurry(fullfile(subfile.folder,subfile.name));  

    %re-reference to average of two electrodes placed on left and right
    %mastoid, in this case M1 and M2, but exclude EOG, EMG and TRIGGER, no
    %need to re-reference those. 
    EEG = pop_reref( EEG, {'M1','M2'}, 'exclude', chan4reref+1:EEG.nbchan);

    %apply bandpass filter (0.1-30Hz), only EEG and EOG channels, not EMG
    %or TRIGGER
    EEG= pop_basicfilter( EEG, 1:chan4filt , 'Cutoff', bpfilt, 'Design', 'butter', 'Filter', 'bandpass', 'Order', 2);

    %apply notch filter (although not really necessary after the above
    %bandpass filter up to 30 Hz, but doesn't harm)
    EEG  = pop_basicfilter( EEG,  1:chan4filt , 'Cutoff',  linenoise, 'Design', 'notch', 'Filter', 'PMnotch', 'Order',  180, 'RemoveDC', 'on' );    

    % cut away data before and after experiment, which is often much
    % noisier because subjects still move, and which would make the next
    % clean-up steps driven by this pre/post-experiment data
    starttrigID = find(extractfield(EEG.event,'type') == starttrigger,1);
    startsamp = extractfield(EEG.event(starttrigID),'latency') - padding*EEG.srate;
    endsamp = extractfield(EEG.event(end),'latency') + padding*EEG.srate;
    
    EEG = pop_select(EEG,'point',[startsamp endsamp]);

    % store re-referenced and filtered data for next script
    fn2save = sprintf('%s%sS%02d_newmethod1_filtreref',subfile.folder,filesep,isub);
    save(fn2save,'EEG');
    
end