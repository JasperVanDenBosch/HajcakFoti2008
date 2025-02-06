scenario = "ERN-No-Startle";
scenario_type = trials;
default_picture_duration = 1300;
default_font_size = 36;


response_matching = simple_matching;
#response_logging = log_active;

#lower limit for response events (in ms) to be associated with response active stimuli
default_stimulus_time_in = 0;

#upper limit of permissible response latencies
default_stimulus_time_out = 1200;

#the number of response buttons that will be used in this scenario -- must match selections in Response panel
active_buttons = 2;


#codes assigned to incorrect button responses; must match number of active buttons
button_codes = 9,10;

#codes assigned to correct button responses; must match number of active buttons
target_button_codes = 3,4;

response_logging = log_active;

#sends event codes
write_codes = true;

#width of pulses in milliseconds
pulse_width = 20;  
default_trial_duration = 1500; 

#assigned to the port parameter for stimulus events that do not define that parameter; does not affect output port used for responses?
default_output_port=1;    

#creates separate .pcl file
pcl_file = "ERN_No-Startle.pcl";

----------------------------------------------

begin;

     bitmap {filename = "fixation.bmp";} fixation;  #uploading fixation cross
#     bitmap {filename = "thumbsdown.jpg";} thumbs;
		
text {font_size=18; caption="You're doing a great job.  Press either mouse button to continue."; 
    system_memory=true;} pause;
    
    text {font_size=18; caption="Please try to respond faster.  Press either mouse button to continue."; 
    system_memory=true;} speedup;
    
    text {font_size=18; caption="Please try to be more accurate.  Press either mouse button to continue."; 
    system_memory=true;} moreaccurate;

text {font_size=18; caption="Please wait for the experimenter."; 
    system_memory=true;} wait;			
    
picture {bitmap fixation;
	x=0;
   y=-25;   
          } default; #renaming fixation cross to "default"

#names the stimulus pictures my_stim
array {
	picture { bitmap { filename = "All_Left.jpg"; }; x = 0; y = 0;};
	picture { bitmap { filename = "All_Right.jpg"; }; x = 0; y = 0;};
	picture { bitmap { filename = "Center_Left.jpg"; }; x = 0; y = 0;};
	picture { bitmap { filename = "Center_Right.jpg"; }; x = 0; y = 0;};
} my_stim;


#wavefile {filename = "startle3.wav";} fake;
        
#sound { wavefile fake;
#        volume = 1;
#      } startle_sound; 


#if person is responding too slowly, this is what will show up on their screen
trial{
   trial_type = first_response;  #specifies what responses, if any, will cause the trial to end
   trial_duration = forever;  #specifies that trial will last forever until any button is pressed
      picture {text speedup;
      x=0; y=0;};
      duration=next_picture;
} my_trial_go_faster;


#if person is responding too inaccurately, this is what will show up on the screen
trial{
   trial_type = first_response;
   trial_duration = forever;
      picture {text moreaccurate;
      x=0; y=0;};
      duration=next_picture;
} my_trial_more_accurate;


#if person is responding well, this is what will show up on the screen
trial{
   trial_type = first_response;
   trial_duration = forever;
      picture {text pause;
      x=0; y=0;};
      duration=next_picture;
} my_trial_good_job;

#wait for experimenter
trial{
   trial_type = first_response;
   trial_duration = forever;
      picture {text wait;
      x=0; y=0;};
      duration=next_picture;
} my_trial_wait;


#fixation cross; ITI
trial {  
    $d = 'ceil(5 * $random_value) * 100'; #randomizing ITI time
#specifies whether only responses during active stimuli, or all responses, can end a trial when trial_type is not fixed; when false = ignore response when no stimuli active
    all_responses = false; 
    start_delay=$d;
    trial_duration= 500;
    picture default; 
    duration=next_picture; #picture stays on the screen until the next picture shows up
} default2;


trial {       
  all_responses = false;
  trial_type = fixed; #button presses do not end the trial
  trial_duration = 200; #trial will end after 200 ms
    stimulus_event {      
      picture default;
      duration = 200; 
    } flank_stim;     
} flankers;  #flakers stimulus trial


trial {     
 trial_duration = 1800; #trial lasts 1.8 seconds
  trial_type = first_response; #trial will end after first button is pressed, regardless of whether it is correct or not
  stimulus_event {      
      picture default;
      time = 0;     
      duration = next_picture; #picture stays on the screen until next picture
      target_button = 2; #target response button
    } stim3;     
} target;

trial {
  all_responses = false;
  trial_duration = 300;
  trial_type = fixed; 
   picture default;
   duration=next_picture;
} early_startle_lag;

/*trial {
  all_responses = false;
  trial_duration = 800;
  trial_type = fixed;
   picture default;
   duration=next_picture;
} late_startle_lag; */

/*trial {
     trial_type = fixed;
     trial_duration = 100;
     picture default; 
     sound startle_sound;
     time = 0;
} startle;*/ 


trial{
   trial_type = first_response;
   trial_duration = forever;
	picture {
	text{caption = " "; }txt1;
	x=0; y=0;};
	duration = next_picture;
}main;

trial {       
  trial_type = first_response;
  trial_duration = forever; 
    stimulus_event {      
      picture default;
      duration = next_picture; 
    } prac_flank;     
} prac_flankers; #practice flankers -- the ones that appear before the practice block