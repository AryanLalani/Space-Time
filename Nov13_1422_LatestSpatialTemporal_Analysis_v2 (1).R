#-----------------------DATA ANALYSIS--------------------#
#--------------------------------------------------------#

#-----Installing and Loading Libraries-----#
install.packages("dplyr")
install.packages("janitor")
install.packages("stringr")
install.packages("ggplot2")
install.packages("rstatix")
install.packages("lme4")

library(dplyr)
library(janitor)
library(stringr)
library(ggplot2)
library(rstatix)
require(tidyverse)

#-------------------------Importing Data--------------------------#
# Before importing the data, go into the csv file and change column
# "First two letters of each Parents First Name and their date of birth. E~g~ hapa1114"
# name to Participant_ID

setwd("~/Desktop/Pilot data 05") #Setting your working directory

# Read the data (the original output from Pavlovia as a .csv file)
dat = read.csv("Database_AllParticipants_WhitakerPilotTest05.csv") 

# Do not use 'na.rm' at the end of this code because it will not give a proper output.

#------------------------Setting up data------------------------#
# Convert the structure of the data to numeric form
dat$mouse_cal_end_2.x = as.numeric(dat$mouse_cal_end_2.x)


# We will create a new data set called 'dat' and select only 
# the columns that we need:
dat = dat %>%
  select(durations, disp, start, display, durationsdistractor1,durationsdistractor2,
         mouse_startx.x,mouse.x,Participant_ID,practicetrialend_key_resp.keys,StartTime,EndTime)

#-------------------Important Terms Defined---------------------#
# practicetrialend_key_resp.keys indicates where the training ends for each participant
# mouse_startx.x indicates where the mouse is located in the beginning of the spatial task (in pixel)
# mouse.x indicates where the mouse is located at the end of the spatial task (in pixel)
# StartTime indicaes the time at beginning of a timing task
#EndTime indicates the time at end of a timing task

#-------------> Continue to set up data <------------------#
MainExperimentHasStarted = FALSE
for (i in 1:length(dat$disp)){
  
  #this goes through the CSV and checks whether rows belong to training/other setup components or to the main experiment
  if (dat$practicetrialend_key_resp.keys[i] != ""){
    MainExperimentHasStarted = TRUE
  } else if (MainExperimentHasStarted && (dat$Participant_ID[i] != dat$Participant_ID[i-1])) {
    MainExperimentHasStarted = FALSE
  }
  
  #Here we make a new column that indicates whether the specific row belongs to training/other setup components of to the main experiment
  if(MainExperimentHasStarted){
    dat$PartOfExperiment[i] = "MainExperiment"     
  } else {
    dat$PartOfExperiment[i] = "Other"
  }
}

# We need to filter everything out we do not want and 
# only keep "main experiment" components
dat = dat %>% filter(PartOfExperiment == "MainExperiment" & practicetrialend_key_resp.keys == "") %>% 
  group_by(Participant_ID) %>%
  slice(1:100)

# We need to go through the remaining columns to check if "display" is an empty character ("") for each
for(i in 1:length(dat$disp)){

  if(dat$display[i] != ""){#if it's not, then we add t he values from this row to the previous row. We do this for:
    dat$display[i-1] = dat$display[i] # display
    dat$durationsdistractor1[i-1] = dat$durationsdistractor1[i] # durationsdistractor1
    dat$durationsdistractor2[i-1] = dat$durationsdistractor2[i] # durationsdistractor2
    dat$durations[i-1] = dat$durations[i] # durations
    dat$disp[i-1] = dat$disp[i] # disp
    # this adds all the relevant values from the two separate rows to the previous row. The previous row is the one that has all the relevant information.
  }
  
  dat$Trial[i] = round(i/2+0.1,0) # Using a quick method to assign trial numbers in R, considering that one trial has two rows
}

dat = dat %>% group_by(Trial,Participant_ID) %>% 
  slice(1) # we keep only the first one that has all the relevant values

# We need to create data sets that separate the spatial and timing data:
dat_spatial = dat %>% 
  filter(display == "line")

dat_timing = dat %>% 
  filter(display == "time")

# We make new columns for the actual response variable in each data set
# actual timing response (in seconds)
dat_timing$duration_response = dat_timing$EndTime-dat_timing$StartTime 
# This indicates how much time a person spent clicking 

dat_timing$total_length = dat_timing$disp/2 * dat_timing$durations 
# This indicates the actual displacement of the line

# actual spatial response (in pixel)
dat_spatial$distance_response = dat_spatial$mouse.x-dat_spatial$mouse_startx.x
# This indicates the estimated length of the line made by the participant

dat_spatial$total_length = dat_spatial$disp/2 * dat_spatial$durations
# This indicates the actual displacement of the line

#------------------------LINEAR MIXED MODELS--------------------------#
# Hypothesis 1: Participants will use spatial information in their temporal
# estimates in both control and experimental conditions

require(lmerTest)
Model3 = lmer(duration_response ~ total_length + (1 | Participant_ID),
              data = dat_timing)
summary(Model3)

# Since this Model4 (Hypothesis 3) will also generate output for Model3 (Hypothesis 1) 
# association we will use Model4. 
# Model3 code is here just to show the variables specific to Hypothesis 1.


# Hypothesis 2: Participants will use temporal information in their spatial 
# estimates in both control and experimental conditions
require(lmerTest)

# Change the variable names to relevant ones from the spatial data set:
Model2 = lmer(total_length ~ distance_response + (1 | Participant_ID),
             data = dat_spatial)
summary(Model2)

# Hypothesis 3: the effect of spatial information in temporal estimates will 
# be greater in the experimental condition.
# This is because increased cognitive load will result in greater inaccuracy of 
# temporal estimates, thereby amplifying the asymmetry of the space-time relationship. 

#-----------> Conditionally recoding to get two conditions <------------#
# 1) Baseline (control) and  2) ExperimentConditon (experimental condition)

dat_timing = dat_timing %>%
  mutate(Condition = case_when(
    durationsdistractor1 == 0 ~ "Baseline",
    durationsdistractor1 != 0 ~ "ExperimentalCondition",
  ))

require(lmerTest)

Model4 = lmer(duration_response ~ total_length * Condition  + (1 | Participant_ID),
              data = dat_timing)
summary(Model4)


#-------------------------------END OF R SYNTAX--------------------------------#
