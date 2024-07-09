
scenario = "ERN_Startle"; 					#This name will be displayed in the Presentation Status window when the scenario is running and preparing to run. 
													#It is also written to the first line of the logfile 
scenario_type = trials;						#Determines scenario type; this is always "trials" unless fMRI
default_picture_duration = 1300;			#Unless otherwise specified, show all pictures for 1300ms
default_font_size = 36;						#Unless otherwise specified, show all font at size 36 points
response_matching = simple_matching;	#Use current Presentation response matching criteria
default_stimulus_time_in = 0;				#By default, the stimulus will be enabled at the start of the trial (time = 0)
default_stimulus_time_out = 1200;		#By default, the stimulus will be disabled at 1200 ms after trial onset
active_buttons = 2; 							#There will be 2 active (selection) buttons for this task

button_codes = 9,10;							#If an error is made, codes 9 or 10 will be sent to log file

target_button_codes = 3,4;					#If a correct response is made, codes 3 or 4 will be sent to log file

response_logging = log_active;			#Responses that are ignored during a trial do not appear in the logfile
write_codes = true;							#Send event codes
pulse_width = 20;  							#Sets pulse width to 20 ms
default_trial_duration = 1500; 			#Trials will last 1500 seconds by default
default_output_port=1;    					#Sets the default output port for responses

pcl_file = "ERN_Startle.pcl"; 			#Name of pcl file that will be used to execute this scenario

#Begin naming different trials ---------------------------
begin;

     bitmap {filename = "fixation.bmp";} fixation;  #Uploads a bitmap of the fixation cross for the ITI and names it "fixation"
		
text {font_size=18; caption="You're doing a great job.  Press either mouse button to continue."; 
    system_memory=true;} pause; 			 				#Creating text at size 18 points that will show on screen in between blocks and assign it to a variable (i.e., pause)
    
    text {font_size=18; caption="Please try to respond faster.  Press either mouse button to continue."; 
    system_memory=true;} speedup; 					 	#Creating text at size 18 points that will show on screen in between blocks and assign it to a variable (i.e., speedup)
    
    text {font_size=18; caption="Please try to be more accurate.  Press either mouse button to continue."; 
    system_memory=true;} moreaccurate; 				#Creating text at size 18 points that will show on screen in between blocks and assign it to a variable (i.e., moreaccurate)

text {font_size=18; caption="Please wait for the experimenter."; 
    system_memory=true;} wait; 						 	#Creating text at size 18 points that will show on screen in between blocks	 and assign it to a variable (i.e., wait)	
    
picture {bitmap fixation;									#Makes the bitmap named "fixation" into a picture
	x=0;															#Placed in the middle of the screen horizontally
   y=-25;   													#And a bit below vertically
          } default; 										#Names this picture "default"

array {
	picture { bitmap { filename = "All_Left.jpg"; }; x = 0; y = 0;}; #my_stim(1)
	picture { bitmap { filename = "All_Right.jpg"; }; x = 0; y = 0;}; #my_stim(2)
	picture { bitmap { filename = "Center_Left.jpg"; }; x = 0; y = 0;}; #my_stim(3)
	picture { bitmap { filename = "Center_Right.jpg"; }; x = 0; y = 0;}; #my_stim(4)
} my_stim; 														#Uploads all flanker task images in an array of pictures, where to display them (i.e., center of screen) and names the array "my_stim"

wavefile {filename = "startle2.wav";} fake; 			#Uploads the wave file and names it "fake" why fake???
        
sound { wavefile fake;										#Makes the wavefile "fake" into a sound
        volume = 1;											#At maximum volume
      } startle_sound; 										#Names this sound "startle_sound"

#Trial that will show up if participant's accuracy > 90%, regardless of speed of response
trial{
   trial_type = first_response;		#Until a button is pressed,
   trial_duration = forever;			#The trial will continue
      picture {text speedup;			#And display the speed up text
      x=0; y=0;};							#At this location on the screen (i.e., center)
      duration=next_picture;			#This picture will stay on the screen until the next picture
} my_trial_go_faster; 					#Names the trial "my_trial_go_faster"



#Trial that will show up if participant's accuracy < 75%, regardless of speed of response
trial{
   trial_type = first_response;		#Until a button is pressed,
   trial_duration = forever;			#The trial will continue
      picture {text moreaccurate;	#And display the more accurate text
      x=0; y=0;};							#At this location on the screen (i.e., center)
      duration=next_picture;			#This picture will stay on the screen until the next picture
} my_trial_more_accurate;				#Names the trial "my_trial_more_accurate"


#Trial that will show up if participant is responding between 75% and 90%, regardless of speed of response
trial{
   trial_type = first_response;		#Until a button is pressed,
   trial_duration = forever;			#The trial will continue
      picture {text pause;				#And display the pause text
      x=0; y=0;};							#At this location on the screen (i.e., center)
      duration=next_picture;			#This picture will stay on the screen until the next photo
} my_trial_good_job;						#Names the trial "my_trial_good_job"


#Trial that will show up when participant is waiting for experimenter
trial{
   trial_type = first_response;		#Until a button is pressed,
   trial_duration = forever;			#The trial will continue
      picture {text wait;				#And display the wait text
      x=0; y=0;};							#At this location on the screen (i.e., center)
      duration=next_picture;			#This picture will stay on the screen until the next photo
} my_trial_wait;							#Names the trial "my_trial_wait"

#Creates intertrial interval (ITI) trial
trial {  
    $d = 'ceil(5 * $random_value) * 100';  #Creates random ITI variable
    all_responses = false;						 #Responses do not impact the length of the trial
    start_delay=$d;			 					#The time of trial onset relative to the end of the previous trial in milliseconds
    trial_duration= 500;						 #The ITI trial itself will last at least 500 ms by default
    picture default; 							#And display the fixation cross on the screen
    duration=next_picture;						#Lasts until next picture
} default2;											#Names this trial "default2"

#Creates flankers stimulus trial 
trial {       
  all_responses = false;		#Responses do not impact the length of the trial
  trial_type = fixed;			#Duration of the trial is not impacted by responses, it is fixed
  trial_duration = 200; 		#Trial lasts for 200ms
    stimulus_event {      		#Creates a stimulus event
      picture default;			#Fixation cross will automatically be on the screen
      duration = 200; 			#Stimulus is on the screen for 200ms
    } flank_stim;     			#calling the stimulus event "flank_stim"
} flankers;  						#names the trial "flankers"


#Creates trial that will log the response from each flankers trial, presented at the same time as the flankers stimulus trial and the ITI after it
trial {     
 trial_duration = 1800;				#Trial will last 1.8 seconds (response will be recorded within 1.8 seconds of stimulus event onset)
 trial_type = first_response;		#And will end at the first response, whether correct or incorrect
    stimulus_event {      			#Creates a stimulus event
      picture default;				#Fixation cross will automatically be on the screen
      time = 0;     					#Will begin at stimulus event onset relative to start of the trial containing the stimulus event (i.e., is played immediately when this trial begins)
      duration = next_picture; 	#And will last until the next picture
      target_button = 2;			#With 2 target buttons?
    } stim3;     						#Names this stimulus event "stim3"; will be used in the pcl file when setting stimulus image
} target;								#Names the trial "target"


#Creates startle lag between end of stimulus and presentation of startle sound
trial {
	 all_responses = false;		#Responses do not impact the length of the trial
	 trial_duration = 300;		#The trial will last for 300 ms
	 trial_type = fixed;			#The length of the trial is not impacted by responses, it is fixed
	 picture default;				#The fixation cross will be on the screen automatically
	 duration=next_picture;		#And will be displayed until the next picture is displayed
} early_startle_lag;				#Names this trial "early_startle_lag"


#Not used in this task but left in (and commented out) when sent to us from original lab
/* trial {
	 all_responses = false;
	 trial_duration = 800;
	 trial_type = fixed;
	 picture default;
	 duration=next_picture;
} late_startle_lag; */

#Creates startle sound trial
trial {
	 trial_type = fixed;			#Responses do not end the trial -- duration is fixed
	 trial_duration = 100;		#Sound is played for 50ms, 50 ms buffer
   	 picture default; 		#Fixation cross is on the screen by default	
    	 sound startle_sound;	#Loads the startle sound for the trial
	 time = 0;						#To start at stimulus event onset relative to start of the trial containing the stimulus event (i.e., is played immediately when this trial begins)
} startle; 							#Names this trial "startle"

#???
trial{
   trial_type = first_response;		#Until a button is pressed, 
   trial_duration = forever;			#The trial will continue
	picture {								#Display
	text{caption = " "; }txt1;			#A blank space on the screen that will later be changed
	x=0; y=0;};								#In the center
	duration = next_picture;			#And will be displayed until the next picture is displayed
}main;										#Names this trial "main"

#Creates practice flankers for practice block
trial {       
  trial_type = first_response;	#Until a response is made (correct or not),
  trial_duration = forever; 		#The trial will continue
    stimulus_event {      			#Creates a stimulus event
      picture default;				#Fixation cross is on the screen by default
      duration = next_picture; 	#Lasts until the next picture comes onto the screen
    } prac_flank;     				#Names this stimulus event "prac_flank"; will be used in the pcl file when setting stimulus image and target button
} prac_flankers; 						#Names this trial "prac_flankers"