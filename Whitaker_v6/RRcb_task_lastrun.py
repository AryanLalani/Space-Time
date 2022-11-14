#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on September 09, 2022, at 16:58
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2020.2.4')


from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'RRcb_task'  # from the Builder filename that created this script
expInfo = {'participant ID': '', 'age': '', 'gender': '', 'first language': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\bjoer\\Dropbox\\Science\\Teaching\\PSYC3010 Advanced Research Methods\\Week 1\\PsychoPy + Pavlovia Papers\\Whitaker 2022\\PsychoPy\\RRcb_task_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "gen_instructions"
gen_instructionsClock = core.Clock()
instruction_text_4 = visual.TextStim(win=win, name='instruction_text_4',
    text='In this experiment you will be completing a task in which you will judge the amount of time an object appears or how far an object travels on your computer screen. This task should take approximately 30 minutes. You can move through this experiment at your own pace, and you will receive a designated break half way through. \n\nYou will receive more instructions before starting. Please make sure your browser is in full screen mode (press "F11" to make browser full screen on a PC and "control+command+F" on a Mac). Press "esc" at any point if you would like to completely exit the experiment. \n\nPress "space" to move onto the next screen.\n',
    font='Arial',
    units='height', pos=(0, 0), height=.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructions_key_resp_3 = keyboard.Keyboard()
thisExp=psychoJS.experiment;
win=psychoJS.window;
event=psychoJS.eventManager;
shuffle = util.shuffle;
Array.prototype.append = [].push

# Initialize components for Routine "screen_calibration"
screen_calibrationClock = core.Clock()
calibration_instructions = visual.TextStim(win=win, name='calibration_instructions',
    text='Click the two ends of the line (click the middle of the  "X\'s") to calibrate your screen size. ',
    font='Arial',
    units='height', pos=(0, .25), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
cal_line = visual.Line(
    win=win, name='cal_line',
    start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
    ori=0, pos=[0,0],
    lineWidth=5, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
c_start_x = visual.ShapeStim(
    win=win, name='c_start_x', vertices='cross',
    size=(50, 50),
    ori=45, pos=(-200, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
c_end_x = visual.ShapeStim(
    win=win, name='c_end_x', vertices='cross',
    size=(50, 50),
    ori=45, pos=(200, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
cal_mouse_start = event.Mouse(win=win)
x, y = [None, None]
cal_mouse_start.mouseClock = core.Clock()

# Initialize components for Routine "screen_calibration_end"
screen_calibration_endClock = core.Clock()
calibration_instructions_2 = visual.TextStim(win=win, name='calibration_instructions_2',
    text='Click the two ends of the line (click the middle of the  "X\'s") to calibrate your screen size.  ',
    font='Arial',
    units='height', pos=(0, .25), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
cal_line_2 = visual.Line(
    win=win, name='cal_line_2',
    start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
    ori=0, pos=[0,0],
    lineWidth=5, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
c_start_x_2 = visual.ShapeStim(
    win=win, name='c_start_x_2', vertices='cross',
    size=(50, 50),
    ori=45, pos=(-200, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
c_end_x_2 = visual.ShapeStim(
    win=win, name='c_end_x_2', vertices='cross',
    size=(50, 50),
    ori=45, pos=(200, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
mouse_cal_end_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_cal_end_2.mouseClock = core.Clock()

# Initialize components for Routine "screen_calibration_end_2"
screen_calibration_end_2Clock = core.Clock()
calibration_instructions_3 = visual.TextStim(win=win, name='calibration_instructions_3',
    text='Click the two ends of the line (click the middle of the  "X\'s") to calibrate your screen size. ',
    font='Arial',
    units='height', pos=(0, .25), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
cal_line_3 = visual.Line(
    win=win, name='cal_line_3',
    start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
    ori=0, pos=[0,0],
    lineWidth=5, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
c_start_x_3 = visual.ShapeStim(
    win=win, name='c_start_x_3', vertices='cross',
    size=(50, 50),
    ori=45, pos=(-200, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
c_end_x_3 = visual.ShapeStim(
    win=win, name='c_end_x_3', vertices='cross',
    size=(50, 50),
    ori=45, pos=(200, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Initialize components for Routine "candb_instructions"
candb_instructionsClock = core.Clock()
instruction_text = visual.TextStim(win=win, name='instruction_text',
    text='In this task, you will see lines that grow across the screen. Pay attention to both the final length of the line as well as the total amount of time the line is on the screen. After the line disappears a prompt saying either "time" or "line" will appear. If the prompt says "line" you will be reproducing the length of the line, and if the prompt says "time" you will be reproducing the amount of time you think the line was on the screen for.\n\nOn "line" trials, you will see an "X" appear in the top or bottom left-hand corner of the screen. You will click this "X", and then (moving in a straight line horizontally from the first "X") click again to place another "X" at a distance away from the initial "X" that you think is equivalent to the length of the line you just saw. On the "time" trials you will see a grey hourglass icon appear in the top or bottom left-hand corner of the screen. You will click in this hourglass to start your duration reproduction and then you will click the hourglass again to end your duration reproduction (i.e., when you think the amount of time that has passed since you clicked the hourglass the first time is equivalent to the amount of time the line that you just saw appeared on the screen). \n\nOn the next screen you will see a video demonstration of this task, and then you will get a chance to practice doing the task before you start the experimental trials. Press "space" to move onto the next screen.\n',
    font='Arial',
    units='height', pos=(0, 0), height=.032, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructions_key_resp = keyboard.Keyboard()

# Initialize components for Routine "Consent"
ConsentClock = core.Clock()
consent_loading = visual.TextStim(win=win, name='consent_loading',
    text='Loading...',
    font='Arial',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "practice_instructions"
practice_instructionsClock = core.Clock()
instruction_text_3 = visual.TextStim(win=win, name='instruction_text_3',
    text='As previously mentioned, you can move through this experiment at your own pace, so feel free to take as much time as you need after each trial.  During this task, we encourage you to take a break if you feel you need it at any point in the experiment by simply not pressing "space" to move onto the next trial until you are ready to do so. \n\nOn each trial, please pay attention to both the length and amount of time the line appears on the screen for. This experiment is aimed at measuring your innate perception of space and time, so it is important that you don\'t count or use your computer screen as a frame of reference for the lines. \n\nOn the next screen you will complete a couple of practice trials to get familiar with this task, and then you will be able to view instructions for this task again before starting the experimental trials. Press "space" to continue.\n\n',
    font='Arial',
    units='height', pos=(0, 0), height=.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instructions_key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "fixationcrosses"
fixationcrossesClock = core.Clock()
fixation_cross = visual.ShapeStim(
    win=win, name='fixation_cross', vertices='cross',
    size=(150, 150),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
trial_counter=0;

# Initialize components for Routine "targetlines"
targetlinesClock = core.Clock()
targetline = visual.Line(
    win=win, name='targetline',
    start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
    ori=0, pos=[0,0],
    lineWidth=5, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "prompt"
promptClock = core.Clock()
prompt_text = visual.TextStim(win=win, name='prompt_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=75, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "start_x"
start_xClock = core.Clock()
startx = visual.ShapeStim(
    win=win, name='startx', vertices='cross',units='height', 
    size=(0.06, 0.06),
    ori=45, pos=[0,0],
    lineWidth=3, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
mouse_startx = event.Mouse(win=win)
x, y = [None, None]
mouse_startx.mouseClock = core.Clock()

# Initialize components for Routine "end_x"
end_xClock = core.Clock()
startx_ph = visual.ShapeStim(
    win=win, name='startx_ph', vertices='cross',units='height', 
    size=(0.06, 0.06),
    ori=45, pos=[0,0],
    lineWidth=3, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
polygon = visual.Rect(
    win=win, name='polygon',units='height', 
    width=(1.6, 0.1)[0], height=(1.6, 0.1)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "pause"
pauseClock = core.Clock()
startx_4 = visual.ShapeStim(
    win=win, name='startx_4', vertices='cross',units='height', 
    size=(0.06, 0.06),
    ori=45, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "hg_start"
hg_startClock = core.Clock()
hg_bottom = visual.ShapeStim(
    win=win, name='hg_bottom',units='height', 
    vertices=[[-(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [+(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [0,(0.08, 0.06)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
mouse_hg = event.Mouse(win=win)
x, y = [None, None]
mouse_hg.mouseClock = core.Clock()
hg_top = visual.ShapeStim(
    win=win, name='hg_top',units='height', 
    vertices=[[-(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [+(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [0,(0.08, 0.06)[1]/2.0]],
    ori=180, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "hg_mid"
hg_midClock = core.Clock()
hg_bottom_2 = visual.ShapeStim(
    win=win, name='hg_bottom_2',units='height', 
    vertices=[[-(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [+(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [0,(0.08, 0.06)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
mouse_hg_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_hg_2.mouseClock = core.Clock()
hg_top_2 = visual.ShapeStim(
    win=win, name='hg_top_2',units='height', 
    vertices=[[-(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [+(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [0,(0.08, 0.06)[1]/2.0]],
    ori=180, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "hg_end"
hg_endClock = core.Clock()
hg_bottom_3 = visual.ShapeStim(
    win=win, name='hg_bottom_3',units='height', 
    vertices=[[-(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [+(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [0,(0.08, 0.06)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
hg_top_3 = visual.ShapeStim(
    win=win, name='hg_top_3',units='height', 
    vertices=[[-(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [+(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [0,(0.08, 0.06)[1]/2.0]],
    ori=180, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "ready"
readyClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Press the "space" when you are ready to move onto the next trial. ',
    font='Arial',
    units='height', pos=(0, 0), height=.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instruction_req = visual.TextStim(win=win, name='instruction_req',
    text='Press "i" to see instructions again, press "t" for troubleshooting help. ',
    font='Arial',
    units='height', pos=(0, -.25), height=.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "reminder"
reminderClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Great job! Below is a reminder of the instructions now that you have seen the task. \n\nAs lines grow across the screen, please pay attention to both the final length of the line as well as the total amount of time the line is on the screen. If the prompt says "time" you will be reproducing the duration (amount of time) the line appeared on the screen, if the prompt says "line" you will be reproducing the length of the line (the amount of space the line takes up on your screen). \n\nOn "line" trials, please click the "X", and then place another "X" (with your mouse click) at a horizontal distance away from the initial "X" that you think is equivalent to the length of the line you just saw. On the "time" trials, you will click the grey hourglass to start your duration reproduction, and again when you think the amount of time that has passed since you first clicked the hourglass is equivalent to the amount of time the line that you just saw.\n\nYou will now move onto a few more practice trials, before stating the experiment. Press "space" to continue. ',
    font='Arial',
    units='height', pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "troubleshooting"
troubleshootingClock = core.Clock()
troubleshooting_text = visual.TextStim(win=win, name='troubleshooting_text',
    text='Below is a troubleshooting guide:\n\nUnable to get back to fullscreen? \nWindows: press "F11" \nMac: press "control+command+F" if the toolbar/taskbar is still visible, then go to View> and make sure that the option "Always Show Toolbar in Fullscreen" is deselected (i.e. doesn\'t have a check mark next to it). \n\nWant to exit the experiment completely ? \nPress "esc" \n\nIf you are having any other issues please contact mirinda.whitaker@utah.edu or call (435)216-8979 for further assistance. \n\nPress "space" to continue with task. ',
    font='Arial',
    units='height', pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_11 = keyboard.Keyboard()

# Initialize components for Routine "request_inst"
request_instClock = core.Clock()
instruction_re_text = visual.TextStim(win=win, name='instruction_re_text',
    text='Below is a reminder of the instructions:\n\nAs lines grow across the screen, please pay attention to both the final length of the line as well as the total amount of time the line is on the screen. If the prompt says "time" you will be reproducing the duration (amount of time) the line appeared on the screen, if the prompt says "line" you will be reproducing the length of the line (the amount of space the line takes up on your screen). \n\nOn "line" trials, please click the "X", and then place another "X" (with your mouse click) at a horizontal distance away from the initial "X" that you think is equivalent to the length of the line you just saw. On the "time" trials, you will click the grey hourglass to start your duration reproduction, and again when you think the amount of time that has passed since you first clicked the hourglass is equivalent to the amount of time the line that you just saw was on the screen. \n\nPress "space" to continue with task. ',
    font='Arial',
    units='height', pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "practicetrialendscreen"
practicetrialendscreenClock = core.Clock()
practicetrialend_text = visual.TextStim(win=win, name='practicetrialend_text',
    text='The practice trials are now finished. \n\nIf you have any questions before starting the experiment, please contact mirinda.whitaker@utah.edu before continuing. If you want to see the experimental instructions again press the "i" key on your keyboard between trials. If you run into any issues with the experiment, press "t" to see a troubleshooting screen.\n\nPress the "space" to start the experiment.',
    font='Arial',
    units='height', pos=(0, 0), height=.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
practicetrialend_key_resp = keyboard.Keyboard()

# Initialize components for Routine "fixationcrosses"
fixationcrossesClock = core.Clock()
fixation_cross = visual.ShapeStim(
    win=win, name='fixation_cross', vertices='cross',
    size=(150, 150),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
trial_counter=0;

# Initialize components for Routine "targetlines"
targetlinesClock = core.Clock()
targetline = visual.Line(
    win=win, name='targetline',
    start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
    ori=0, pos=[0,0],
    lineWidth=5, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "prompt"
promptClock = core.Clock()
prompt_text = visual.TextStim(win=win, name='prompt_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=75, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "start_x"
start_xClock = core.Clock()
startx = visual.ShapeStim(
    win=win, name='startx', vertices='cross',units='height', 
    size=(0.06, 0.06),
    ori=45, pos=[0,0],
    lineWidth=3, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
mouse_startx = event.Mouse(win=win)
x, y = [None, None]
mouse_startx.mouseClock = core.Clock()

# Initialize components for Routine "end_x"
end_xClock = core.Clock()
startx_ph = visual.ShapeStim(
    win=win, name='startx_ph', vertices='cross',units='height', 
    size=(0.06, 0.06),
    ori=45, pos=[0,0],
    lineWidth=3, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
polygon = visual.Rect(
    win=win, name='polygon',units='height', 
    width=(1.6, 0.1)[0], height=(1.6, 0.1)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1.000,1.000,1.000], lineColorSpace='rgb',
    fillColor=[1.000,1.000,1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "pause"
pauseClock = core.Clock()
startx_4 = visual.ShapeStim(
    win=win, name='startx_4', vertices='cross',units='height', 
    size=(0.06, 0.06),
    ori=45, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "hg_start"
hg_startClock = core.Clock()
hg_bottom = visual.ShapeStim(
    win=win, name='hg_bottom',units='height', 
    vertices=[[-(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [+(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [0,(0.08, 0.06)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
mouse_hg = event.Mouse(win=win)
x, y = [None, None]
mouse_hg.mouseClock = core.Clock()
hg_top = visual.ShapeStim(
    win=win, name='hg_top',units='height', 
    vertices=[[-(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [+(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [0,(0.08, 0.06)[1]/2.0]],
    ori=180, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "hg_mid"
hg_midClock = core.Clock()
hg_bottom_2 = visual.ShapeStim(
    win=win, name='hg_bottom_2',units='height', 
    vertices=[[-(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [+(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [0,(0.08, 0.06)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
mouse_hg_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_hg_2.mouseClock = core.Clock()
hg_top_2 = visual.ShapeStim(
    win=win, name='hg_top_2',units='height', 
    vertices=[[-(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [+(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [0,(0.08, 0.06)[1]/2.0]],
    ori=180, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "hg_end"
hg_endClock = core.Clock()
hg_bottom_3 = visual.ShapeStim(
    win=win, name='hg_bottom_3',units='height', 
    vertices=[[-(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [+(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [0,(0.08, 0.06)[1]/2.0]],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
hg_top_3 = visual.ShapeStim(
    win=win, name='hg_top_3',units='height', 
    vertices=[[-(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [+(0.08, 0.06)[0]/2.0,-(0.08, 0.06)[1]/2.0], [0,(0.08, 0.06)[1]/2.0]],
    ori=180, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "ready"
readyClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Press the "space" when you are ready to move onto the next trial. ',
    font='Arial',
    units='height', pos=(0, 0), height=.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instruction_req = visual.TextStim(win=win, name='instruction_req',
    text='Press "i" to see instructions again, press "t" for troubleshooting help. ',
    font='Arial',
    units='height', pos=(0, -.25), height=.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "request_inst"
request_instClock = core.Clock()
instruction_re_text = visual.TextStim(win=win, name='instruction_re_text',
    text='Below is a reminder of the instructions:\n\nAs lines grow across the screen, please pay attention to both the final length of the line as well as the total amount of time the line is on the screen. If the prompt says "time" you will be reproducing the duration (amount of time) the line appeared on the screen, if the prompt says "line" you will be reproducing the length of the line (the amount of space the line takes up on your screen). \n\nOn "line" trials, please click the "X", and then place another "X" (with your mouse click) at a horizontal distance away from the initial "X" that you think is equivalent to the length of the line you just saw. On the "time" trials, you will click the grey hourglass to start your duration reproduction, and again when you think the amount of time that has passed since you first clicked the hourglass is equivalent to the amount of time the line that you just saw was on the screen. \n\nPress "space" to continue with task. ',
    font='Arial',
    units='height', pos=(0, 0), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "catchtrials"
catchtrialsClock = core.Clock()
catch_text = visual.TextStim(win=win, name='catch_text',
    text='default text',
    font='Arial',
    units='height', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "breakscreen"
breakscreenClock = core.Clock()
breakscreen_text = visual.TextStim(win=win, name='breakscreen_text',
    text='default text',
    font='Arial',
    units='height', pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
break_key_resp = keyboard.Keyboard()

# Initialize components for Routine "end_screen"
end_screenClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Thank you for your participation! Please wait while your data is saved. ',
    font='Arial',
    units='height', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "gen_instructions"-------
continueRoutine = True
# update component parameters for each repeat
instructions_key_resp_3.keys = []
instructions_key_resp_3.rt = []
_instructions_key_resp_3_allKeys = []
# keep track of which components have finished
gen_instructionsComponents = [instruction_text_4, instructions_key_resp_3]
for thisComponent in gen_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
gen_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "gen_instructions"-------
while continueRoutine:
    # get current time
    t = gen_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=gen_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_text_4* updates
    if instruction_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_text_4.frameNStart = frameN  # exact frame index
        instruction_text_4.tStart = t  # local t and not account for scr refresh
        instruction_text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_text_4, 'tStartRefresh')  # time at next scr refresh
        instruction_text_4.setAutoDraw(True)
    
    # *instructions_key_resp_3* updates
    waitOnFlip = False
    if instructions_key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_key_resp_3.frameNStart = frameN  # exact frame index
        instructions_key_resp_3.tStart = t  # local t and not account for scr refresh
        instructions_key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_key_resp_3, 'tStartRefresh')  # time at next scr refresh
        instructions_key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructions_key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructions_key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructions_key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = instructions_key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _instructions_key_resp_3_allKeys.extend(theseKeys)
        if len(_instructions_key_resp_3_allKeys):
            instructions_key_resp_3.keys = _instructions_key_resp_3_allKeys[-1].name  # just the last key pressed
            instructions_key_resp_3.rt = _instructions_key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in gen_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "gen_instructions"-------
for thisComponent in gen_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction_text_4.started', instruction_text_4.tStartRefresh)
thisExp.addData('instruction_text_4.stopped', instruction_text_4.tStopRefresh)
# check responses
if instructions_key_resp_3.keys in ['', [], None]:  # No response was made
    instructions_key_resp_3.keys = None
thisExp.addData('instructions_key_resp_3.keys',instructions_key_resp_3.keys)
if instructions_key_resp_3.keys != None:  # we had a response
    thisExp.addData('instructions_key_resp_3.rt', instructions_key_resp_3.rt)
thisExp.addData('instructions_key_resp_3.started', instructions_key_resp_3.tStartRefresh)
thisExp.addData('instructions_key_resp_3.stopped', instructions_key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "gen_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "screen_calibration"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the cal_mouse_start
cal_mouse_start.x = []
cal_mouse_start.y = []
cal_mouse_start.leftButton = []
cal_mouse_start.midButton = []
cal_mouse_start.rightButton = []
cal_mouse_start.time = []
cal_mouse_start.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
screen_calibrationComponents = [calibration_instructions, cal_line, c_start_x, c_end_x, cal_mouse_start]
for thisComponent in screen_calibrationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
screen_calibrationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "screen_calibration"-------
while continueRoutine:
    # get current time
    t = screen_calibrationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=screen_calibrationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *calibration_instructions* updates
    if calibration_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        calibration_instructions.frameNStart = frameN  # exact frame index
        calibration_instructions.tStart = t  # local t and not account for scr refresh
        calibration_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(calibration_instructions, 'tStartRefresh')  # time at next scr refresh
        calibration_instructions.setAutoDraw(True)
    
    # *cal_line* updates
    if cal_line.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cal_line.frameNStart = frameN  # exact frame index
        cal_line.tStart = t  # local t and not account for scr refresh
        cal_line.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cal_line, 'tStartRefresh')  # time at next scr refresh
        cal_line.setAutoDraw(True)
    if cal_line.status == STARTED:  # only update if drawing
        cal_line.setPos((0,0), log=False)
        cal_line.setSize(400, log=False)
    
    # *c_start_x* updates
    if c_start_x.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        c_start_x.frameNStart = frameN  # exact frame index
        c_start_x.tStart = t  # local t and not account for scr refresh
        c_start_x.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(c_start_x, 'tStartRefresh')  # time at next scr refresh
        c_start_x.setAutoDraw(True)
    
    # *c_end_x* updates
    if c_end_x.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        c_end_x.frameNStart = frameN  # exact frame index
        c_end_x.tStart = t  # local t and not account for scr refresh
        c_end_x.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(c_end_x, 'tStartRefresh')  # time at next scr refresh
        c_end_x.setAutoDraw(True)
    # *cal_mouse_start* updates
    if cal_mouse_start.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cal_mouse_start.frameNStart = frameN  # exact frame index
        cal_mouse_start.tStart = t  # local t and not account for scr refresh
        cal_mouse_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cal_mouse_start, 'tStartRefresh')  # time at next scr refresh
        cal_mouse_start.status = STARTED
        cal_mouse_start.mouseClock.reset()
        prevButtonState = cal_mouse_start.getPressed()  # if button is down already this ISN'T a new click
    if cal_mouse_start.status == STARTED:  # only update if started and not finished!
        buttons = cal_mouse_start.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [c_start_x]:
                    if obj.contains(cal_mouse_start):
                        gotValidClick = True
                        cal_mouse_start.clicked_name.append(obj.name)
                x, y = cal_mouse_start.getPos()
                cal_mouse_start.x.append(x)
                cal_mouse_start.y.append(y)
                buttons = cal_mouse_start.getPressed()
                cal_mouse_start.leftButton.append(buttons[0])
                cal_mouse_start.midButton.append(buttons[1])
                cal_mouse_start.rightButton.append(buttons[2])
                cal_mouse_start.time.append(cal_mouse_start.mouseClock.getTime())
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in screen_calibrationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "screen_calibration"-------
for thisComponent in screen_calibrationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('calibration_instructions.started', calibration_instructions.tStartRefresh)
thisExp.addData('calibration_instructions.stopped', calibration_instructions.tStopRefresh)
thisExp.addData('cal_line.started', cal_line.tStartRefresh)
thisExp.addData('cal_line.stopped', cal_line.tStopRefresh)
thisExp.addData('c_start_x.started', c_start_x.tStartRefresh)
thisExp.addData('c_start_x.stopped', c_start_x.tStopRefresh)
thisExp.addData('c_end_x.started', c_end_x.tStartRefresh)
thisExp.addData('c_end_x.stopped', c_end_x.tStopRefresh)
# store data for thisExp (ExperimentHandler)
if len(cal_mouse_start.x): thisExp.addData('cal_mouse_start.x', cal_mouse_start.x[0])
if len(cal_mouse_start.y): thisExp.addData('cal_mouse_start.y', cal_mouse_start.y[0])
if len(cal_mouse_start.leftButton): thisExp.addData('cal_mouse_start.leftButton', cal_mouse_start.leftButton[0])
if len(cal_mouse_start.midButton): thisExp.addData('cal_mouse_start.midButton', cal_mouse_start.midButton[0])
if len(cal_mouse_start.rightButton): thisExp.addData('cal_mouse_start.rightButton', cal_mouse_start.rightButton[0])
if len(cal_mouse_start.time): thisExp.addData('cal_mouse_start.time', cal_mouse_start.time[0])
if len(cal_mouse_start.clicked_name): thisExp.addData('cal_mouse_start.clicked_name', cal_mouse_start.clicked_name[0])
thisExp.addData('cal_mouse_start.started', cal_mouse_start.tStart)
thisExp.addData('cal_mouse_start.stopped', cal_mouse_start.tStop)
thisExp.nextEntry()
# the Routine "screen_calibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "screen_calibration_end"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_cal_end_2
mouse_cal_end_2.x = []
mouse_cal_end_2.y = []
mouse_cal_end_2.leftButton = []
mouse_cal_end_2.midButton = []
mouse_cal_end_2.rightButton = []
mouse_cal_end_2.time = []
mouse_cal_end_2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
screen_calibration_endComponents = [calibration_instructions_2, cal_line_2, c_start_x_2, c_end_x_2, mouse_cal_end_2]
for thisComponent in screen_calibration_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
screen_calibration_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "screen_calibration_end"-------
while continueRoutine:
    # get current time
    t = screen_calibration_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=screen_calibration_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *calibration_instructions_2* updates
    if calibration_instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        calibration_instructions_2.frameNStart = frameN  # exact frame index
        calibration_instructions_2.tStart = t  # local t and not account for scr refresh
        calibration_instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(calibration_instructions_2, 'tStartRefresh')  # time at next scr refresh
        calibration_instructions_2.setAutoDraw(True)
    
    # *cal_line_2* updates
    if cal_line_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cal_line_2.frameNStart = frameN  # exact frame index
        cal_line_2.tStart = t  # local t and not account for scr refresh
        cal_line_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cal_line_2, 'tStartRefresh')  # time at next scr refresh
        cal_line_2.setAutoDraw(True)
    if cal_line_2.status == STARTED:  # only update if drawing
        cal_line_2.setPos((0,0), log=False)
        cal_line_2.setSize(400, log=False)
    
    # *c_start_x_2* updates
    if c_start_x_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        c_start_x_2.frameNStart = frameN  # exact frame index
        c_start_x_2.tStart = t  # local t and not account for scr refresh
        c_start_x_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(c_start_x_2, 'tStartRefresh')  # time at next scr refresh
        c_start_x_2.setAutoDraw(True)
    
    # *c_end_x_2* updates
    if c_end_x_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        c_end_x_2.frameNStart = frameN  # exact frame index
        c_end_x_2.tStart = t  # local t and not account for scr refresh
        c_end_x_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(c_end_x_2, 'tStartRefresh')  # time at next scr refresh
        c_end_x_2.setAutoDraw(True)
    # *mouse_cal_end_2* updates
    if mouse_cal_end_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_cal_end_2.frameNStart = frameN  # exact frame index
        mouse_cal_end_2.tStart = t  # local t and not account for scr refresh
        mouse_cal_end_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_cal_end_2, 'tStartRefresh')  # time at next scr refresh
        mouse_cal_end_2.status = STARTED
        mouse_cal_end_2.mouseClock.reset()
        prevButtonState = mouse_cal_end_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse_cal_end_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse_cal_end_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [c_end_x]:
                    if obj.contains(mouse_cal_end_2):
                        gotValidClick = True
                        mouse_cal_end_2.clicked_name.append(obj.name)
                x, y = mouse_cal_end_2.getPos()
                mouse_cal_end_2.x.append(x)
                mouse_cal_end_2.y.append(y)
                buttons = mouse_cal_end_2.getPressed()
                mouse_cal_end_2.leftButton.append(buttons[0])
                mouse_cal_end_2.midButton.append(buttons[1])
                mouse_cal_end_2.rightButton.append(buttons[2])
                mouse_cal_end_2.time.append(mouse_cal_end_2.mouseClock.getTime())
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in screen_calibration_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "screen_calibration_end"-------
for thisComponent in screen_calibration_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('calibration_instructions_2.started', calibration_instructions_2.tStartRefresh)
thisExp.addData('calibration_instructions_2.stopped', calibration_instructions_2.tStopRefresh)
thisExp.addData('cal_line_2.started', cal_line_2.tStartRefresh)
thisExp.addData('cal_line_2.stopped', cal_line_2.tStopRefresh)
thisExp.addData('c_start_x_2.started', c_start_x_2.tStartRefresh)
thisExp.addData('c_start_x_2.stopped', c_start_x_2.tStopRefresh)
thisExp.addData('c_end_x_2.started', c_end_x_2.tStartRefresh)
thisExp.addData('c_end_x_2.stopped', c_end_x_2.tStopRefresh)
# store data for thisExp (ExperimentHandler)
if len(mouse_cal_end_2.x): thisExp.addData('mouse_cal_end_2.x', mouse_cal_end_2.x[0])
if len(mouse_cal_end_2.y): thisExp.addData('mouse_cal_end_2.y', mouse_cal_end_2.y[0])
if len(mouse_cal_end_2.leftButton): thisExp.addData('mouse_cal_end_2.leftButton', mouse_cal_end_2.leftButton[0])
if len(mouse_cal_end_2.midButton): thisExp.addData('mouse_cal_end_2.midButton', mouse_cal_end_2.midButton[0])
if len(mouse_cal_end_2.rightButton): thisExp.addData('mouse_cal_end_2.rightButton', mouse_cal_end_2.rightButton[0])
if len(mouse_cal_end_2.time): thisExp.addData('mouse_cal_end_2.time', mouse_cal_end_2.time[0])
if len(mouse_cal_end_2.clicked_name): thisExp.addData('mouse_cal_end_2.clicked_name', mouse_cal_end_2.clicked_name[0])
thisExp.addData('mouse_cal_end_2.started', mouse_cal_end_2.tStart)
thisExp.addData('mouse_cal_end_2.stopped', mouse_cal_end_2.tStop)
thisExp.nextEntry()
# the Routine "screen_calibration_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "screen_calibration_end_2"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
screen_calibration_end_2Components = [calibration_instructions_3, cal_line_3, c_start_x_3, c_end_x_3]
for thisComponent in screen_calibration_end_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
screen_calibration_end_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "screen_calibration_end_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = screen_calibration_end_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=screen_calibration_end_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *calibration_instructions_3* updates
    if calibration_instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        calibration_instructions_3.frameNStart = frameN  # exact frame index
        calibration_instructions_3.tStart = t  # local t and not account for scr refresh
        calibration_instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(calibration_instructions_3, 'tStartRefresh')  # time at next scr refresh
        calibration_instructions_3.setAutoDraw(True)
    if calibration_instructions_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > calibration_instructions_3.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            calibration_instructions_3.tStop = t  # not accounting for scr refresh
            calibration_instructions_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(calibration_instructions_3, 'tStopRefresh')  # time at next scr refresh
            calibration_instructions_3.setAutoDraw(False)
    
    # *cal_line_3* updates
    if cal_line_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cal_line_3.frameNStart = frameN  # exact frame index
        cal_line_3.tStart = t  # local t and not account for scr refresh
        cal_line_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cal_line_3, 'tStartRefresh')  # time at next scr refresh
        cal_line_3.setAutoDraw(True)
    if cal_line_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cal_line_3.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            cal_line_3.tStop = t  # not accounting for scr refresh
            cal_line_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(cal_line_3, 'tStopRefresh')  # time at next scr refresh
            cal_line_3.setAutoDraw(False)
    if cal_line_3.status == STARTED:  # only update if drawing
        cal_line_3.setPos((0,0), log=False)
        cal_line_3.setSize(400, log=False)
    
    # *c_start_x_3* updates
    if c_start_x_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        c_start_x_3.frameNStart = frameN  # exact frame index
        c_start_x_3.tStart = t  # local t and not account for scr refresh
        c_start_x_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(c_start_x_3, 'tStartRefresh')  # time at next scr refresh
        c_start_x_3.setAutoDraw(True)
    if c_start_x_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > c_start_x_3.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            c_start_x_3.tStop = t  # not accounting for scr refresh
            c_start_x_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(c_start_x_3, 'tStopRefresh')  # time at next scr refresh
            c_start_x_3.setAutoDraw(False)
    
    # *c_end_x_3* updates
    if c_end_x_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        c_end_x_3.frameNStart = frameN  # exact frame index
        c_end_x_3.tStart = t  # local t and not account for scr refresh
        c_end_x_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(c_end_x_3, 'tStartRefresh')  # time at next scr refresh
        c_end_x_3.setAutoDraw(True)
    if c_end_x_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > c_end_x_3.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            c_end_x_3.tStop = t  # not accounting for scr refresh
            c_end_x_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(c_end_x_3, 'tStopRefresh')  # time at next scr refresh
            c_end_x_3.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in screen_calibration_end_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "screen_calibration_end_2"-------
for thisComponent in screen_calibration_end_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('calibration_instructions_3.started', calibration_instructions_3.tStartRefresh)
thisExp.addData('calibration_instructions_3.stopped', calibration_instructions_3.tStopRefresh)
thisExp.addData('cal_line_3.started', cal_line_3.tStartRefresh)
thisExp.addData('cal_line_3.stopped', cal_line_3.tStopRefresh)
thisExp.addData('c_start_x_3.started', c_start_x_3.tStartRefresh)
thisExp.addData('c_start_x_3.stopped', c_start_x_3.tStopRefresh)
thisExp.addData('c_end_x_3.started', c_end_x_3.tStartRefresh)
thisExp.addData('c_end_x_3.stopped', c_end_x_3.tStopRefresh)

# ------Prepare to start Routine "candb_instructions"-------
continueRoutine = True
# update component parameters for each repeat
instructions_key_resp.keys = []
instructions_key_resp.rt = []
_instructions_key_resp_allKeys = []
# keep track of which components have finished
candb_instructionsComponents = [instruction_text, instructions_key_resp]
for thisComponent in candb_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
candb_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "candb_instructions"-------
while continueRoutine:
    # get current time
    t = candb_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=candb_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_text* updates
    if instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_text.frameNStart = frameN  # exact frame index
        instruction_text.tStart = t  # local t and not account for scr refresh
        instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_text, 'tStartRefresh')  # time at next scr refresh
        instruction_text.setAutoDraw(True)
    
    # *instructions_key_resp* updates
    waitOnFlip = False
    if instructions_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_key_resp.frameNStart = frameN  # exact frame index
        instructions_key_resp.tStart = t  # local t and not account for scr refresh
        instructions_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_key_resp, 'tStartRefresh')  # time at next scr refresh
        instructions_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructions_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructions_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructions_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = instructions_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _instructions_key_resp_allKeys.extend(theseKeys)
        if len(_instructions_key_resp_allKeys):
            instructions_key_resp.keys = _instructions_key_resp_allKeys[-1].name  # just the last key pressed
            instructions_key_resp.rt = _instructions_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in candb_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "candb_instructions"-------
for thisComponent in candb_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction_text.started', instruction_text.tStartRefresh)
thisExp.addData('instruction_text.stopped', instruction_text.tStopRefresh)
# check responses
if instructions_key_resp.keys in ['', [], None]:  # No response was made
    instructions_key_resp.keys = None
thisExp.addData('instructions_key_resp.keys',instructions_key_resp.keys)
if instructions_key_resp.keys != None:  # we had a response
    thisExp.addData('instructions_key_resp.rt', instructions_key_resp.rt)
thisExp.addData('instructions_key_resp.started', instructions_key_resp.tStartRefresh)
thisExp.addData('instructions_key_resp.stopped', instructions_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "candb_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Consent"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
ConsentComponents = [consent_loading]
for thisComponent in ConsentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ConsentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Consent"-------
while continueRoutine:
    # get current time
    t = ConsentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ConsentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *consent_loading* updates
    if consent_loading.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        consent_loading.frameNStart = frameN  # exact frame index
        consent_loading.tStart = t  # local t and not account for scr refresh
        consent_loading.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(consent_loading, 'tStartRefresh')  # time at next scr refresh
        consent_loading.setAutoDraw(True)
    continueRoutine = False;
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ConsentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Consent"-------
for thisComponent in ConsentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('consent_loading.started', consent_loading.tStartRefresh)
thisExp.addData('consent_loading.stopped', consent_loading.tStopRefresh)
# the Routine "Consent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice_instructions"-------
continueRoutine = True
# update component parameters for each repeat
instructions_key_resp_2.keys = []
instructions_key_resp_2.rt = []
_instructions_key_resp_2_allKeys = []
# keep track of which components have finished
practice_instructionsComponents = [instruction_text_3, instructions_key_resp_2]
for thisComponent in practice_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_instructions"-------
while continueRoutine:
    # get current time
    t = practice_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_text_3* updates
    if instruction_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_text_3.frameNStart = frameN  # exact frame index
        instruction_text_3.tStart = t  # local t and not account for scr refresh
        instruction_text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_text_3, 'tStartRefresh')  # time at next scr refresh
        instruction_text_3.setAutoDraw(True)
    
    # *instructions_key_resp_2* updates
    waitOnFlip = False
    if instructions_key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_key_resp_2.frameNStart = frameN  # exact frame index
        instructions_key_resp_2.tStart = t  # local t and not account for scr refresh
        instructions_key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_key_resp_2, 'tStartRefresh')  # time at next scr refresh
        instructions_key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructions_key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructions_key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructions_key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = instructions_key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _instructions_key_resp_2_allKeys.extend(theseKeys)
        if len(_instructions_key_resp_2_allKeys):
            instructions_key_resp_2.keys = _instructions_key_resp_2_allKeys[-1].name  # just the last key pressed
            instructions_key_resp_2.rt = _instructions_key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_instructions"-------
for thisComponent in practice_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruction_text_3.started', instruction_text_3.tStartRefresh)
thisExp.addData('instruction_text_3.stopped', instruction_text_3.tStopRefresh)
# check responses
if instructions_key_resp_2.keys in ['', [], None]:  # No response was made
    instructions_key_resp_2.keys = None
thisExp.addData('instructions_key_resp_2.keys',instructions_key_resp_2.keys)
if instructions_key_resp_2.keys != None:  # we had a response
    thisExp.addData('instructions_key_resp_2.rt', instructions_key_resp_2.rt)
thisExp.addData('instructions_key_resp_2.started', instructions_key_resp_2.tStartRefresh)
thisExp.addData('instructions_key_resp_2.stopped', instructions_key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "practice_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_loop = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('linetask_prac_conditions.csv'),
    seed=None, name='practice_loop')
thisExp.addLoop(practice_loop)  # add the loop to the experiment
thisPractice_loop = practice_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
if thisPractice_loop != None:
    for paramName in thisPractice_loop:
        exec('{} = thisPractice_loop[paramName]'.format(paramName))

for thisPractice_loop in practice_loop:
    currentLoop = practice_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
    if thisPractice_loop != None:
        for paramName in thisPractice_loop:
            exec('{} = thisPractice_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixationcrosses"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationcrossesComponents = [fixation_cross]
    for thisComponent in fixationcrossesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationcrossesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixationcrosses"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationcrossesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationcrossesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross* updates
        if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.tStart = t  # local t and not account for scr refresh
            fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(True)
        if fixation_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_cross.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_cross.tStop = t  # not accounting for scr refresh
                fixation_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_cross, 'tStopRefresh')  # time at next scr refresh
                fixation_cross.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationcrossesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixationcrosses"-------
    for thisComponent in fixationcrossesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_loop.addData('fixation_cross.started', fixation_cross.tStartRefresh)
    practice_loop.addData('fixation_cross.stopped', fixation_cross.tStopRefresh)
    trial_counter+=1; 
    
    # ------Prepare to start Routine "targetlines"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    targetlinesComponents = [targetline]
    for thisComponent in targetlinesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    targetlinesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "targetlines"-------
    while continueRoutine:
        # get current time
        t = targetlinesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=targetlinesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *targetline* updates
        if targetline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            targetline.frameNStart = frameN  # exact frame index
            targetline.tStart = t  # local t and not account for scr refresh
            targetline.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(targetline, 'tStartRefresh')  # time at next scr refresh
            targetline.setAutoDraw(True)
        if targetline.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > targetline.tStartRefresh + durations-frameTolerance:
                # keep track of stop time/frame for later
                targetline.tStop = t  # not accounting for scr refresh
                targetline.frameNStop = frameN  # exact frame index
                win.timeOnFlip(targetline, 'tStopRefresh')  # time at next scr refresh
                targetline.setAutoDraw(False)
        if targetline.status == STARTED:  # only update if drawing
            targetline.setPos((start+t*jitter,0), log=False)
            targetline.setSize(t*disp, log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in targetlinesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "targetlines"-------
    for thisComponent in targetlinesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_loop.addData('targetline.started', targetline.tStartRefresh)
    practice_loop.addData('targetline.stopped', targetline.tStopRefresh)
    # the Routine "targetlines" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "prompt"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    prompt_text.setText(display)
    # keep track of which components have finished
    promptComponents = [prompt_text]
    for thisComponent in promptComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    promptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "prompt"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = promptClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=promptClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prompt_text* updates
        if prompt_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            prompt_text.frameNStart = frameN  # exact frame index
            prompt_text.tStart = t  # local t and not account for scr refresh
            prompt_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prompt_text, 'tStartRefresh')  # time at next scr refresh
            prompt_text.setAutoDraw(True)
        if prompt_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prompt_text.tStartRefresh + .75-frameTolerance:
                # keep track of stop time/frame for later
                prompt_text.tStop = t  # not accounting for scr refresh
                prompt_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prompt_text, 'tStopRefresh')  # time at next scr refresh
                prompt_text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in promptComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prompt"-------
    for thisComponent in promptComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_loop.addData('prompt_text.started', prompt_text.tStartRefresh)
    practice_loop.addData('prompt_text.stopped', prompt_text.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    loop_spatial = data.TrialHandler(nReps=spatial, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loop_spatial')
    thisExp.addLoop(loop_spatial)  # add the loop to the experiment
    thisLoop_spatial = loop_spatial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_spatial.rgb)
    if thisLoop_spatial != None:
        for paramName in thisLoop_spatial:
            exec('{} = thisLoop_spatial[paramName]'.format(paramName))
    
    for thisLoop_spatial in loop_spatial:
        currentLoop = loop_spatial
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_spatial.rgb)
        if thisLoop_spatial != None:
            for paramName in thisLoop_spatial:
                exec('{} = thisLoop_spatial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "start_x"-------
        continueRoutine = True
        # update component parameters for each repeat
        startx.setPos(x_loc)
        startx.setFillColor([1.000,1.000,1.000])
        startx.setLineColor([-1.000,-1.000,-1.000])
        # setup some python lists for storing info about the mouse_startx
        mouse_startx.x = []
        mouse_startx.y = []
        mouse_startx.leftButton = []
        mouse_startx.midButton = []
        mouse_startx.rightButton = []
        mouse_startx.time = []
        mouse_startx.clicked_name = []
        gotValidClick = False  # until a click is received
        
        
        
        # keep track of which components have finished
        start_xComponents = [startx, mouse_startx]
        for thisComponent in start_xComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        start_xClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "start_x"-------
        while continueRoutine:
            # get current time
            t = start_xClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=start_xClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *startx* updates
            if startx.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                startx.frameNStart = frameN  # exact frame index
                startx.tStart = t  # local t and not account for scr refresh
                startx.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(startx, 'tStartRefresh')  # time at next scr refresh
                startx.setAutoDraw(True)
            # *mouse_startx* updates
            if mouse_startx.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_startx.frameNStart = frameN  # exact frame index
                mouse_startx.tStart = t  # local t and not account for scr refresh
                mouse_startx.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_startx, 'tStartRefresh')  # time at next scr refresh
                mouse_startx.status = STARTED
                mouse_startx.mouseClock.reset()
                prevButtonState = mouse_startx.getPressed()  # if button is down already this ISN'T a new click
            if mouse_startx.status == STARTED:  # only update if started and not finished!
                buttons = mouse_startx.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [startx]:
                            if obj.contains(mouse_startx):
                                gotValidClick = True
                                mouse_startx.clicked_name.append(obj.name)
                        x, y = mouse_startx.getPos()
                        mouse_startx.x.append(x)
                        mouse_startx.y.append(y)
                        buttons = mouse_startx.getPressed()
                        mouse_startx.leftButton.append(buttons[0])
                        mouse_startx.midButton.append(buttons[1])
                        mouse_startx.rightButton.append(buttons[2])
                        mouse_startx.time.append(mouse_startx.mouseClock.getTime())
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_xComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "start_x"-------
        for thisComponent in start_xComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_spatial.addData('startx.started', startx.tStartRefresh)
        loop_spatial.addData('startx.stopped', startx.tStopRefresh)
        # store data for loop_spatial (TrialHandler)
        if len(mouse_startx.x): loop_spatial.addData('mouse_startx.x', mouse_startx.x[0])
        if len(mouse_startx.y): loop_spatial.addData('mouse_startx.y', mouse_startx.y[0])
        if len(mouse_startx.leftButton): loop_spatial.addData('mouse_startx.leftButton', mouse_startx.leftButton[0])
        if len(mouse_startx.midButton): loop_spatial.addData('mouse_startx.midButton', mouse_startx.midButton[0])
        if len(mouse_startx.rightButton): loop_spatial.addData('mouse_startx.rightButton', mouse_startx.rightButton[0])
        if len(mouse_startx.time): loop_spatial.addData('mouse_startx.time', mouse_startx.time[0])
        if len(mouse_startx.clicked_name): loop_spatial.addData('mouse_startx.clicked_name', mouse_startx.clicked_name[0])
        loop_spatial.addData('mouse_startx.started', mouse_startx.tStartRefresh)
        loop_spatial.addData('mouse_startx.stopped', mouse_startx.tStopRefresh)
        # the Routine "start_x" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "end_x"-------
        continueRoutine = True
        # update component parameters for each repeat
        startx_ph.setPos(x_loc)
        startx_ph.setFillColor([-1.000,-1.000,-1.000])
        startx_ph.setLineColor([-1.000,-1.000,-1.000])
        polygon.setPos(box_loc)
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        crosses = [] ;
        
        
        # keep track of which components have finished
        end_xComponents = [startx_ph, polygon, mouse]
        for thisComponent in end_xComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        end_xClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "end_x"-------
        while continueRoutine:
            # get current time
            t = end_xClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=end_xClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *startx_ph* updates
            if startx_ph.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                startx_ph.frameNStart = frameN  # exact frame index
                startx_ph.tStart = t  # local t and not account for scr refresh
                startx_ph.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(startx_ph, 'tStartRefresh')  # time at next scr refresh
                startx_ph.setAutoDraw(True)
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                polygon.setAutoDraw(True)
            # *mouse* updates
            if mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [polygon]:
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            if mouse.isPressedIn(polygon):
                cross = visual.ShapeStim(win, pos=clicker.getPos(), vertices='cross', depth=-2, size=(50,50), ori=45.0, fillColor="black")
                cross.setAutoDraw(True)
                crosses.append()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_xComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "end_x"-------
        for thisComponent in end_xComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_spatial.addData('startx_ph.started', startx_ph.tStartRefresh)
        loop_spatial.addData('startx_ph.stopped', startx_ph.tStopRefresh)
        loop_spatial.addData('polygon.started', polygon.tStartRefresh)
        loop_spatial.addData('polygon.stopped', polygon.tStopRefresh)
        # store data for loop_spatial (TrialHandler)
        if len(mouse.x): loop_spatial.addData('mouse.x', mouse.x[0])
        if len(mouse.y): loop_spatial.addData('mouse.y', mouse.y[0])
        if len(mouse.leftButton): loop_spatial.addData('mouse.leftButton', mouse.leftButton[0])
        if len(mouse.midButton): loop_spatial.addData('mouse.midButton', mouse.midButton[0])
        if len(mouse.rightButton): loop_spatial.addData('mouse.rightButton', mouse.rightButton[0])
        if len(mouse.time): loop_spatial.addData('mouse.time', mouse.time[0])
        if len(mouse.clicked_name): loop_spatial.addData('mouse.clicked_name', mouse.clicked_name[0])
        loop_spatial.addData('mouse.started', mouse.tStartRefresh)
        loop_spatial.addData('mouse.stopped', mouse.tStopRefresh)
        # the Routine "end_x" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "pause"-------
        continueRoutine = True
        routineTimer.add(0.750000)
        # update component parameters for each repeat
        
        
        
        startx_4.setPos(x_loc)
        startx_4.setFillColor([-1.000,-1.000,-1.000])
        startx_4.setLineColor([-1.000,-1.000,-1.000])
        # keep track of which components have finished
        pauseComponents = [startx_4]
        for thisComponent in pauseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "pause"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = pauseClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=pauseClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *startx_4* updates
            if startx_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                startx_4.frameNStart = frameN  # exact frame index
                startx_4.tStart = t  # local t and not account for scr refresh
                startx_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(startx_4, 'tStartRefresh')  # time at next scr refresh
                startx_4.setAutoDraw(True)
            if startx_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > startx_4.tStartRefresh + .75-frameTolerance:
                    # keep track of stop time/frame for later
                    startx_4.tStop = t  # not accounting for scr refresh
                    startx_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(startx_4, 'tStopRefresh')  # time at next scr refresh
                    startx_4.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pauseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "pause"-------
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        for across in crosses:
                across.setAutoDraw(False)
        loop_spatial.addData('startx_4.started', startx_4.tStartRefresh)
        loop_spatial.addData('startx_4.stopped', startx_4.tStopRefresh)
        thisExp.nextEntry()
        
    # completed spatial repeats of 'loop_spatial'
    
    
    # set up handler to look after randomisation of conditions etc
    loop_temporal = data.TrialHandler(nReps=temporal, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loop_temporal')
    thisExp.addLoop(loop_temporal)  # add the loop to the experiment
    thisLoop_temporal = loop_temporal.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_temporal.rgb)
    if thisLoop_temporal != None:
        for paramName in thisLoop_temporal:
            exec('{} = thisLoop_temporal[paramName]'.format(paramName))
    
    for thisLoop_temporal in loop_temporal:
        currentLoop = loop_temporal
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_temporal.rgb)
        if thisLoop_temporal != None:
            for paramName in thisLoop_temporal:
                exec('{} = thisLoop_temporal[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "hg_start"-------
        continueRoutine = True
        # update component parameters for each repeat
        hg_bottom.setPos(bottom_hg_loc)
        hg_bottom.setFillColor([0.004,0.004,0.004])
        hg_bottom.setLineColor([0.004,0.004,0.004])
        # setup some python lists for storing info about the mouse_hg
        mouse_hg.clicked_name = []
        gotValidClick = False  # until a click is received
        hg_top.setPos(top_hg_loc)
        hg_top.setFillColor([0.004,0.004,0.004])
        hg_top.setLineColor([0.004,0.004,0.004])
        # keep track of which components have finished
        hg_startComponents = [hg_bottom, mouse_hg, hg_top]
        for thisComponent in hg_startComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        hg_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "hg_start"-------
        while continueRoutine:
            # get current time
            t = hg_startClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=hg_startClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *hg_bottom* updates
            if hg_bottom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hg_bottom.frameNStart = frameN  # exact frame index
                hg_bottom.tStart = t  # local t and not account for scr refresh
                hg_bottom.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hg_bottom, 'tStartRefresh')  # time at next scr refresh
                hg_bottom.setAutoDraw(True)
            # *mouse_hg* updates
            if mouse_hg.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_hg.frameNStart = frameN  # exact frame index
                mouse_hg.tStart = t  # local t and not account for scr refresh
                mouse_hg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_hg, 'tStartRefresh')  # time at next scr refresh
                mouse_hg.status = STARTED
                mouse_hg.mouseClock.reset()
                prevButtonState = mouse_hg.getPressed()  # if button is down already this ISN'T a new click
            if mouse_hg.status == STARTED:  # only update if started and not finished!
                buttons = mouse_hg.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [hg_bottom, hg_top]:
                            if obj.contains(mouse_hg):
                                gotValidClick = True
                                mouse_hg.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *hg_top* updates
            if hg_top.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hg_top.frameNStart = frameN  # exact frame index
                hg_top.tStart = t  # local t and not account for scr refresh
                hg_top.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hg_top, 'tStartRefresh')  # time at next scr refresh
                hg_top.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in hg_startComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "hg_start"-------
        for thisComponent in hg_startComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_temporal.addData('hg_bottom.started', hg_bottom.tStartRefresh)
        loop_temporal.addData('hg_bottom.stopped', hg_bottom.tStopRefresh)
        # store data for loop_temporal (TrialHandler)
        x, y = mouse_hg.getPos()
        buttons = mouse_hg.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [hg_bottom, hg_top]:
                if obj.contains(mouse_hg):
                    gotValidClick = True
                    mouse_hg.clicked_name.append(obj.name)
        loop_temporal.addData('mouse_hg.x', x)
        loop_temporal.addData('mouse_hg.y', y)
        loop_temporal.addData('mouse_hg.leftButton', buttons[0])
        loop_temporal.addData('mouse_hg.midButton', buttons[1])
        loop_temporal.addData('mouse_hg.rightButton', buttons[2])
        if len(mouse_hg.clicked_name):
            loop_temporal.addData('mouse_hg.clicked_name', mouse_hg.clicked_name[0])
        loop_temporal.addData('mouse_hg.started', mouse_hg.tStart)
        loop_temporal.addData('mouse_hg.stopped', mouse_hg.tStop)
        loop_temporal.addData('hg_top.started', hg_top.tStartRefresh)
        loop_temporal.addData('hg_top.stopped', hg_top.tStopRefresh)
        # the Routine "hg_start" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "hg_mid"-------
        continueRoutine = True
        # update component parameters for each repeat
        hg_bottom_2.setPos(bottom_hg_loc)
        hg_bottom_2.setFillColor([-1.000,-1.000,-1.000])
        hg_bottom_2.setLineColor([-1.000,-1.000,-1.000])
        # setup some python lists for storing info about the mouse_hg_2
        mouse_hg_2.clicked_name = []
        gotValidClick = False  # until a click is received
        hg_top_2.setPos(top_hg_loc)
        hg_top_2.setFillColor([-1.000,-1.000,-1.000])
        hg_top_2.setLineColor([-1.000,-1.000,-1.000])
        # keep track of which components have finished
        hg_midComponents = [hg_bottom_2, mouse_hg_2, hg_top_2]
        for thisComponent in hg_midComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        hg_midClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "hg_mid"-------
        while continueRoutine:
            # get current time
            t = hg_midClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=hg_midClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *hg_bottom_2* updates
            if hg_bottom_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hg_bottom_2.frameNStart = frameN  # exact frame index
                hg_bottom_2.tStart = t  # local t and not account for scr refresh
                hg_bottom_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hg_bottom_2, 'tStartRefresh')  # time at next scr refresh
                hg_bottom_2.setAutoDraw(True)
            # *mouse_hg_2* updates
            if mouse_hg_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_hg_2.frameNStart = frameN  # exact frame index
                mouse_hg_2.tStart = t  # local t and not account for scr refresh
                mouse_hg_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_hg_2, 'tStartRefresh')  # time at next scr refresh
                mouse_hg_2.status = STARTED
                mouse_hg_2.mouseClock.reset()
                prevButtonState = mouse_hg_2.getPressed()  # if button is down already this ISN'T a new click
            if mouse_hg_2.status == STARTED:  # only update if started and not finished!
                buttons = mouse_hg_2.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [hg_bottom_2, hg_top_2]:
                            if obj.contains(mouse_hg_2):
                                gotValidClick = True
                                mouse_hg_2.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *hg_top_2* updates
            if hg_top_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hg_top_2.frameNStart = frameN  # exact frame index
                hg_top_2.tStart = t  # local t and not account for scr refresh
                hg_top_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hg_top_2, 'tStartRefresh')  # time at next scr refresh
                hg_top_2.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in hg_midComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "hg_mid"-------
        for thisComponent in hg_midComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_temporal.addData('hg_bottom_2.started', hg_bottom_2.tStartRefresh)
        loop_temporal.addData('hg_bottom_2.stopped', hg_bottom_2.tStopRefresh)
        # store data for loop_temporal (TrialHandler)
        x, y = mouse_hg_2.getPos()
        buttons = mouse_hg_2.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [hg_bottom_2, hg_top_2]:
                if obj.contains(mouse_hg_2):
                    gotValidClick = True
                    mouse_hg_2.clicked_name.append(obj.name)
        loop_temporal.addData('mouse_hg_2.x', x)
        loop_temporal.addData('mouse_hg_2.y', y)
        loop_temporal.addData('mouse_hg_2.leftButton', buttons[0])
        loop_temporal.addData('mouse_hg_2.midButton', buttons[1])
        loop_temporal.addData('mouse_hg_2.rightButton', buttons[2])
        if len(mouse_hg_2.clicked_name):
            loop_temporal.addData('mouse_hg_2.clicked_name', mouse_hg_2.clicked_name[0])
        loop_temporal.addData('mouse_hg_2.started', mouse_hg_2.tStart)
        loop_temporal.addData('mouse_hg_2.stopped', mouse_hg_2.tStop)
        loop_temporal.addData('hg_top_2.started', hg_top_2.tStartRefresh)
        loop_temporal.addData('hg_top_2.stopped', hg_top_2.tStopRefresh)
        # the Routine "hg_mid" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "hg_end"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        hg_bottom_3.setPos(bottom_hg_loc)
        hg_bottom_3.setFillColor([0.004,0.004,0.004])
        hg_bottom_3.setLineColor([0.004,0.004,0.004])
        hg_top_3.setPos(top_hg_loc)
        hg_top_3.setFillColor([0.004,0.004,0.004])
        hg_top_3.setLineColor([0.004,0.004,0.004])
        # keep track of which components have finished
        hg_endComponents = [hg_bottom_3, hg_top_3]
        for thisComponent in hg_endComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        hg_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "hg_end"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = hg_endClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=hg_endClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *hg_bottom_3* updates
            if hg_bottom_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hg_bottom_3.frameNStart = frameN  # exact frame index
                hg_bottom_3.tStart = t  # local t and not account for scr refresh
                hg_bottom_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hg_bottom_3, 'tStartRefresh')  # time at next scr refresh
                hg_bottom_3.setAutoDraw(True)
            if hg_bottom_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > hg_bottom_3.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    hg_bottom_3.tStop = t  # not accounting for scr refresh
                    hg_bottom_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(hg_bottom_3, 'tStopRefresh')  # time at next scr refresh
                    hg_bottom_3.setAutoDraw(False)
            
            # *hg_top_3* updates
            if hg_top_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hg_top_3.frameNStart = frameN  # exact frame index
                hg_top_3.tStart = t  # local t and not account for scr refresh
                hg_top_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hg_top_3, 'tStartRefresh')  # time at next scr refresh
                hg_top_3.setAutoDraw(True)
            if hg_top_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > hg_top_3.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    hg_top_3.tStop = t  # not accounting for scr refresh
                    hg_top_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(hg_top_3, 'tStopRefresh')  # time at next scr refresh
                    hg_top_3.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in hg_endComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "hg_end"-------
        for thisComponent in hg_endComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_temporal.addData('hg_bottom_3.started', hg_bottom_3.tStartRefresh)
        loop_temporal.addData('hg_bottom_3.stopped', hg_bottom_3.tStopRefresh)
        loop_temporal.addData('hg_top_3.started', hg_top_3.tStartRefresh)
        loop_temporal.addData('hg_top_3.stopped', hg_top_3.tStopRefresh)
        thisExp.nextEntry()
        
    # completed temporal repeats of 'loop_temporal'
    
    
    # ------Prepare to start Routine "ready"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    readyComponents = [text, instruction_req, key_resp]
    for thisComponent in readyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    readyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ready"-------
    while continueRoutine:
        # get current time
        t = readyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=readyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *instruction_req* updates
        if instruction_req.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_req.frameNStart = frameN  # exact frame index
            instruction_req.tStart = t  # local t and not account for scr refresh
            instruction_req.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_req, 'tStartRefresh')  # time at next scr refresh
            instruction_req.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space', 'i', 't'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in readyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ready"-------
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_loop.addData('text.started', text.tStartRefresh)
    practice_loop.addData('text.stopped', text.tStopRefresh)
    practice_loop.addData('instruction_req.started', instruction_req.tStartRefresh)
    practice_loop.addData('instruction_req.stopped', instruction_req.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    practice_loop.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        practice_loop.addData('key_resp.rt', key_resp.rt)
    practice_loop.addData('key_resp.started', key_resp.tStartRefresh)
    practice_loop.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "ready" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "reminder"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    reminderComponents = [text_4, key_resp_6]
    for thisComponent in reminderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    reminderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "reminder"-------
    while continueRoutine:
        # get current time
        t = reminderClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=reminderClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        
        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        if trial_counter != 2:
            continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reminderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "reminder"-------
    for thisComponent in reminderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_loop.addData('text_4.started', text_4.tStartRefresh)
    practice_loop.addData('text_4.stopped', text_4.tStopRefresh)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    practice_loop.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        practice_loop.addData('key_resp_6.rt', key_resp_6.rt)
    practice_loop.addData('key_resp_6.started', key_resp_6.tStartRefresh)
    practice_loop.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
    # the Routine "reminder" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "troubleshooting"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_11.keys = []
    key_resp_11.rt = []
    _key_resp_11_allKeys = []
    # keep track of which components have finished
    troubleshootingComponents = [troubleshooting_text, key_resp_11]
    for thisComponent in troubleshootingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    troubleshootingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "troubleshooting"-------
    while continueRoutine:
        # get current time
        t = troubleshootingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=troubleshootingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *troubleshooting_text* updates
        if troubleshooting_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            troubleshooting_text.frameNStart = frameN  # exact frame index
            troubleshooting_text.tStart = t  # local t and not account for scr refresh
            troubleshooting_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(troubleshooting_text, 'tStartRefresh')  # time at next scr refresh
            troubleshooting_text.setAutoDraw(True)
        if key_resp.keys[0] != 't':
            continueRoutine = False # don't even start this routine
        
        
        # *key_resp_11* updates
        waitOnFlip = False
        if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.tStart = t  # local t and not account for scr refresh
            key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_11.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_11_allKeys.extend(theseKeys)
            if len(_key_resp_11_allKeys):
                key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in troubleshootingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "troubleshooting"-------
    for thisComponent in troubleshootingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_loop.addData('troubleshooting_text.started', troubleshooting_text.tStartRefresh)
    practice_loop.addData('troubleshooting_text.stopped', troubleshooting_text.tStopRefresh)
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
        key_resp_11.keys = None
    practice_loop.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        practice_loop.addData('key_resp_11.rt', key_resp_11.rt)
    practice_loop.addData('key_resp_11.started', key_resp_11.tStartRefresh)
    practice_loop.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
    # the Routine "troubleshooting" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "request_inst"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_9.keys = []
    key_resp_9.rt = []
    _key_resp_9_allKeys = []
    # keep track of which components have finished
    request_instComponents = [instruction_re_text, key_resp_9]
    for thisComponent in request_instComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    request_instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "request_inst"-------
    while continueRoutine:
        # get current time
        t = request_instClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=request_instClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_re_text* updates
        if instruction_re_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_re_text.frameNStart = frameN  # exact frame index
            instruction_re_text.tStart = t  # local t and not account for scr refresh
            instruction_re_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_re_text, 'tStartRefresh')  # time at next scr refresh
            instruction_re_text.setAutoDraw(True)
        if key_resp.keys[0] != 'i':
            continueRoutine = False # don't even start this routine
        
        
        # *key_resp_9* updates
        waitOnFlip = False
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.tStart = t  # local t and not account for scr refresh
            key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_9_allKeys.extend(theseKeys)
            if len(_key_resp_9_allKeys):
                key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in request_instComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "request_inst"-------
    for thisComponent in request_instComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_loop.addData('instruction_re_text.started', instruction_re_text.tStartRefresh)
    practice_loop.addData('instruction_re_text.stopped', instruction_re_text.tStopRefresh)
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
    practice_loop.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        practice_loop.addData('key_resp_9.rt', key_resp_9.rt)
    practice_loop.addData('key_resp_9.started', key_resp_9.tStartRefresh)
    practice_loop.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
    # the Routine "request_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'practice_loop'


# ------Prepare to start Routine "practicetrialendscreen"-------
continueRoutine = True
# update component parameters for each repeat
practicetrialend_key_resp.keys = []
practicetrialend_key_resp.rt = []
_practicetrialend_key_resp_allKeys = []
# keep track of which components have finished
practicetrialendscreenComponents = [practicetrialend_text, practicetrialend_key_resp]
for thisComponent in practicetrialendscreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practicetrialendscreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practicetrialendscreen"-------
while continueRoutine:
    # get current time
    t = practicetrialendscreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practicetrialendscreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practicetrialend_text* updates
    if practicetrialend_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practicetrialend_text.frameNStart = frameN  # exact frame index
        practicetrialend_text.tStart = t  # local t and not account for scr refresh
        practicetrialend_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practicetrialend_text, 'tStartRefresh')  # time at next scr refresh
        practicetrialend_text.setAutoDraw(True)
    
    # *practicetrialend_key_resp* updates
    waitOnFlip = False
    if practicetrialend_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practicetrialend_key_resp.frameNStart = frameN  # exact frame index
        practicetrialend_key_resp.tStart = t  # local t and not account for scr refresh
        practicetrialend_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practicetrialend_key_resp, 'tStartRefresh')  # time at next scr refresh
        practicetrialend_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(practicetrialend_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(practicetrialend_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practicetrialend_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = practicetrialend_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _practicetrialend_key_resp_allKeys.extend(theseKeys)
        if len(_practicetrialend_key_resp_allKeys):
            practicetrialend_key_resp.keys = _practicetrialend_key_resp_allKeys[-1].name  # just the last key pressed
            practicetrialend_key_resp.rt = _practicetrialend_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practicetrialendscreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practicetrialendscreen"-------
for thisComponent in practicetrialendscreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practicetrialend_text.started', practicetrialend_text.tStartRefresh)
thisExp.addData('practicetrialend_text.stopped', practicetrialend_text.tStopRefresh)
# check responses
if practicetrialend_key_resp.keys in ['', [], None]:  # No response was made
    practicetrialend_key_resp.keys = None
thisExp.addData('practicetrialend_key_resp.keys',practicetrialend_key_resp.keys)
if practicetrialend_key_resp.keys != None:  # we had a response
    thisExp.addData('practicetrialend_key_resp.rt', practicetrialend_key_resp.rt)
thisExp.addData('practicetrialend_key_resp.started', practicetrialend_key_resp.tStartRefresh)
thisExp.addData('practicetrialend_key_resp.stopped', practicetrialend_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "practicetrialendscreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
exp_loop = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('linetask_full_conditions.csv'),
    seed=None, name='exp_loop')
thisExp.addLoop(exp_loop)  # add the loop to the experiment
thisExp_loop = exp_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExp_loop.rgb)
if thisExp_loop != None:
    for paramName in thisExp_loop:
        exec('{} = thisExp_loop[paramName]'.format(paramName))

for thisExp_loop in exp_loop:
    currentLoop = exp_loop
    # abbreviate parameter names if possible (e.g. rgb = thisExp_loop.rgb)
    if thisExp_loop != None:
        for paramName in thisExp_loop:
            exec('{} = thisExp_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixationcrosses"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationcrossesComponents = [fixation_cross]
    for thisComponent in fixationcrossesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationcrossesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixationcrosses"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationcrossesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationcrossesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross* updates
        if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.tStart = t  # local t and not account for scr refresh
            fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(True)
        if fixation_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_cross.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_cross.tStop = t  # not accounting for scr refresh
                fixation_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_cross, 'tStopRefresh')  # time at next scr refresh
                fixation_cross.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationcrossesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixationcrosses"-------
    for thisComponent in fixationcrossesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    exp_loop.addData('fixation_cross.started', fixation_cross.tStartRefresh)
    exp_loop.addData('fixation_cross.stopped', fixation_cross.tStopRefresh)
    trial_counter+=1; 
    
    # ------Prepare to start Routine "targetlines"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    targetlinesComponents = [targetline]
    for thisComponent in targetlinesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    targetlinesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "targetlines"-------
    while continueRoutine:
        # get current time
        t = targetlinesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=targetlinesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *targetline* updates
        if targetline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            targetline.frameNStart = frameN  # exact frame index
            targetline.tStart = t  # local t and not account for scr refresh
            targetline.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(targetline, 'tStartRefresh')  # time at next scr refresh
            targetline.setAutoDraw(True)
        if targetline.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > targetline.tStartRefresh + durations-frameTolerance:
                # keep track of stop time/frame for later
                targetline.tStop = t  # not accounting for scr refresh
                targetline.frameNStop = frameN  # exact frame index
                win.timeOnFlip(targetline, 'tStopRefresh')  # time at next scr refresh
                targetline.setAutoDraw(False)
        if targetline.status == STARTED:  # only update if drawing
            targetline.setPos((start+t*jitter,0), log=False)
            targetline.setSize(t*disp, log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in targetlinesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "targetlines"-------
    for thisComponent in targetlinesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    exp_loop.addData('targetline.started', targetline.tStartRefresh)
    exp_loop.addData('targetline.stopped', targetline.tStopRefresh)
    # the Routine "targetlines" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "prompt"-------
    continueRoutine = True
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    prompt_text.setText(display)
    # keep track of which components have finished
    promptComponents = [prompt_text]
    for thisComponent in promptComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    promptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "prompt"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = promptClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=promptClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prompt_text* updates
        if prompt_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            prompt_text.frameNStart = frameN  # exact frame index
            prompt_text.tStart = t  # local t and not account for scr refresh
            prompt_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prompt_text, 'tStartRefresh')  # time at next scr refresh
            prompt_text.setAutoDraw(True)
        if prompt_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prompt_text.tStartRefresh + .75-frameTolerance:
                # keep track of stop time/frame for later
                prompt_text.tStop = t  # not accounting for scr refresh
                prompt_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prompt_text, 'tStopRefresh')  # time at next scr refresh
                prompt_text.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in promptComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prompt"-------
    for thisComponent in promptComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    exp_loop.addData('prompt_text.started', prompt_text.tStartRefresh)
    exp_loop.addData('prompt_text.stopped', prompt_text.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    loop_spatial_exp = data.TrialHandler(nReps=spatial, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loop_spatial_exp')
    thisExp.addLoop(loop_spatial_exp)  # add the loop to the experiment
    thisLoop_spatial_exp = loop_spatial_exp.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_spatial_exp.rgb)
    if thisLoop_spatial_exp != None:
        for paramName in thisLoop_spatial_exp:
            exec('{} = thisLoop_spatial_exp[paramName]'.format(paramName))
    
    for thisLoop_spatial_exp in loop_spatial_exp:
        currentLoop = loop_spatial_exp
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_spatial_exp.rgb)
        if thisLoop_spatial_exp != None:
            for paramName in thisLoop_spatial_exp:
                exec('{} = thisLoop_spatial_exp[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "start_x"-------
        continueRoutine = True
        # update component parameters for each repeat
        startx.setPos(x_loc)
        startx.setFillColor([1.000,1.000,1.000])
        startx.setLineColor([-1.000,-1.000,-1.000])
        # setup some python lists for storing info about the mouse_startx
        mouse_startx.x = []
        mouse_startx.y = []
        mouse_startx.leftButton = []
        mouse_startx.midButton = []
        mouse_startx.rightButton = []
        mouse_startx.time = []
        mouse_startx.clicked_name = []
        gotValidClick = False  # until a click is received
        
        
        
        # keep track of which components have finished
        start_xComponents = [startx, mouse_startx]
        for thisComponent in start_xComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        start_xClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "start_x"-------
        while continueRoutine:
            # get current time
            t = start_xClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=start_xClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *startx* updates
            if startx.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                startx.frameNStart = frameN  # exact frame index
                startx.tStart = t  # local t and not account for scr refresh
                startx.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(startx, 'tStartRefresh')  # time at next scr refresh
                startx.setAutoDraw(True)
            # *mouse_startx* updates
            if mouse_startx.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_startx.frameNStart = frameN  # exact frame index
                mouse_startx.tStart = t  # local t and not account for scr refresh
                mouse_startx.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_startx, 'tStartRefresh')  # time at next scr refresh
                mouse_startx.status = STARTED
                mouse_startx.mouseClock.reset()
                prevButtonState = mouse_startx.getPressed()  # if button is down already this ISN'T a new click
            if mouse_startx.status == STARTED:  # only update if started and not finished!
                buttons = mouse_startx.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [startx]:
                            if obj.contains(mouse_startx):
                                gotValidClick = True
                                mouse_startx.clicked_name.append(obj.name)
                        x, y = mouse_startx.getPos()
                        mouse_startx.x.append(x)
                        mouse_startx.y.append(y)
                        buttons = mouse_startx.getPressed()
                        mouse_startx.leftButton.append(buttons[0])
                        mouse_startx.midButton.append(buttons[1])
                        mouse_startx.rightButton.append(buttons[2])
                        mouse_startx.time.append(mouse_startx.mouseClock.getTime())
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in start_xComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "start_x"-------
        for thisComponent in start_xComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_spatial_exp.addData('startx.started', startx.tStartRefresh)
        loop_spatial_exp.addData('startx.stopped', startx.tStopRefresh)
        # store data for loop_spatial_exp (TrialHandler)
        if len(mouse_startx.x): loop_spatial_exp.addData('mouse_startx.x', mouse_startx.x[0])
        if len(mouse_startx.y): loop_spatial_exp.addData('mouse_startx.y', mouse_startx.y[0])
        if len(mouse_startx.leftButton): loop_spatial_exp.addData('mouse_startx.leftButton', mouse_startx.leftButton[0])
        if len(mouse_startx.midButton): loop_spatial_exp.addData('mouse_startx.midButton', mouse_startx.midButton[0])
        if len(mouse_startx.rightButton): loop_spatial_exp.addData('mouse_startx.rightButton', mouse_startx.rightButton[0])
        if len(mouse_startx.time): loop_spatial_exp.addData('mouse_startx.time', mouse_startx.time[0])
        if len(mouse_startx.clicked_name): loop_spatial_exp.addData('mouse_startx.clicked_name', mouse_startx.clicked_name[0])
        loop_spatial_exp.addData('mouse_startx.started', mouse_startx.tStartRefresh)
        loop_spatial_exp.addData('mouse_startx.stopped', mouse_startx.tStopRefresh)
        # the Routine "start_x" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "end_x"-------
        continueRoutine = True
        # update component parameters for each repeat
        startx_ph.setPos(x_loc)
        startx_ph.setFillColor([-1.000,-1.000,-1.000])
        startx_ph.setLineColor([-1.000,-1.000,-1.000])
        polygon.setPos(box_loc)
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        crosses = [] ;
        
        
        # keep track of which components have finished
        end_xComponents = [startx_ph, polygon, mouse]
        for thisComponent in end_xComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        end_xClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "end_x"-------
        while continueRoutine:
            # get current time
            t = end_xClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=end_xClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *startx_ph* updates
            if startx_ph.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                startx_ph.frameNStart = frameN  # exact frame index
                startx_ph.tStart = t  # local t and not account for scr refresh
                startx_ph.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(startx_ph, 'tStartRefresh')  # time at next scr refresh
                startx_ph.setAutoDraw(True)
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                polygon.setAutoDraw(True)
            # *mouse* updates
            if mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [polygon]:
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            if mouse.isPressedIn(polygon):
                cross = visual.ShapeStim(win, pos=clicker.getPos(), vertices='cross', depth=-2, size=(50,50), ori=45.0, fillColor="black")
                cross.setAutoDraw(True)
                crosses.append()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in end_xComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "end_x"-------
        for thisComponent in end_xComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_spatial_exp.addData('startx_ph.started', startx_ph.tStartRefresh)
        loop_spatial_exp.addData('startx_ph.stopped', startx_ph.tStopRefresh)
        loop_spatial_exp.addData('polygon.started', polygon.tStartRefresh)
        loop_spatial_exp.addData('polygon.stopped', polygon.tStopRefresh)
        # store data for loop_spatial_exp (TrialHandler)
        if len(mouse.x): loop_spatial_exp.addData('mouse.x', mouse.x[0])
        if len(mouse.y): loop_spatial_exp.addData('mouse.y', mouse.y[0])
        if len(mouse.leftButton): loop_spatial_exp.addData('mouse.leftButton', mouse.leftButton[0])
        if len(mouse.midButton): loop_spatial_exp.addData('mouse.midButton', mouse.midButton[0])
        if len(mouse.rightButton): loop_spatial_exp.addData('mouse.rightButton', mouse.rightButton[0])
        if len(mouse.time): loop_spatial_exp.addData('mouse.time', mouse.time[0])
        if len(mouse.clicked_name): loop_spatial_exp.addData('mouse.clicked_name', mouse.clicked_name[0])
        loop_spatial_exp.addData('mouse.started', mouse.tStartRefresh)
        loop_spatial_exp.addData('mouse.stopped', mouse.tStopRefresh)
        # the Routine "end_x" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "pause"-------
        continueRoutine = True
        routineTimer.add(0.750000)
        # update component parameters for each repeat
        
        
        
        startx_4.setPos(x_loc)
        startx_4.setFillColor([-1.000,-1.000,-1.000])
        startx_4.setLineColor([-1.000,-1.000,-1.000])
        # keep track of which components have finished
        pauseComponents = [startx_4]
        for thisComponent in pauseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "pause"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = pauseClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=pauseClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *startx_4* updates
            if startx_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                startx_4.frameNStart = frameN  # exact frame index
                startx_4.tStart = t  # local t and not account for scr refresh
                startx_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(startx_4, 'tStartRefresh')  # time at next scr refresh
                startx_4.setAutoDraw(True)
            if startx_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > startx_4.tStartRefresh + .75-frameTolerance:
                    # keep track of stop time/frame for later
                    startx_4.tStop = t  # not accounting for scr refresh
                    startx_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(startx_4, 'tStopRefresh')  # time at next scr refresh
                    startx_4.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pauseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "pause"-------
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        for across in crosses:
                across.setAutoDraw(False)
        loop_spatial_exp.addData('startx_4.started', startx_4.tStartRefresh)
        loop_spatial_exp.addData('startx_4.stopped', startx_4.tStopRefresh)
        thisExp.nextEntry()
        
    # completed spatial repeats of 'loop_spatial_exp'
    
    
    # set up handler to look after randomisation of conditions etc
    loop_temporal_exp = data.TrialHandler(nReps=temporal, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loop_temporal_exp')
    thisExp.addLoop(loop_temporal_exp)  # add the loop to the experiment
    thisLoop_temporal_exp = loop_temporal_exp.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_temporal_exp.rgb)
    if thisLoop_temporal_exp != None:
        for paramName in thisLoop_temporal_exp:
            exec('{} = thisLoop_temporal_exp[paramName]'.format(paramName))
    
    for thisLoop_temporal_exp in loop_temporal_exp:
        currentLoop = loop_temporal_exp
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_temporal_exp.rgb)
        if thisLoop_temporal_exp != None:
            for paramName in thisLoop_temporal_exp:
                exec('{} = thisLoop_temporal_exp[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "hg_start"-------
        continueRoutine = True
        # update component parameters for each repeat
        hg_bottom.setPos(bottom_hg_loc)
        hg_bottom.setFillColor([0.004,0.004,0.004])
        hg_bottom.setLineColor([0.004,0.004,0.004])
        # setup some python lists for storing info about the mouse_hg
        mouse_hg.clicked_name = []
        gotValidClick = False  # until a click is received
        hg_top.setPos(top_hg_loc)
        hg_top.setFillColor([0.004,0.004,0.004])
        hg_top.setLineColor([0.004,0.004,0.004])
        # keep track of which components have finished
        hg_startComponents = [hg_bottom, mouse_hg, hg_top]
        for thisComponent in hg_startComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        hg_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "hg_start"-------
        while continueRoutine:
            # get current time
            t = hg_startClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=hg_startClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *hg_bottom* updates
            if hg_bottom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hg_bottom.frameNStart = frameN  # exact frame index
                hg_bottom.tStart = t  # local t and not account for scr refresh
                hg_bottom.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hg_bottom, 'tStartRefresh')  # time at next scr refresh
                hg_bottom.setAutoDraw(True)
            # *mouse_hg* updates
            if mouse_hg.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_hg.frameNStart = frameN  # exact frame index
                mouse_hg.tStart = t  # local t and not account for scr refresh
                mouse_hg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_hg, 'tStartRefresh')  # time at next scr refresh
                mouse_hg.status = STARTED
                mouse_hg.mouseClock.reset()
                prevButtonState = mouse_hg.getPressed()  # if button is down already this ISN'T a new click
            if mouse_hg.status == STARTED:  # only update if started and not finished!
                buttons = mouse_hg.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [hg_bottom, hg_top]:
                            if obj.contains(mouse_hg):
                                gotValidClick = True
                                mouse_hg.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *hg_top* updates
            if hg_top.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hg_top.frameNStart = frameN  # exact frame index
                hg_top.tStart = t  # local t and not account for scr refresh
                hg_top.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hg_top, 'tStartRefresh')  # time at next scr refresh
                hg_top.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in hg_startComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "hg_start"-------
        for thisComponent in hg_startComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_temporal_exp.addData('hg_bottom.started', hg_bottom.tStartRefresh)
        loop_temporal_exp.addData('hg_bottom.stopped', hg_bottom.tStopRefresh)
        # store data for loop_temporal_exp (TrialHandler)
        x, y = mouse_hg.getPos()
        buttons = mouse_hg.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [hg_bottom, hg_top]:
                if obj.contains(mouse_hg):
                    gotValidClick = True
                    mouse_hg.clicked_name.append(obj.name)
        loop_temporal_exp.addData('mouse_hg.x', x)
        loop_temporal_exp.addData('mouse_hg.y', y)
        loop_temporal_exp.addData('mouse_hg.leftButton', buttons[0])
        loop_temporal_exp.addData('mouse_hg.midButton', buttons[1])
        loop_temporal_exp.addData('mouse_hg.rightButton', buttons[2])
        if len(mouse_hg.clicked_name):
            loop_temporal_exp.addData('mouse_hg.clicked_name', mouse_hg.clicked_name[0])
        loop_temporal_exp.addData('mouse_hg.started', mouse_hg.tStart)
        loop_temporal_exp.addData('mouse_hg.stopped', mouse_hg.tStop)
        loop_temporal_exp.addData('hg_top.started', hg_top.tStartRefresh)
        loop_temporal_exp.addData('hg_top.stopped', hg_top.tStopRefresh)
        # the Routine "hg_start" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "hg_mid"-------
        continueRoutine = True
        # update component parameters for each repeat
        hg_bottom_2.setPos(bottom_hg_loc)
        hg_bottom_2.setFillColor([-1.000,-1.000,-1.000])
        hg_bottom_2.setLineColor([-1.000,-1.000,-1.000])
        # setup some python lists for storing info about the mouse_hg_2
        mouse_hg_2.clicked_name = []
        gotValidClick = False  # until a click is received
        hg_top_2.setPos(top_hg_loc)
        hg_top_2.setFillColor([-1.000,-1.000,-1.000])
        hg_top_2.setLineColor([-1.000,-1.000,-1.000])
        # keep track of which components have finished
        hg_midComponents = [hg_bottom_2, mouse_hg_2, hg_top_2]
        for thisComponent in hg_midComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        hg_midClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "hg_mid"-------
        while continueRoutine:
            # get current time
            t = hg_midClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=hg_midClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *hg_bottom_2* updates
            if hg_bottom_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hg_bottom_2.frameNStart = frameN  # exact frame index
                hg_bottom_2.tStart = t  # local t and not account for scr refresh
                hg_bottom_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hg_bottom_2, 'tStartRefresh')  # time at next scr refresh
                hg_bottom_2.setAutoDraw(True)
            # *mouse_hg_2* updates
            if mouse_hg_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_hg_2.frameNStart = frameN  # exact frame index
                mouse_hg_2.tStart = t  # local t and not account for scr refresh
                mouse_hg_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_hg_2, 'tStartRefresh')  # time at next scr refresh
                mouse_hg_2.status = STARTED
                mouse_hg_2.mouseClock.reset()
                prevButtonState = mouse_hg_2.getPressed()  # if button is down already this ISN'T a new click
            if mouse_hg_2.status == STARTED:  # only update if started and not finished!
                buttons = mouse_hg_2.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [hg_bottom_2, hg_top_2]:
                            if obj.contains(mouse_hg_2):
                                gotValidClick = True
                                mouse_hg_2.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *hg_top_2* updates
            if hg_top_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hg_top_2.frameNStart = frameN  # exact frame index
                hg_top_2.tStart = t  # local t and not account for scr refresh
                hg_top_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hg_top_2, 'tStartRefresh')  # time at next scr refresh
                hg_top_2.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in hg_midComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "hg_mid"-------
        for thisComponent in hg_midComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_temporal_exp.addData('hg_bottom_2.started', hg_bottom_2.tStartRefresh)
        loop_temporal_exp.addData('hg_bottom_2.stopped', hg_bottom_2.tStopRefresh)
        # store data for loop_temporal_exp (TrialHandler)
        x, y = mouse_hg_2.getPos()
        buttons = mouse_hg_2.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [hg_bottom_2, hg_top_2]:
                if obj.contains(mouse_hg_2):
                    gotValidClick = True
                    mouse_hg_2.clicked_name.append(obj.name)
        loop_temporal_exp.addData('mouse_hg_2.x', x)
        loop_temporal_exp.addData('mouse_hg_2.y', y)
        loop_temporal_exp.addData('mouse_hg_2.leftButton', buttons[0])
        loop_temporal_exp.addData('mouse_hg_2.midButton', buttons[1])
        loop_temporal_exp.addData('mouse_hg_2.rightButton', buttons[2])
        if len(mouse_hg_2.clicked_name):
            loop_temporal_exp.addData('mouse_hg_2.clicked_name', mouse_hg_2.clicked_name[0])
        loop_temporal_exp.addData('mouse_hg_2.started', mouse_hg_2.tStart)
        loop_temporal_exp.addData('mouse_hg_2.stopped', mouse_hg_2.tStop)
        loop_temporal_exp.addData('hg_top_2.started', hg_top_2.tStartRefresh)
        loop_temporal_exp.addData('hg_top_2.stopped', hg_top_2.tStopRefresh)
        # the Routine "hg_mid" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "hg_end"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        hg_bottom_3.setPos(bottom_hg_loc)
        hg_bottom_3.setFillColor([0.004,0.004,0.004])
        hg_bottom_3.setLineColor([0.004,0.004,0.004])
        hg_top_3.setPos(top_hg_loc)
        hg_top_3.setFillColor([0.004,0.004,0.004])
        hg_top_3.setLineColor([0.004,0.004,0.004])
        # keep track of which components have finished
        hg_endComponents = [hg_bottom_3, hg_top_3]
        for thisComponent in hg_endComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        hg_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "hg_end"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = hg_endClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=hg_endClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *hg_bottom_3* updates
            if hg_bottom_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hg_bottom_3.frameNStart = frameN  # exact frame index
                hg_bottom_3.tStart = t  # local t and not account for scr refresh
                hg_bottom_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hg_bottom_3, 'tStartRefresh')  # time at next scr refresh
                hg_bottom_3.setAutoDraw(True)
            if hg_bottom_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > hg_bottom_3.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    hg_bottom_3.tStop = t  # not accounting for scr refresh
                    hg_bottom_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(hg_bottom_3, 'tStopRefresh')  # time at next scr refresh
                    hg_bottom_3.setAutoDraw(False)
            
            # *hg_top_3* updates
            if hg_top_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hg_top_3.frameNStart = frameN  # exact frame index
                hg_top_3.tStart = t  # local t and not account for scr refresh
                hg_top_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hg_top_3, 'tStartRefresh')  # time at next scr refresh
                hg_top_3.setAutoDraw(True)
            if hg_top_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > hg_top_3.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    hg_top_3.tStop = t  # not accounting for scr refresh
                    hg_top_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(hg_top_3, 'tStopRefresh')  # time at next scr refresh
                    hg_top_3.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in hg_endComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "hg_end"-------
        for thisComponent in hg_endComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_temporal_exp.addData('hg_bottom_3.started', hg_bottom_3.tStartRefresh)
        loop_temporal_exp.addData('hg_bottom_3.stopped', hg_bottom_3.tStopRefresh)
        loop_temporal_exp.addData('hg_top_3.started', hg_top_3.tStartRefresh)
        loop_temporal_exp.addData('hg_top_3.stopped', hg_top_3.tStopRefresh)
        thisExp.nextEntry()
        
    # completed temporal repeats of 'loop_temporal_exp'
    
    
    # ------Prepare to start Routine "ready"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    readyComponents = [text, instruction_req, key_resp]
    for thisComponent in readyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    readyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ready"-------
    while continueRoutine:
        # get current time
        t = readyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=readyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *instruction_req* updates
        if instruction_req.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_req.frameNStart = frameN  # exact frame index
            instruction_req.tStart = t  # local t and not account for scr refresh
            instruction_req.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_req, 'tStartRefresh')  # time at next scr refresh
            instruction_req.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space', 'i', 't'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in readyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ready"-------
    for thisComponent in readyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    exp_loop.addData('text.started', text.tStartRefresh)
    exp_loop.addData('text.stopped', text.tStopRefresh)
    exp_loop.addData('instruction_req.started', instruction_req.tStartRefresh)
    exp_loop.addData('instruction_req.stopped', instruction_req.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    exp_loop.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        exp_loop.addData('key_resp.rt', key_resp.rt)
    exp_loop.addData('key_resp.started', key_resp.tStartRefresh)
    exp_loop.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "ready" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "request_inst"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_9.keys = []
    key_resp_9.rt = []
    _key_resp_9_allKeys = []
    # keep track of which components have finished
    request_instComponents = [instruction_re_text, key_resp_9]
    for thisComponent in request_instComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    request_instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "request_inst"-------
    while continueRoutine:
        # get current time
        t = request_instClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=request_instClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_re_text* updates
        if instruction_re_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_re_text.frameNStart = frameN  # exact frame index
            instruction_re_text.tStart = t  # local t and not account for scr refresh
            instruction_re_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_re_text, 'tStartRefresh')  # time at next scr refresh
            instruction_re_text.setAutoDraw(True)
        if key_resp.keys[0] != 'i':
            continueRoutine = False # don't even start this routine
        
        
        # *key_resp_9* updates
        waitOnFlip = False
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.tStart = t  # local t and not account for scr refresh
            key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_9_allKeys.extend(theseKeys)
            if len(_key_resp_9_allKeys):
                key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in request_instComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "request_inst"-------
    for thisComponent in request_instComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    exp_loop.addData('instruction_re_text.started', instruction_re_text.tStartRefresh)
    exp_loop.addData('instruction_re_text.stopped', instruction_re_text.tStopRefresh)
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
    exp_loop.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        exp_loop.addData('key_resp_9.rt', key_resp_9.rt)
    exp_loop.addData('key_resp_9.started', key_resp_9.tStartRefresh)
    exp_loop.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
    # the Routine "request_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "catchtrials"-------
    continueRoutine = True
    # update component parameters for each repeat
    catch_text.setText(catchd)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    catchtrialsComponents = [catch_text, key_resp_2]
    for thisComponent in catchtrialsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    catchtrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "catchtrials"-------
    while continueRoutine:
        # get current time
        t = catchtrialsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=catchtrialsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *catch_text* updates
        if catch_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            catch_text.frameNStart = frameN  # exact frame index
            catch_text.tStart = t  # local t and not account for scr refresh
            catch_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(catch_text, 'tStartRefresh')  # time at next scr refresh
            catch_text.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['c', 'l', 's', 'space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        if trial_counter==0 or (trial_counter+1) %20!=0 :
            continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in catchtrialsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "catchtrials"-------
    for thisComponent in catchtrialsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    exp_loop.addData('catch_text.started', catch_text.tStartRefresh)
    exp_loop.addData('catch_text.stopped', catch_text.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    exp_loop.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        exp_loop.addData('key_resp_2.rt', key_resp_2.rt)
    exp_loop.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    exp_loop.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "catchtrials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "breakscreen"-------
    continueRoutine = True
    # update component parameters for each repeat
    breakscreen_text.setText('You are now half way done with the trials. You can take a quick break if you\'d like. Once you are ready to proceed with the rest of the experiment you can press "space".')
    break_key_resp.keys = []
    break_key_resp.rt = []
    _break_key_resp_allKeys = []
    # keep track of which components have finished
    breakscreenComponents = [breakscreen_text, break_key_resp]
    for thisComponent in breakscreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    breakscreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "breakscreen"-------
    while continueRoutine:
        # get current time
        t = breakscreenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=breakscreenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *breakscreen_text* updates
        if breakscreen_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            breakscreen_text.frameNStart = frameN  # exact frame index
            breakscreen_text.tStart = t  # local t and not account for scr refresh
            breakscreen_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(breakscreen_text, 'tStartRefresh')  # time at next scr refresh
            breakscreen_text.setAutoDraw(True)
        
        # *break_key_resp* updates
        waitOnFlip = False
        if break_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_key_resp.frameNStart = frameN  # exact frame index
            break_key_resp.tStart = t  # local t and not account for scr refresh
            break_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_key_resp, 'tStartRefresh')  # time at next scr refresh
            break_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(break_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(break_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if break_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = break_key_resp.getKeys(keyList=['space', 'i'], waitRelease=False)
            _break_key_resp_allKeys.extend(theseKeys)
            if len(_break_key_resp_allKeys):
                break_key_resp.keys = _break_key_resp_allKeys[-1].name  # just the last key pressed
                break_key_resp.rt = _break_key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        if trial_counter != 81:
            continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in breakscreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "breakscreen"-------
    for thisComponent in breakscreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    exp_loop.addData('breakscreen_text.started', breakscreen_text.tStartRefresh)
    exp_loop.addData('breakscreen_text.stopped', breakscreen_text.tStopRefresh)
    # check responses
    if break_key_resp.keys in ['', [], None]:  # No response was made
        break_key_resp.keys = None
    exp_loop.addData('break_key_resp.keys',break_key_resp.keys)
    if break_key_resp.keys != None:  # we had a response
        exp_loop.addData('break_key_resp.rt', break_key_resp.rt)
    exp_loop.addData('break_key_resp.started', break_key_resp.tStartRefresh)
    exp_loop.addData('break_key_resp.stopped', break_key_resp.tStopRefresh)
    # the Routine "breakscreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'exp_loop'


# ------Prepare to start Routine "end_screen"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
end_screenComponents = [text_7]
for thisComponent in end_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_screen"-------
for thisComponent in end_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
