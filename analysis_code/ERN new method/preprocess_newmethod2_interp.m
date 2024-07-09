close all; clearvars; clc

%This script enables you to interpolate 'bad' channels before doing ICA
rootdir = '/Users/ingmardevries/Library/CloudStorage/GoogleDrive-ingmar.devries@unitn.it/My Drive/Active projects/HajcakFoti2008/';
addpath(genpath(rootdir));
data_path = fullfile(rootdir,'data');

addpath '/Users/ingmardevries/Library/CloudStorage/GoogleDrive-ingmar.devries@unitn.it/My Drive/Active projects/Toolboxes/eeglab2024.0';
eeglab;

%% Loops through each subject and plots the data to allow for checking channels.
% The computer will then ask you for input for interpolation
% If the data looks okay without interpolation, just press enter without
% entering any input

for isub = 1:20 %change the first number to start from the desired participant file if you have taken a break from interpolation and are coming back to it
    
    clear interp_channels;
    
    % get folder name for this subject
    subfolder = dir(sprintf('%s%sS%02d*',data_path,filesep,isub));

    % get EEG  file name for this subject
    subfile = dir(sprintf('%s%s%s%s*.cdt',subfolder.folder,filesep,subfolder.name,filesep));

    % load re-referenced and filtered data from previous step
    fn2load = sprintf('%s%sS%02d_newmethod1_filtreref',subfile.folder,filesep,isub);
    load(fn2load,'EEG');
    
    %plot data, scroll horizontally to see if certain channels are
    %consistently bad, better to start checking from the start of the real
    %blocks onwards (first trigger value of 160), because if subjects were
    %still moving a lot before the experiment started, it'll look more
    %noisy than it might be during the real experiment. 
    close all
    pop_eegplot( EEG, 1, 1, 1); %plot data
    
    %display which file is being interpolated
    disp(['Currently checking participant ' num2str(isub)])
    
    %prompt for saving data
    answers2 = input('Save data? Press 1 for Yes or 2 if you want to interpolate channel(s): ');

    if answers2 == 1
        % store interpolated file for next step
        fn2save = sprintf('%s%sS%02d_newmethod2_interp',subfile.folder,filesep,isub);
        save(fn2save,'EEG');
        continue
    end

    %Matlab will ask you which channel numbers you would like to interpolate
    answers = input('Which channels would you like to interpolate? Enter the names, separated by a comma: ','s');
    chosen_channels = regexprep(answers,',',' ');
    
    %interpolates channels
    EEG = pop_interp(EEG, eeg_chaninds(EEG,chosen_channels), 'spherical');
    
    %save channels that were interpolated
    interp_channels = eeg_chaninds(EEG,chosen_channels);
    
    %% Either save data or repeat process until desired result
    
    k = 0;
    
    while k < 1
        
        close all 
        pop_eegplot( EEG, 1, 1, 1);

        %prompt for saving data
        answers2 = input('Save data? Press 1 for Yes or 2 if you want to select more channels: ');
        
        if answers2 == 1
            
            %save which channels were interpolated as part of EEG struct
            EEG.interpChannels = interp_channels;

            % store interpolated file for next step
            fn2save = sprintf('%s%sS%02d_newmethod2_interp',subfile.folder,filesep,isub);
            save(fn2save,'EEG');
            
            k = k + 1;
            
            disp(['Saved participant ' num2str(isub)])
            
        else
            
            answers = input('Which channels would you like to interpolate? Enter the names, separated by a comma: ','s');
            chosen_channels = regexprep(answers,',',' ');
            
            interp_channels = [interp_channels eeg_chaninds(EEG,chosen_channels)];
            
            EEG = pop_interp(EEG, eeg_chaninds(EEG,chosen_channels), 'spherical');
            
            k = 0;
            
        end
        
    end
    
    
end


