%This script automatically selects bad components using SASICA
close all; clearvars; clc

rootdir = '/Users/ingmardevries/Library/CloudStorage/GoogleDrive-ingmar.devries@unitn.it/My Drive/Active projects/HajcakFoti2008/';
data_path = fullfile(rootdir,'data');
addpath(genpath(rootdir));

addpath '/Users/ingmardevries/Library/CloudStorage/GoogleDrive-ingmar.devries@unitn.it/My Drive/Active projects/Toolboxes/eeglab2024.0';
eeglab;

% loop over subjects
for isub = 1:20

    % get folder name for this subject
    subfolder = dir(sprintf('%s%sS%02d*',data_path,filesep,isub));
    % get EEG file name for this subject
    subfile = dir(sprintf('%s%s%s%s*.cdt',subfolder.folder,filesep,subfolder.name,filesep));

    % load data from previous step
    fn2load = sprintf('%s%sS%02d_newmethod3_ICA',subfile.folder,filesep,isub);
    EEG = pop_loadset([fn2load '.set']);

    % Automatic bad component detection using SASICA, with the following
    % settings with default parameters:
    % - Autocorrelation, Focal Components, Signal to noise Ratio, ADJUST
    % Selection.
    % 
    % Either automatically accept the SASICA components, by setting
    % 'opts_noplot' to 1 in the below call to eeg_SASICA, or set to 0 to
    % visually inspect the SASICA selection (and (de)select SASICA
    % components if desired) before accepting. When deciding, it
    % additionally can help to look at the component time series themselves:
%     pop_eegplot( EEG, 0, 1, 1); %plot components

    % run SASICA
    EEG = eeg_SASICA(EEG,'MARA_enable',0,'FASTER_enable',0,'FASTER_blinkchanname','No channel','ADJUST_enable',1,'chancorr_enable',...
        0,'chancorr_channames','No channel','chancorr_corthresh','auto 4','EOGcorr_enable',0,'EOGcorr_Heogchannames','No channel',...
        'EOGcorr_corthreshH','auto 4','EOGcorr_Veogchannames','No channel','EOGcorr_corthreshV','auto 4','resvar_enable',0,'resvar_thresh',15,...
        'SNR_enable',1,'SNR_snrcut',1,'SNR_snrBL',[-Inf 0] ,'SNR_snrPOI',[0 Inf] ,'trialfoc_enable',0,'trialfoc_focaltrialout','auto',...
        'focalcomp_enable',1,'focalcomp_focalICAout','auto','autocorr_enable',1,'autocorr_autocorrint',20,'autocorr_dropautocorr','auto',...
        'opts_noplot',1,'opts_nocompute',0,'opts_FontSize',14);

    % extract automatically selected components
    comp2rej = find(EEG.reject.gcompreject == 1);

    % remove components from data
    EEG = pop_subcomp(EEG, comp2rej);

    % store file after component removal
    fn2save = sprintf('%s%sS%02d_newmethod4_comprem',subfile.folder,filesep,isub);
    save(fn2save,'EEG','comp2rej');

end

