close all; clearvars; clc

%This script enables you to interpolate 'bad' channels before doing ICA
rootdir = '/Users/ingmardevries/Library/CloudStorage/GoogleDrive-ingmar.devries@unitn.it/My Drive/Active projects/HajcakFoti2008/';
addpath(genpath(rootdir));
data_path = fullfile(rootdir,'data');

addpath '/Users/ingmardevries/Library/CloudStorage/GoogleDrive-ingmar.devries@unitn.it/My Drive/Active projects/Toolboxes/eeglab2024.0';
eeglab;

% parameters
chan4ICA = 1:28;% only include EEG channels in ICA, not EOG channels or any other recorded channels! Depends on your setup which indices to include.
epochtime = [-0.2 0.8];% time window to epoch
errtrig = 70;% trigger locked to error response
corrtrig = 20;% trigger locked to correct response
% settings for automatic artifact rejection algorithm, see below and
% clean_artifacts.m documentation for more info
BurstCrit = 30;
WinCrit = 0.25;
WinTol = [-inf 10];

%% subject loop
for isub = 1:20
    
    % get folder name for this subject
    subfolder = dir(sprintf('%s%sS%02d*',data_path,filesep,isub));

    % get EEG  file name for this subject
    subfile = dir(sprintf('%s%s%s%s*.cdt',subfolder.folder,filesep,subfolder.name,filesep));

    % load data from previous step
    fn2load = sprintf('%s%sS%02d_newmethod2_interp',subfile.folder,filesep,isub);
    load(fn2load,'EEG');
    
    EEG = pop_select(EEG,'channel',chan4ICA);

    % First reject extremely noisy data segments because they reduce ICA quality
    % Note that bad epochs with smaller noise are either corrected by ICA, or removed in the last script   
    % Note that BurstCriterion [30] and WindowCriterionTolerances [10] are set relatively high now to really only remove the worst noise. If you think more could be
    % removed try reducing these values. If you think too much is being removed, try increasing these values. We don't want to remove blinks yet at
    % this stage because ICA will correct for the influence of blinks without the need for rejecting those segments completely. 
    EEGclean = clean_artifacts(EEG,'ChannelCriterion','off','LineNoiseCriterion','off','BurstCriterion',BurstCrit,'BurstRejection','off','WindowCriterion',WinCrit,'WindowCriterionTolerances',WinTol);
%     vis_artifacts(EEGclean,EEG);% resulting plot will show all data (red) and remaining data (blue) overlaid, but doesn't always work for some reason...
    
    % epoch the data
    EEG = pop_epoch(EEG, {num2str(errtrig), num2str(corrtrig)}, epochtime); 

    %run ICA    
    EEG = pop_runica(EEG, 'chanind', chan4ICA , 'icatype', 'runica', 'extended',1,'interrupt','on');
        
    % store file with ICA weights for next step
    fn2save = sprintf('%s%sS%02d_newmethod3_ICA',subfile.folder,filesep,isub);
    pop_saveset(EEG,'filename',fn2save);
    
end

