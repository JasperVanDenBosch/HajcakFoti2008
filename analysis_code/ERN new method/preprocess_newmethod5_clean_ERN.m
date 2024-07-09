close all; clearvars; clc

%This script adds correct events and epochs data
rootdir = '/Users/ingmardevries/Library/CloudStorage/GoogleDrive-ingmar.devries@unitn.it/My Drive/Active projects/HajcakFoti2008/';
addpath(genpath(rootdir));
data_path = fullfile(rootdir,'data');

addpath '/Users/ingmardevries/Library/CloudStorage/GoogleDrive-ingmar.devries@unitn.it/My Drive/Active projects/Toolboxes/eeglab2024.0';
eeglab;

% parameters
basetime = [-100 0];% baseline period in msec
errtrig = 70;% trigger locked to error response
corrtrig = 20;% trigger locked to correct response
ERNtime = [0 100];% time window to average over for ERN
ERNchan = {'FCz','Cz'};% first checks if FCz if present, otherwise uses Cz
threshold_DB = 90;% deciBell threshold for automatic bad trial rejection
threshold_SD = 3.29;% standard deviation threshold for automatic trial rejection

%% subject loop
for isub = 1:20

    % get folder name for this subject
    subfolder = dir(sprintf('%s%sS%02d*',data_path,filesep,isub));

    % get EEG  file name for this subject
    subfile = dir(sprintf('%s%s%s%s*.cdt',subfolder.folder,filesep,subfolder.name,filesep));

    % load data from previous step
    fn2load = sprintf('%s%sS%02d_newmethod4_comprem',subfile.folder,filesep,isub);
    load(fn2load,'EEG');

    % single-trial baseline normalisation
    EEG = pop_rmbase(EEG, basetime);

    % find ERN electrode
    try
        chanID = eeg_chaninds(EEG,ERNchan(1));
    catch
        chanID = eeg_chaninds(EEG,ERNchan(2));
    end

    %% reject trials that are still noisy at this point (epochs deviating more than 3.29 SD) (Ref Tabachnik 2007)
    % from trimmed normalized means with respect to joint probability, kurtosis or the spectrum)
    % code adapted from  Paul et al. (2021): https://osf.io/2w9gy/?view_only=d79c0538c9e04f1298848dcfd7266d5d
    % only apply this bad trial rejection procedure on the ERN channel
    Clean_Epochs_Mask = ones(1,EEG.trials);

    % Check Frequency Spectrum
    [~, bad_Spectrum] = pop_rejspec(EEG, 1, 'elecrange', chanID, 'threshold', [-threshold_DB threshold_DB], 'freqlimits', [1 30]);
    Clean_Epochs_Mask(bad_Spectrum) = 0;

    % Check Kurtosis
    bad_Kurtosis = pop_rejkurt(EEG, 1, chanID,  threshold_SD,threshold_SD,0,0,0);
    bad_Kurtosis = find(bad_Kurtosis.reject.rejkurt);
    Clean_Epochs_Mask(bad_Kurtosis) = 0;

    % Check Probability
    bad_Probability = pop_jointprob(EEG, 1, chanID,  threshold_SD, threshold_SD,0,0,0);
    bad_Probability = find(bad_Probability.reject.rejjp);
    Clean_Epochs_Mask(bad_Probability) = 0;

    % Remove bad Epochs
    EEG = pop_select( EEG, 'trial',find(Clean_Epochs_Mask));

    % find error trials
    triggers = zeros(EEG.trials,1);
    for itrial = 1:EEG.trials

        % to be absolutely sure we are looking at the correct event, find
        % the event with a latency of zero in each trial
        latencies = extractfield(EEG.epoch(itrial),'eventlatency');
        trigID = cell2mat(latencies{:}) == 0;
        types = extractfield(EEG.epoch(itrial),'eventtype');
        triggers(itrial) = str2double(types{:}(trigID));

    end% trial loop

    % compute ERP waveforms
    ERP(1,:,:) = mean(EEG.data(:,:,triggers==errtrig),3,'omitnan');% error trials
    ERP(2,:,:) = mean(EEG.data(:,:,triggers==corrtrig),3,'omitnan');% correct trials

    % store for each subject how many trials went into final ERN, per channel, and excluding noisy rejected trials
    ERNtrialcount = sum(triggers == errtrig);

    % compute ERN, defined as the average activity in a 0- to 100-ms window
    % following response onset on error trials
    toi = dsearchn(EEG.times',ERNtime');
    ERN = mean(ERP(1,chanID,toi(1):toi(2)),'omitnan');

    % extract some info for storage
    time = EEG.times;
    labels = EEG.chanlocs;
    badtrial = 240 - sum(~isnan(triggers));% total amount of bad trials for ERN channel

    % store data in subject folder
    fn2save = sprintf('%s%sS%02d_ERN_newmethod',subfile.folder,filesep,isub);
    save(fn2save,'ERP','ERN','time','labels','badtrial','ERNtrialcount','chanID');

    disp(['Saved participant ' num2str(isub)])

end
