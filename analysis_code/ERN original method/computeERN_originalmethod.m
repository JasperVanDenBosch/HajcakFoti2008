close all; clearvars; clc

% This script re-references to the average of both earlobes, applies a 0.1-30Hz bandpass filter,
% epochs the data from -200 to 800 msec, applies regression-based removal of blinks and eye movements
% using the method developed by Gratton et al. (1983), and removes bad trials for individual channels.
% Last, it computes the ERN. All following Hajcak & Foti 2008. 
rootdir = '/Users/ingmardevries/Library/CloudStorage/GoogleDrive-ingmar.devries@unitn.it/My Drive/Active projects/HajcakFoti2008/';

rootdir = 'D:\Dropbox\Science\EEG_database\#EEGML_temp\HajcakFoti2008\biotrialValeryPilot\EEG Many Labs\'
addpath(genpath(rootdir));
data_path = fullfile(rootdir,'data');
data_path = fullfile(rootdir);


addpath '/Users/ingmardevries/Library/CloudStorage/GoogleDrive-ingmar.devries@unitn.it/My Drive/Active projects/Toolboxes/eeglab2024.0';
eeglab;

% parameters
chan4reref = 30;% channels to rereference (excl. EMG, EOG and TRIGGER)
chan4filt = 30;% channels to filter (excl. EMG and TRIGGER)
bpfilt = [0.1 30];% bandpass filter band
epochtime = [-0.2 0.8];% time window to epoch
errtrig = 70;% trigger locked to error response
corrtrig = 20;% trigger locked to correct response
basetime = [-100 0];% baseline period in msec for single-trial baseline normalisation
ERNtime = [0 100];% time window to average over for ERN
ERNchan = {'FCz','Cz'};% first checks if FCz if present, otherwise uses Cz

% subject loop
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

    %apply bandpass filter (0.1-30Hz following Hajcak & Foti 2008)
    EEG= pop_basicfilter( EEG, 1:chan4filt , 'Cutoff', bpfilt, 'Design', 'butter', 'Filter', 'bandpass', 'Order', 2);

    % epoch the data
    EEG = pop_epoch(EEG, {num2str(errtrig), num2str(corrtrig)}, epochtime); 

    % regression-based correction for blinks
    selection_cards =  {num2str(errtrig), num2str(corrtrig)};
    EEG = gratton_emcp(EEG,selection_cards,{'VEOG'},{'HEOG'});

    % remove EOG channels and other channels not necessary anymore 
    %EEG = pop_select(EEG,'rmchannel',{'VEOG','HEOG','EMG','TRIGGER'});
    EEG = pop_select(EEG,'nochannel',{'VEOG','HEOG','EMG','TRIGGER'});


    % Automatic trial rejection per channel, with physiological artifacts identified by the following criteria:
    % 1. a voltage step of more than 50.0 μV between sample points
    % 2. a voltage difference of more than 300.0 μV within a trial
    % 3. a maximum voltage difference of less than 0.50 μV within a 100-ms interval.
    badtrialXchan = false(EEG.trials,EEG.nbchan);
    for itrial = 1:EEG.trials
        for ichan = 1:EEG.nbchan

            % toggle badtrial
            badtrial = false;

            % current trial
            trial = EEG.data(ichan,:,itrial);

            %1. a voltage step of more than 50.0 μV between sample points
            if any(abs(diff(trial)) > 50)
                badtrial = true;
            end

            % 2. a voltage difference of more than 300.0 μV within a trial        
            if range(trial) > 300
                badtrial = true;
            end

            % 3. a maximum voltage difference of less than 0.50 μV within a 100-ms interval.
            nint = ceil((EEG.xmax-EEG.xmin)/.1);% number of 100 msec intervals
            intlen = round(.1*EEG.srate);% interval length in samples
            for iint = 1:nint

                interval = trial(1+intlen*(iint-1):intlen*iint);
                if range(interval) < .50
                    badtrial = true;
                end
            end% interval loop

            % mark bad trial X channel combinations by changing values to
            % NaN, which will later be omitted when averaging for ERN
            if badtrial

                badtrialXchan(itrial,ichan) = 1;
                EEG.data(ichan,:,itrial) = nan;

            end

            % toggle badtrial
            badtrial = false;

        end% channel loop
    end% trial loop
 
    % single-trial baseline normalisation
    EEG = pop_rmbase(EEG, basetime);

    % find error trials
    triggers = zeros(EEG.trials,1);
    for itrial = 1:EEG.trials

        % to be absolutely sure we are looking at the correct event, find
        % the event with a latency of zero in each trial
        latencies = extractfield(EEG.epoch(itrial),'eventlatency');
        trigID = cell2mat(latencies{:}) == 0;
        types = extractfield(EEG.epoch(itrial),'eventtype');
        triggers(itrial) = cell2mat(types{:}(trigID));

    end% trial loop

    % compute ERP waveforms
    ERP(1,:,:) = mean(EEG.data(:,:,triggers==errtrig),3,'omitnan');% error trials
    ERP(2,:,:) = mean(EEG.data(:,:,triggers==corrtrig),3,'omitnan');% correct trials
    ERP_all(isub,:,:,:) = ERP;

    % find ERN electrode
    try
        chanID = eeg_chaninds(EEG,ERNchan(1));
    catch
        chanID = eeg_chaninds(EEG,ERNchan(2));
    end

    % compute ERN, defined as the average activity in a 0- to 100-ms window
    % following response onset on error trials
    toi = dsearchn(EEG.times',ERNtime');
    ERN = mean(ERP(1,chanID,toi(1):toi(2)),'omitnan');

    % extract some info for storage
    time = EEG.times;
    labels = EEG.chanlocs;

    % store for each subject how many trials went into final ERN, excluding noisy rejected trials
    ERNtrialcount = sum(~badtrialXchan(triggers == errtrig,chanID));
    badtrialXchan = sum(badtrialXchan);% total amount of bad trials per channel

    % store data in subject folder
    fn2save = sprintf('%s%sS%02d_ERN_originalmethod',subfile.folder,filesep,isub);
    save(fn2save,'ERP','ERN','time','labels','badtrialXchan','ERNtrialcount','chanID');

    disp(['Saved participant ' num2str(isub)])
    
end% subject loop



