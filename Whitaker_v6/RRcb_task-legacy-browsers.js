/****************** 
 * Rrcb_Task Test *
 ******************/


// store info about the experiment session:
let expName = 'RRcb_task';  // from the Builder filename that created this script
let expInfo = {
    'First two letters of each parents First Name and their date of birth (Month and Day only) . E.g. hapa1114': '',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([1.0, 1.0, 1.0]),
  units: 'pix',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(gen_instructionsRoutineBegin());
flowScheduler.add(gen_instructionsRoutineEachFrame());
flowScheduler.add(gen_instructionsRoutineEnd());
flowScheduler.add(screen_calibrationRoutineBegin());
flowScheduler.add(screen_calibrationRoutineEachFrame());
flowScheduler.add(screen_calibrationRoutineEnd());
flowScheduler.add(screen_calibration_endRoutineBegin());
flowScheduler.add(screen_calibration_endRoutineEachFrame());
flowScheduler.add(screen_calibration_endRoutineEnd());
flowScheduler.add(screen_calibration_end_2RoutineBegin());
flowScheduler.add(screen_calibration_end_2RoutineEachFrame());
flowScheduler.add(screen_calibration_end_2RoutineEnd());
flowScheduler.add(candb_instructionsRoutineBegin());
flowScheduler.add(candb_instructionsRoutineEachFrame());
flowScheduler.add(candb_instructionsRoutineEnd());
flowScheduler.add(practice_instructionsRoutineBegin());
flowScheduler.add(practice_instructionsRoutineEachFrame());
flowScheduler.add(practice_instructionsRoutineEnd());
const practice_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practice_loopLoopBegin(practice_loopLoopScheduler));
flowScheduler.add(practice_loopLoopScheduler);
flowScheduler.add(practice_loopLoopEnd);
flowScheduler.add(practicetrialendscreenRoutineBegin());
flowScheduler.add(practicetrialendscreenRoutineEachFrame());
flowScheduler.add(practicetrialendscreenRoutineEnd());
const exp_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(exp_loopLoopBegin(exp_loopLoopScheduler));
flowScheduler.add(exp_loopLoopScheduler);
flowScheduler.add(exp_loopLoopEnd);
flowScheduler.add(end_screenRoutineBegin());
flowScheduler.add(end_screenRoutineEachFrame());
flowScheduler.add(end_screenRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'linetask_full_conditions.csv', 'path': 'linetask_full_conditions.csv'},
    {'name': 'linetask_prac_conditions_mod.csv', 'path': 'linetask_prac_conditions_mod.csv'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.4';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var gen_instructionsClock;
var instruction_text_4;
var instructions_key_resp_3;
var thisExp;
var win;
var shuffle;
var GlobalClock;
var screen_calibrationClock;
var calibration_instructions;
var cal_line;
var c_start_x;
var c_end_x;
var cal_mouse_start;
var screen_calibration_endClock;
var calibration_instructions_2;
var cal_line_2;
var c_start_x_2;
var c_end_x_2;
var mouse_cal_end_2;
var screen_calibration_end_2Clock;
var calibration_instructions_3;
var cal_line_3;
var c_start_x_3;
var c_end_x_3;
var candb_instructionsClock;
var instruction_text;
var instructions_key_resp;
var practice_instructionsClock;
var instruction_text_3;
var instructions_key_resp_2;
var fixationcrossesClock;
var fixation_cross;
var trial_counter;
var targetlinesClock;
var targetline;
var distractorline1;
var distractorline2;
var promptClock;
var prompt_text;
var start_xClock;
var startx;
var mouse_startx;
var end_xClock;
var startx_ph;
var polygon;
var mouse;
var pauseClock;
var startx_4;
var hg_startClock;
var hg_bottom;
var mouse_hg;
var hg_top;
var hg_midClock;
var hg_bottom_2;
var mouse_hg_2;
var hg_top_2;
var hg_endClock;
var hg_bottom_3;
var hg_top_3;
var readyClock;
var text;
var instruction_req;
var key_resp;
var reminderClock;
var text_4;
var key_resp_6;
var troubleshootingClock;
var troubleshooting_text;
var key_resp_11;
var request_instClock;
var instruction_re_text;
var key_resp_9;
var practicetrialendscreenClock;
var practicetrialend_text;
var practicetrialend_key_resp;
var catchtrialsClock;
var catch_text;
var key_resp_2;
var breakscreenClock;
var breakscreen_text;
var break_key_resp;
var end_screenClock;
var text_7;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "gen_instructions"
  gen_instructionsClock = new util.Clock();
  instruction_text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_text_4',
    text: 'In this task, you will be making temporal and spatial judgements of a line stimulus that appears on your screen. This task should take approximately 15 - 20 minutes.\n\nYou can move through this experiment at your own pace, and there will be a designated break at the half-way point should you require it.\n\nWhen prompted, click the “X” icon(s) to calibrate left to right.\n\nYou will receive more instructions before beginning. Please make sure your browser is in full screen mode (press "F11" to make the browser full screen on a PC and "control+command+F" on a Mac). Press "esc" at any point if you would like to completely exit the experiment. \n\nPress "space" to move onto the next screen',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  instructions_key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from code_JS_2
  thisExp = psychoJS.experiment;
  win = psychoJS.window;
  shuffle = util.shuffle;
  Array.prototype.append = [].push;
  GlobalClock = new util.Clock();
  // Initialize components for Routine "screen_calibration"
  screen_calibrationClock = new util.Clock();
  calibration_instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'calibration_instructions',
    text: 'Click the two ends of the line to calibrate your screen size.',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0.25], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  cal_line = new visual.ShapeStim ({
    win: psychoJS.window, name: 'cal_line', units : 'height', 
    vertices: [[-0.5[0]/2.0, 0], [+0.5[0]/2.0, 0]],
    ori: 0, pos: [0, 0],
    lineWidth: 5, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  c_start_x = new visual.ShapeStim ({
    win: psychoJS.window, name: 'c_start_x', units : 'height', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 45, pos: [(- 0.25), 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  c_end_x = new visual.ShapeStim ({
    win: psychoJS.window, name: 'c_end_x', units : 'height', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 45, pos: [0.25, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  cal_mouse_start = new core.Mouse({
    win: psychoJS.window,
  });
  cal_mouse_start.mouseClock = new util.Clock();
  // Initialize components for Routine "screen_calibration_end"
  screen_calibration_endClock = new util.Clock();
  calibration_instructions_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'calibration_instructions_2',
    text: 'Click the two ends of the line to calibrate your screen size.  ',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0.25], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  cal_line_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'cal_line_2', units : 'height', 
    vertices: [[-[1.0, 1.0][0]/2.0, 0], [+[1.0, 1.0][0]/2.0, 0]],
    ori: 0, pos: [0, 0],
    lineWidth: 5, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  c_start_x_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'c_start_x_2', units : 'height', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 45, pos: [(- 0.25), 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  c_end_x_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'c_end_x_2', units : 'height', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 45, pos: [0.25, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  mouse_cal_end_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_cal_end_2.mouseClock = new util.Clock();
  // Initialize components for Routine "screen_calibration_end_2"
  screen_calibration_end_2Clock = new util.Clock();
  calibration_instructions_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'calibration_instructions_3',
    text: 'Click the two ends of the line to calibrate your screen size. ',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0.25], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  cal_line_3 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'cal_line_3', units : 'height', 
    vertices: [[-[1.0, 1.0][0]/2.0, 0], [+[1.0, 1.0][0]/2.0, 0]],
    ori: 0, pos: [0, 0],
    lineWidth: 5, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  c_start_x_3 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'c_start_x_3', units : 'height', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 45, pos: [(- 0.25), 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  c_end_x_3 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'c_end_x_3', units : 'height', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 45, pos: [0.25, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  // Initialize components for Routine "candb_instructions"
  candb_instructionsClock = new util.Clock();
  instruction_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_text',
    text: 'In this task, you will see line(s) growing across the screen. Please pay attention to both the final length, as well as the total amount of time that the black target line is presented for.\n\nAfter the stimulus presentation, you will either be prompted to reproduce the duration (amount of time) of the black target line, or its length.\n\nOn the "line" trials, you will click the "X" icon, and then place another "X" (with your cursor) adjacent to the first. The distance between these two "X" icons will represent your estimate of the target line’s final length.\n\nOn the "time" trials, you will click the grey hourglass to start your duration reproduction. Do not drag the hourglass, just click it again when you think the duration of the target line has passed.\n\nPlease make sure your browser is in full screen mode (press "F11" to make the browser full screen on a PC and "control+command+F" on a Mac). Press "esc" at any point if you would like to completely exit the experiment.\n\nPress "space" to move onto the next screen',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.029,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  instructions_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice_instructions"
  practice_instructionsClock = new util.Clock();
  instruction_text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_text_3',
    text: 'Below is a troubleshooting guide:\n\nUnable to get back to fullscreen? \nWindows: press "F11" \nMac: press "control+command+F" if the toolbar/taskbar is still visible, then go to View> and make sure that the option "Always Show Toolbar in Fullscreen" is deselected (i.e. doesn\'t have a check mark next to it). \n\nIf you wish to completely exit the experiment, press "esc"\n\nIf you are having any other issues, please contact shyamu93@my.yorku.ca for further assistance. \n\nPress "space" to continue with the task',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  instructions_key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixationcrosses"
  fixationcrossesClock = new util.Clock();
  fixation_cross = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_cross', 
    vertices: 'cross', size:[150, 150],
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  // Run 'Begin Experiment' code from counter_code
  trial_counter = 0;
  
  // Initialize components for Routine "targetlines"
  targetlinesClock = new util.Clock();
  targetline = new visual.ShapeStim ({
    win: psychoJS.window, name: 'targetline', 
    vertices: [[-[1.0, 1.0][0]/2.0, 0], [+[1.0, 1.0][0]/2.0, 0]],
    ori: 0, pos: [0, 0],
    lineWidth: 5, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  distractorline1 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'distractorline1', 
    vertices: [[-[1.0, 1.0][0]/2.0, 0], [+[1.0, 1.0][0]/2.0, 0]],
    ori: 0, pos: [0, 0],
    lineWidth: 5, 
    colorSpace: 'rgb',
    lineColor: new util.Color('coral'),
    fillColor: new util.Color('coral'),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  distractorline2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'distractorline2', 
    vertices: [[-[1.0, 1.0][0]/2.0, 0], [+[1.0, 1.0][0]/2.0, 0]],
    ori: 0, pos: [0, 0],
    lineWidth: 5, 
    colorSpace: 'rgb',
    lineColor: new util.Color('coral'),
    fillColor: new util.Color('coral'),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  // Initialize components for Routine "prompt"
  promptClock = new util.Clock();
  prompt_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'prompt_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 75,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "start_x"
  start_xClock = new util.Clock();
  startx = new visual.ShapeStim ({
    win: psychoJS.window, name: 'startx', units : 'height', 
    vertices: 'cross', size:[0.06, 0.06],
    ori: 45, pos: [0, 0],
    lineWidth: 3, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  mouse_startx = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_startx.mouseClock = new util.Clock();
  // Initialize components for Routine "end_x"
  end_xClock = new util.Clock();
  startx_ph = new visual.ShapeStim ({
    win: psychoJS.window, name: 'startx_ph', units : 'height', 
    vertices: 'cross', size:[0.06, 0.06],
    ori: 45, pos: [0, 0],
    lineWidth: 3, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  polygon = new visual.Rect ({
    win: psychoJS.window, name: 'polygon', units : 'height', 
    width: [1.6, 0.1][0], height: [1.6, 0.1][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 1.0, 1.0]),
    fillColor: new util.Color([1.0, 1.0, 1.0]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "pause"
  pauseClock = new util.Clock();
  startx_4 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'startx_4', units : 'height', 
    vertices: 'cross', size:[0.06, 0.06],
    ori: 45, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  // Initialize components for Routine "hg_start"
  hg_startClock = new util.Clock();
  hg_bottom = new visual.ShapeStim ({
    win: psychoJS.window, name: 'hg_bottom', units : 'height', 
    vertices: [[-[0.08, 0.06][0]/2.0, -[0.08, 0.06][1]/2.0], [+[0.08, 0.06][0]/2.0, -[0.08, 0.06][1]/2.0], [0, [0.08, 0.06][1]/2.0]],
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  mouse_hg = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_hg.mouseClock = new util.Clock();
  hg_top = new visual.ShapeStim ({
    win: psychoJS.window, name: 'hg_top', units : 'height', 
    vertices: [[-[0.08, 0.06][0]/2.0, -[0.08, 0.06][1]/2.0], [+[0.08, 0.06][0]/2.0, -[0.08, 0.06][1]/2.0], [0, [0.08, 0.06][1]/2.0]],
    ori: 180, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  // Initialize components for Routine "hg_mid"
  hg_midClock = new util.Clock();
  hg_bottom_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'hg_bottom_2', units : 'height', 
    vertices: [[-[0.08, 0.06][0]/2.0, -[0.08, 0.06][1]/2.0], [+[0.08, 0.06][0]/2.0, -[0.08, 0.06][1]/2.0], [0, [0.08, 0.06][1]/2.0]],
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  mouse_hg_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_hg_2.mouseClock = new util.Clock();
  hg_top_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'hg_top_2', units : 'height', 
    vertices: [[-[0.08, 0.06][0]/2.0, -[0.08, 0.06][1]/2.0], [+[0.08, 0.06][0]/2.0, -[0.08, 0.06][1]/2.0], [0, [0.08, 0.06][1]/2.0]],
    ori: 180, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  // Initialize components for Routine "hg_end"
  hg_endClock = new util.Clock();
  hg_bottom_3 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'hg_bottom_3', units : 'height', 
    vertices: [[-[0.08, 0.06][0]/2.0, -[0.08, 0.06][1]/2.0], [+[0.08, 0.06][0]/2.0, -[0.08, 0.06][1]/2.0], [0, [0.08, 0.06][1]/2.0]],
    ori: 0, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  hg_top_3 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'hg_top_3', units : 'height', 
    vertices: [[-[0.08, 0.06][0]/2.0, -[0.08, 0.06][1]/2.0], [+[0.08, 0.06][0]/2.0, -[0.08, 0.06][1]/2.0], [0, [0.08, 0.06][1]/2.0]],
    ori: 180, pos: [0, 0],
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  // Initialize components for Routine "ready"
  readyClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Press the "space" when you are ready to move onto the next trial. ',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  instruction_req = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_req',
    text: 'Press "i" to see instructions again, press "t" for troubleshooting help. ',
    font: 'Arial',
    units: 'height', 
    pos: [0, (- 0.25)], height: 0.03,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reminder"
  reminderClock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Great job! Below is a reminder of the instructions now that you have seen the task.\n\nDepending on the given prompt, you will be asked to reproduce the length of the line or the amount of time it was presented for. Your screen will either show you one or multiple lines, but your focus should be on the black target line.\n\nAs lines grow across the screen, please pay attention to both the final length, as well as the total amount of time the target line was on the screen. This experiment is aimed at measuring your innate perception of space and time, so it is important that you don\'t count or use your computer screen as a frame of reference for the lines.\n\nAfter the presentation of the line(s), if the prompt says "time," you will reproduce the duration that the target line appeared for. If the prompt says "line," you will reproduce the length of the target line.\n\nOn the "line" trials, you will click the "X" icon, and then place another "X" (with your cursor) adjacent to the first. The distance between these two "X" icons will represent your estimate of the target line’s final length.\n\nOn the "time" trials, you will click the grey hourglass to start your duration reproduction. Do not drag the hourglass, just click it again when you think the duration of the target line has passed.\n\nPlease make sure your browser is in full screen mode (press "F11" to make the browser full screen on a PC and "control+command+F" on a Mac). Press "esc" at any point if you would like to completely exit the experiment.\n\nPress "space" to continue',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.025,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "troubleshooting"
  troubleshootingClock = new util.Clock();
  troubleshooting_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'troubleshooting_text',
    text: 'Below is a troubleshooting guide:\n\nUnable to get back to fullscreen? \nWindows: press "F11" \nMac: press "control+command+F" if the toolbar/taskbar is still visible, then go to View> and make sure that the option "Always Show Toolbar in Fullscreen" is deselected (i.e. doesn\'t have a check mark next to it). \n\nIf you wish to completely exit the experiment, press "esc"\n\nIf you are having any other issues, please contact shyamu93@my.yorku.ca for further assistance. \n\nPress "space" to continue with the task',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_11 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "request_inst"
  request_instClock = new util.Clock();
  instruction_re_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_re_text',
    text: 'Below is a reminder of the instructions:\n\nAs lines grow across the screen, please pay attention to both the final length, as well as the total amount of time the target line is on the screen.\n\nAfter the presentation of the line(s), if the prompt says "time," you will reproduce the duration that the target line appeared for. If the prompt says "line," you will reproduce the length of the target line.\n\nOn the "line" trials, you will click the "X" icon, and then place another "X" (with your cursor) adjacent to the first. The distance between these two "X" icons will represent your estimate of the target line’s final length.\n\nOn the "time" trials, you will click the grey hourglass to start your duration reproduction. Do not drag the hourglass, just click it again when you think the duration of the target line has passed.\n\nPress "space" to continue with the task',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practicetrialendscreen"
  practicetrialendscreenClock = new util.Clock();
  practicetrialend_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'practicetrialend_text',
    text: 'The practice trials are now finished. \n\nIf you have any questions before starting the experiment, please contact shyamu93@my.yorku.ca before continuing. If you want to see the experimental instructions again, press the "i" key on your keyboard any time in between trials. If you run into any issues with the experiment, press "t" to view a troubleshooting screen.\n\nPress "space" to start the experiment',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  practicetrialend_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "catchtrials"
  catchtrialsClock = new util.Clock();
  catch_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'catch_text',
    text: '',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "breakscreen"
  breakscreenClock = new util.Clock();
  breakscreen_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'breakscreen_text',
    text: '',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.07,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  break_key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end_screen"
  end_screenClock = new util.Clock();
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: 'Thank you for your participation! Please wait while your data is saved. ',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _instructions_key_resp_3_allKeys;
var gen_instructionsComponents;
function gen_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'gen_instructions' ---
    t = 0;
    gen_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instructions_key_resp_3.keys = undefined;
    instructions_key_resp_3.rt = undefined;
    _instructions_key_resp_3_allKeys = [];
    // keep track of which components have finished
    gen_instructionsComponents = [];
    gen_instructionsComponents.push(instruction_text_4);
    gen_instructionsComponents.push(instructions_key_resp_3);
    
    gen_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function gen_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'gen_instructions' ---
    // get current time
    t = gen_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction_text_4* updates
    if (t >= 0.0 && instruction_text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_text_4.tStart = t;  // (not accounting for frame time here)
      instruction_text_4.frameNStart = frameN;  // exact frame index
      
      instruction_text_4.setAutoDraw(true);
    }

    
    // *instructions_key_resp_3* updates
    if (t >= 0.0 && instructions_key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_key_resp_3.tStart = t;  // (not accounting for frame time here)
      instructions_key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instructions_key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instructions_key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instructions_key_resp_3.clearEvents(); });
    }

    if (instructions_key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = instructions_key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _instructions_key_resp_3_allKeys = _instructions_key_resp_3_allKeys.concat(theseKeys);
      if (_instructions_key_resp_3_allKeys.length > 0) {
        instructions_key_resp_3.keys = _instructions_key_resp_3_allKeys[_instructions_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        instructions_key_resp_3.rt = _instructions_key_resp_3_allKeys[_instructions_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    gen_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function gen_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'gen_instructions' ---
    gen_instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(instructions_key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('instructions_key_resp_3.keys', instructions_key_resp_3.keys);
    if (typeof instructions_key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instructions_key_resp_3.rt', instructions_key_resp_3.rt);
        routineTimer.reset();
        }
    
    instructions_key_resp_3.stop();
    // the Routine "gen_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var gotValidClick;
var screen_calibrationComponents;
function screen_calibrationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'screen_calibration' ---
    t = 0;
    screen_calibrationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the cal_mouse_start
    // current position of the mouse:
    cal_mouse_start.x = [];
    cal_mouse_start.y = [];
    cal_mouse_start.leftButton = [];
    cal_mouse_start.midButton = [];
    cal_mouse_start.rightButton = [];
    cal_mouse_start.time = [];
    cal_mouse_start.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    screen_calibrationComponents = [];
    screen_calibrationComponents.push(calibration_instructions);
    screen_calibrationComponents.push(cal_line);
    screen_calibrationComponents.push(c_start_x);
    screen_calibrationComponents.push(c_end_x);
    screen_calibrationComponents.push(cal_mouse_start);
    
    screen_calibrationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function screen_calibrationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'screen_calibration' ---
    // get current time
    t = screen_calibrationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *calibration_instructions* updates
    if (t >= 0.0 && calibration_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      calibration_instructions.tStart = t;  // (not accounting for frame time here)
      calibration_instructions.frameNStart = frameN;  // exact frame index
      
      calibration_instructions.setAutoDraw(true);
    }

    
    // *cal_line* updates
    if (t >= 0.0 && cal_line.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cal_line.tStart = t;  // (not accounting for frame time here)
      cal_line.frameNStart = frameN;  // exact frame index
      
      cal_line.setAutoDraw(true);
    }

    
    // *c_start_x* updates
    if (t >= 0.0 && c_start_x.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      c_start_x.tStart = t;  // (not accounting for frame time here)
      c_start_x.frameNStart = frameN;  // exact frame index
      
      c_start_x.setAutoDraw(true);
    }

    
    // *c_end_x* updates
    if (t >= 0.0 && c_end_x.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      c_end_x.tStart = t;  // (not accounting for frame time here)
      c_end_x.frameNStart = frameN;  // exact frame index
      
      c_end_x.setAutoDraw(true);
    }

    // *cal_mouse_start* updates
    if (t >= 0.0 && cal_mouse_start.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cal_mouse_start.tStart = t;  // (not accounting for frame time here)
      cal_mouse_start.frameNStart = frameN;  // exact frame index
      
      cal_mouse_start.status = PsychoJS.Status.STARTED;
      cal_mouse_start.mouseClock.reset();
      prevButtonState = cal_mouse_start.getPressed();  // if button is down already this ISN'T a new click
      }
    if (cal_mouse_start.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = cal_mouse_start.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [c_start_x]) {
            if (obj.contains(cal_mouse_start)) {
              gotValidClick = true;
              cal_mouse_start.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = cal_mouse_start.getPos();
          cal_mouse_start.x.push(_mouseXYs[0]);
          cal_mouse_start.y.push(_mouseXYs[1]);
          cal_mouse_start.leftButton.push(_mouseButtons[0]);
          cal_mouse_start.midButton.push(_mouseButtons[1]);
          cal_mouse_start.rightButton.push(_mouseButtons[2]);
          cal_mouse_start.time.push(cal_mouse_start.mouseClock.getTime());
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    if (cal_mouse_start.isPressedIn(c_start_x)) {
        c_start_x.fillColor = [1.000,0.004,1.000];
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    screen_calibrationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function screen_calibrationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'screen_calibration' ---
    screen_calibrationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    if (cal_mouse_start.x) {  psychoJS.experiment.addData('cal_mouse_start.x', cal_mouse_start.x[0])};
    if (cal_mouse_start.y) {  psychoJS.experiment.addData('cal_mouse_start.y', cal_mouse_start.y[0])};
    if (cal_mouse_start.leftButton) {  psychoJS.experiment.addData('cal_mouse_start.leftButton', cal_mouse_start.leftButton[0])};
    if (cal_mouse_start.midButton) {  psychoJS.experiment.addData('cal_mouse_start.midButton', cal_mouse_start.midButton[0])};
    if (cal_mouse_start.rightButton) {  psychoJS.experiment.addData('cal_mouse_start.rightButton', cal_mouse_start.rightButton[0])};
    if (cal_mouse_start.time) {  psychoJS.experiment.addData('cal_mouse_start.time', cal_mouse_start.time[0])};
    if (cal_mouse_start.clicked_name) {  psychoJS.experiment.addData('cal_mouse_start.clicked_name', cal_mouse_start.clicked_name[0])};
    
    // the Routine "screen_calibration" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var screen_calibration_endComponents;
function screen_calibration_endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'screen_calibration_end' ---
    t = 0;
    screen_calibration_endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_cal_end_2
    // current position of the mouse:
    mouse_cal_end_2.x = [];
    mouse_cal_end_2.y = [];
    mouse_cal_end_2.leftButton = [];
    mouse_cal_end_2.midButton = [];
    mouse_cal_end_2.rightButton = [];
    mouse_cal_end_2.time = [];
    mouse_cal_end_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    screen_calibration_endComponents = [];
    screen_calibration_endComponents.push(calibration_instructions_2);
    screen_calibration_endComponents.push(cal_line_2);
    screen_calibration_endComponents.push(c_start_x_2);
    screen_calibration_endComponents.push(c_end_x_2);
    screen_calibration_endComponents.push(mouse_cal_end_2);
    
    screen_calibration_endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function screen_calibration_endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'screen_calibration_end' ---
    // get current time
    t = screen_calibration_endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *calibration_instructions_2* updates
    if (t >= 0.0 && calibration_instructions_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      calibration_instructions_2.tStart = t;  // (not accounting for frame time here)
      calibration_instructions_2.frameNStart = frameN;  // exact frame index
      
      calibration_instructions_2.setAutoDraw(true);
    }

    
    // *cal_line_2* updates
    if (t >= 0.0 && cal_line_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cal_line_2.tStart = t;  // (not accounting for frame time here)
      cal_line_2.frameNStart = frameN;  // exact frame index
      
      cal_line_2.setAutoDraw(true);
    }

    
    if (cal_line_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      cal_line_2.setPos([0, 0], false);
      cal_line_2.setSize(0.5, false);
    }
    
    // *c_start_x_2* updates
    if (t >= 0.0 && c_start_x_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      c_start_x_2.tStart = t;  // (not accounting for frame time here)
      c_start_x_2.frameNStart = frameN;  // exact frame index
      
      c_start_x_2.setAutoDraw(true);
    }

    
    // *c_end_x_2* updates
    if (t >= 0.0 && c_end_x_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      c_end_x_2.tStart = t;  // (not accounting for frame time here)
      c_end_x_2.frameNStart = frameN;  // exact frame index
      
      c_end_x_2.setAutoDraw(true);
    }

    // *mouse_cal_end_2* updates
    if (t >= 0.0 && mouse_cal_end_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_cal_end_2.tStart = t;  // (not accounting for frame time here)
      mouse_cal_end_2.frameNStart = frameN;  // exact frame index
      
      mouse_cal_end_2.status = PsychoJS.Status.STARTED;
      mouse_cal_end_2.mouseClock.reset();
      prevButtonState = mouse_cal_end_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_cal_end_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_cal_end_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [c_end_x]) {
            if (obj.contains(mouse_cal_end_2)) {
              gotValidClick = true;
              mouse_cal_end_2.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_cal_end_2.getPos();
          mouse_cal_end_2.x.push(_mouseXYs[0]);
          mouse_cal_end_2.y.push(_mouseXYs[1]);
          mouse_cal_end_2.leftButton.push(_mouseButtons[0]);
          mouse_cal_end_2.midButton.push(_mouseButtons[1]);
          mouse_cal_end_2.rightButton.push(_mouseButtons[2]);
          mouse_cal_end_2.time.push(mouse_cal_end_2.mouseClock.getTime());
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    screen_calibration_endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function screen_calibration_endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'screen_calibration_end' ---
    screen_calibration_endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_cal_end_2.x) {  psychoJS.experiment.addData('mouse_cal_end_2.x', mouse_cal_end_2.x[0])};
    if (mouse_cal_end_2.y) {  psychoJS.experiment.addData('mouse_cal_end_2.y', mouse_cal_end_2.y[0])};
    if (mouse_cal_end_2.leftButton) {  psychoJS.experiment.addData('mouse_cal_end_2.leftButton', mouse_cal_end_2.leftButton[0])};
    if (mouse_cal_end_2.midButton) {  psychoJS.experiment.addData('mouse_cal_end_2.midButton', mouse_cal_end_2.midButton[0])};
    if (mouse_cal_end_2.rightButton) {  psychoJS.experiment.addData('mouse_cal_end_2.rightButton', mouse_cal_end_2.rightButton[0])};
    if (mouse_cal_end_2.time) {  psychoJS.experiment.addData('mouse_cal_end_2.time', mouse_cal_end_2.time[0])};
    if (mouse_cal_end_2.clicked_name) {  psychoJS.experiment.addData('mouse_cal_end_2.clicked_name', mouse_cal_end_2.clicked_name[0])};
    
    // the Routine "screen_calibration_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var screen_calibration_end_2Components;
function screen_calibration_end_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'screen_calibration_end_2' ---
    t = 0;
    screen_calibration_end_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    screen_calibration_end_2Components = [];
    screen_calibration_end_2Components.push(calibration_instructions_3);
    screen_calibration_end_2Components.push(cal_line_3);
    screen_calibration_end_2Components.push(c_start_x_3);
    screen_calibration_end_2Components.push(c_end_x_3);
    
    screen_calibration_end_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function screen_calibration_end_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'screen_calibration_end_2' ---
    // get current time
    t = screen_calibration_end_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *calibration_instructions_3* updates
    if (t >= 0.0 && calibration_instructions_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      calibration_instructions_3.tStart = t;  // (not accounting for frame time here)
      calibration_instructions_3.frameNStart = frameN;  // exact frame index
      
      calibration_instructions_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (calibration_instructions_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      calibration_instructions_3.setAutoDraw(false);
    }
    
    // *cal_line_3* updates
    if (t >= 0.0 && cal_line_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cal_line_3.tStart = t;  // (not accounting for frame time here)
      cal_line_3.frameNStart = frameN;  // exact frame index
      
      cal_line_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (cal_line_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cal_line_3.setAutoDraw(false);
    }
    
    if (cal_line_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      cal_line_3.setPos([0, 0], false);
      cal_line_3.setSize(0.5, false);
    }
    
    // *c_start_x_3* updates
    if (t >= 0.0 && c_start_x_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      c_start_x_3.tStart = t;  // (not accounting for frame time here)
      c_start_x_3.frameNStart = frameN;  // exact frame index
      
      c_start_x_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (c_start_x_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      c_start_x_3.setAutoDraw(false);
    }
    
    // *c_end_x_3* updates
    if (t >= 0.0 && c_end_x_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      c_end_x_3.tStart = t;  // (not accounting for frame time here)
      c_end_x_3.frameNStart = frameN;  // exact frame index
      
      c_end_x_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (c_end_x_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      c_end_x_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    screen_calibration_end_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function screen_calibration_end_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'screen_calibration_end_2' ---
    screen_calibration_end_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _instructions_key_resp_allKeys;
var candb_instructionsComponents;
function candb_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'candb_instructions' ---
    t = 0;
    candb_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instructions_key_resp.keys = undefined;
    instructions_key_resp.rt = undefined;
    _instructions_key_resp_allKeys = [];
    // keep track of which components have finished
    candb_instructionsComponents = [];
    candb_instructionsComponents.push(instruction_text);
    candb_instructionsComponents.push(instructions_key_resp);
    
    candb_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function candb_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'candb_instructions' ---
    // get current time
    t = candb_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction_text* updates
    if (t >= 0.0 && instruction_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_text.tStart = t;  // (not accounting for frame time here)
      instruction_text.frameNStart = frameN;  // exact frame index
      
      instruction_text.setAutoDraw(true);
    }

    
    // *instructions_key_resp* updates
    if (t >= 0.0 && instructions_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_key_resp.tStart = t;  // (not accounting for frame time here)
      instructions_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instructions_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instructions_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instructions_key_resp.clearEvents(); });
    }

    if (instructions_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instructions_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _instructions_key_resp_allKeys = _instructions_key_resp_allKeys.concat(theseKeys);
      if (_instructions_key_resp_allKeys.length > 0) {
        instructions_key_resp.keys = _instructions_key_resp_allKeys[_instructions_key_resp_allKeys.length - 1].name;  // just the last key pressed
        instructions_key_resp.rt = _instructions_key_resp_allKeys[_instructions_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    candb_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function candb_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'candb_instructions' ---
    candb_instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(instructions_key_resp.corr, level);
    }
    psychoJS.experiment.addData('instructions_key_resp.keys', instructions_key_resp.keys);
    if (typeof instructions_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instructions_key_resp.rt', instructions_key_resp.rt);
        routineTimer.reset();
        }
    
    instructions_key_resp.stop();
    // the Routine "candb_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _instructions_key_resp_2_allKeys;
var practice_instructionsComponents;
function practice_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_instructions' ---
    t = 0;
    practice_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instructions_key_resp_2.keys = undefined;
    instructions_key_resp_2.rt = undefined;
    _instructions_key_resp_2_allKeys = [];
    // keep track of which components have finished
    practice_instructionsComponents = [];
    practice_instructionsComponents.push(instruction_text_3);
    practice_instructionsComponents.push(instructions_key_resp_2);
    
    practice_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practice_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_instructions' ---
    // get current time
    t = practice_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction_text_3* updates
    if (t >= 0.0 && instruction_text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_text_3.tStart = t;  // (not accounting for frame time here)
      instruction_text_3.frameNStart = frameN;  // exact frame index
      
      instruction_text_3.setAutoDraw(true);
    }

    
    // *instructions_key_resp_2* updates
    if (t >= 0.0 && instructions_key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_key_resp_2.tStart = t;  // (not accounting for frame time here)
      instructions_key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instructions_key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instructions_key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instructions_key_resp_2.clearEvents(); });
    }

    if (instructions_key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = instructions_key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _instructions_key_resp_2_allKeys = _instructions_key_resp_2_allKeys.concat(theseKeys);
      if (_instructions_key_resp_2_allKeys.length > 0) {
        instructions_key_resp_2.keys = _instructions_key_resp_2_allKeys[_instructions_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        instructions_key_resp_2.rt = _instructions_key_resp_2_allKeys[_instructions_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_instructions' ---
    practice_instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(instructions_key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('instructions_key_resp_2.keys', instructions_key_resp_2.keys);
    if (typeof instructions_key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('instructions_key_resp_2.rt', instructions_key_resp_2.rt);
        routineTimer.reset();
        }
    
    instructions_key_resp_2.stop();
    // the Routine "practice_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_loop;
function practice_loopLoopBegin(practice_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practice_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'linetask_prac_conditions_mod.csv',
      seed: undefined, name: 'practice_loop'
    });
    psychoJS.experiment.addLoop(practice_loop); // add the loop to the experiment
    currentLoop = practice_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practice_loop.forEach(function() {
      snapshot = practice_loop.getSnapshot();
    
      practice_loopLoopScheduler.add(importConditions(snapshot));
      practice_loopLoopScheduler.add(fixationcrossesRoutineBegin(snapshot));
      practice_loopLoopScheduler.add(fixationcrossesRoutineEachFrame());
      practice_loopLoopScheduler.add(fixationcrossesRoutineEnd(snapshot));
      practice_loopLoopScheduler.add(targetlinesRoutineBegin(snapshot));
      practice_loopLoopScheduler.add(targetlinesRoutineEachFrame());
      practice_loopLoopScheduler.add(targetlinesRoutineEnd(snapshot));
      practice_loopLoopScheduler.add(promptRoutineBegin(snapshot));
      practice_loopLoopScheduler.add(promptRoutineEachFrame());
      practice_loopLoopScheduler.add(promptRoutineEnd(snapshot));
      const loop_spatialLoopScheduler = new Scheduler(psychoJS);
      practice_loopLoopScheduler.add(loop_spatialLoopBegin(loop_spatialLoopScheduler, snapshot));
      practice_loopLoopScheduler.add(loop_spatialLoopScheduler);
      practice_loopLoopScheduler.add(loop_spatialLoopEnd);
      const loop_temporalLoopScheduler = new Scheduler(psychoJS);
      practice_loopLoopScheduler.add(loop_temporalLoopBegin(loop_temporalLoopScheduler, snapshot));
      practice_loopLoopScheduler.add(loop_temporalLoopScheduler);
      practice_loopLoopScheduler.add(loop_temporalLoopEnd);
      practice_loopLoopScheduler.add(readyRoutineBegin(snapshot));
      practice_loopLoopScheduler.add(readyRoutineEachFrame());
      practice_loopLoopScheduler.add(readyRoutineEnd(snapshot));
      practice_loopLoopScheduler.add(reminderRoutineBegin(snapshot));
      practice_loopLoopScheduler.add(reminderRoutineEachFrame());
      practice_loopLoopScheduler.add(reminderRoutineEnd(snapshot));
      practice_loopLoopScheduler.add(troubleshootingRoutineBegin(snapshot));
      practice_loopLoopScheduler.add(troubleshootingRoutineEachFrame());
      practice_loopLoopScheduler.add(troubleshootingRoutineEnd(snapshot));
      practice_loopLoopScheduler.add(request_instRoutineBegin(snapshot));
      practice_loopLoopScheduler.add(request_instRoutineEachFrame());
      practice_loopLoopScheduler.add(request_instRoutineEnd(snapshot));
      practice_loopLoopScheduler.add(practice_loopLoopEndIteration(practice_loopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var loop_spatial;
function loop_spatialLoopBegin(loop_spatialLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_spatial = new TrialHandler({
      psychoJS: psychoJS,
      nReps: spatial, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'loop_spatial'
    });
    psychoJS.experiment.addLoop(loop_spatial); // add the loop to the experiment
    currentLoop = loop_spatial;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    loop_spatial.forEach(function() {
      snapshot = loop_spatial.getSnapshot();
    
      loop_spatialLoopScheduler.add(importConditions(snapshot));
      loop_spatialLoopScheduler.add(start_xRoutineBegin(snapshot));
      loop_spatialLoopScheduler.add(start_xRoutineEachFrame());
      loop_spatialLoopScheduler.add(start_xRoutineEnd(snapshot));
      loop_spatialLoopScheduler.add(end_xRoutineBegin(snapshot));
      loop_spatialLoopScheduler.add(end_xRoutineEachFrame());
      loop_spatialLoopScheduler.add(end_xRoutineEnd(snapshot));
      loop_spatialLoopScheduler.add(pauseRoutineBegin(snapshot));
      loop_spatialLoopScheduler.add(pauseRoutineEachFrame());
      loop_spatialLoopScheduler.add(pauseRoutineEnd(snapshot));
      loop_spatialLoopScheduler.add(loop_spatialLoopEndIteration(loop_spatialLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function loop_spatialLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_spatial);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loop_spatialLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var loop_temporal;
function loop_temporalLoopBegin(loop_temporalLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_temporal = new TrialHandler({
      psychoJS: psychoJS,
      nReps: temporal, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'loop_temporal'
    });
    psychoJS.experiment.addLoop(loop_temporal); // add the loop to the experiment
    currentLoop = loop_temporal;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    loop_temporal.forEach(function() {
      snapshot = loop_temporal.getSnapshot();
    
      loop_temporalLoopScheduler.add(importConditions(snapshot));
      loop_temporalLoopScheduler.add(hg_startRoutineBegin(snapshot));
      loop_temporalLoopScheduler.add(hg_startRoutineEachFrame());
      loop_temporalLoopScheduler.add(hg_startRoutineEnd(snapshot));
      loop_temporalLoopScheduler.add(hg_midRoutineBegin(snapshot));
      loop_temporalLoopScheduler.add(hg_midRoutineEachFrame());
      loop_temporalLoopScheduler.add(hg_midRoutineEnd(snapshot));
      loop_temporalLoopScheduler.add(hg_endRoutineBegin(snapshot));
      loop_temporalLoopScheduler.add(hg_endRoutineEachFrame());
      loop_temporalLoopScheduler.add(hg_endRoutineEnd(snapshot));
      loop_temporalLoopScheduler.add(loop_temporalLoopEndIteration(loop_temporalLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function loop_temporalLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_temporal);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loop_temporalLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function practice_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practice_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practice_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var exp_loop;
function exp_loopLoopBegin(exp_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    exp_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'linetask_full_conditions.csv',
      seed: undefined, name: 'exp_loop'
    });
    psychoJS.experiment.addLoop(exp_loop); // add the loop to the experiment
    currentLoop = exp_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    exp_loop.forEach(function() {
      snapshot = exp_loop.getSnapshot();
    
      exp_loopLoopScheduler.add(importConditions(snapshot));
      exp_loopLoopScheduler.add(fixationcrossesRoutineBegin(snapshot));
      exp_loopLoopScheduler.add(fixationcrossesRoutineEachFrame());
      exp_loopLoopScheduler.add(fixationcrossesRoutineEnd(snapshot));
      exp_loopLoopScheduler.add(targetlinesRoutineBegin(snapshot));
      exp_loopLoopScheduler.add(targetlinesRoutineEachFrame());
      exp_loopLoopScheduler.add(targetlinesRoutineEnd(snapshot));
      exp_loopLoopScheduler.add(promptRoutineBegin(snapshot));
      exp_loopLoopScheduler.add(promptRoutineEachFrame());
      exp_loopLoopScheduler.add(promptRoutineEnd(snapshot));
      const loop_spatial_expLoopScheduler = new Scheduler(psychoJS);
      exp_loopLoopScheduler.add(loop_spatial_expLoopBegin(loop_spatial_expLoopScheduler, snapshot));
      exp_loopLoopScheduler.add(loop_spatial_expLoopScheduler);
      exp_loopLoopScheduler.add(loop_spatial_expLoopEnd);
      const loop_temporal_expLoopScheduler = new Scheduler(psychoJS);
      exp_loopLoopScheduler.add(loop_temporal_expLoopBegin(loop_temporal_expLoopScheduler, snapshot));
      exp_loopLoopScheduler.add(loop_temporal_expLoopScheduler);
      exp_loopLoopScheduler.add(loop_temporal_expLoopEnd);
      exp_loopLoopScheduler.add(readyRoutineBegin(snapshot));
      exp_loopLoopScheduler.add(readyRoutineEachFrame());
      exp_loopLoopScheduler.add(readyRoutineEnd(snapshot));
      exp_loopLoopScheduler.add(request_instRoutineBegin(snapshot));
      exp_loopLoopScheduler.add(request_instRoutineEachFrame());
      exp_loopLoopScheduler.add(request_instRoutineEnd(snapshot));
      exp_loopLoopScheduler.add(catchtrialsRoutineBegin(snapshot));
      exp_loopLoopScheduler.add(catchtrialsRoutineEachFrame());
      exp_loopLoopScheduler.add(catchtrialsRoutineEnd(snapshot));
      exp_loopLoopScheduler.add(breakscreenRoutineBegin(snapshot));
      exp_loopLoopScheduler.add(breakscreenRoutineEachFrame());
      exp_loopLoopScheduler.add(breakscreenRoutineEnd(snapshot));
      exp_loopLoopScheduler.add(exp_loopLoopEndIteration(exp_loopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var loop_spatial_exp;
function loop_spatial_expLoopBegin(loop_spatial_expLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_spatial_exp = new TrialHandler({
      psychoJS: psychoJS,
      nReps: spatial, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'loop_spatial_exp'
    });
    psychoJS.experiment.addLoop(loop_spatial_exp); // add the loop to the experiment
    currentLoop = loop_spatial_exp;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    loop_spatial_exp.forEach(function() {
      snapshot = loop_spatial_exp.getSnapshot();
    
      loop_spatial_expLoopScheduler.add(importConditions(snapshot));
      loop_spatial_expLoopScheduler.add(start_xRoutineBegin(snapshot));
      loop_spatial_expLoopScheduler.add(start_xRoutineEachFrame());
      loop_spatial_expLoopScheduler.add(start_xRoutineEnd(snapshot));
      loop_spatial_expLoopScheduler.add(end_xRoutineBegin(snapshot));
      loop_spatial_expLoopScheduler.add(end_xRoutineEachFrame());
      loop_spatial_expLoopScheduler.add(end_xRoutineEnd(snapshot));
      loop_spatial_expLoopScheduler.add(pauseRoutineBegin(snapshot));
      loop_spatial_expLoopScheduler.add(pauseRoutineEachFrame());
      loop_spatial_expLoopScheduler.add(pauseRoutineEnd(snapshot));
      loop_spatial_expLoopScheduler.add(loop_spatial_expLoopEndIteration(loop_spatial_expLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function loop_spatial_expLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_spatial_exp);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loop_spatial_expLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var loop_temporal_exp;
function loop_temporal_expLoopBegin(loop_temporal_expLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_temporal_exp = new TrialHandler({
      psychoJS: psychoJS,
      nReps: temporal, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'loop_temporal_exp'
    });
    psychoJS.experiment.addLoop(loop_temporal_exp); // add the loop to the experiment
    currentLoop = loop_temporal_exp;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    loop_temporal_exp.forEach(function() {
      snapshot = loop_temporal_exp.getSnapshot();
    
      loop_temporal_expLoopScheduler.add(importConditions(snapshot));
      loop_temporal_expLoopScheduler.add(hg_startRoutineBegin(snapshot));
      loop_temporal_expLoopScheduler.add(hg_startRoutineEachFrame());
      loop_temporal_expLoopScheduler.add(hg_startRoutineEnd(snapshot));
      loop_temporal_expLoopScheduler.add(hg_midRoutineBegin(snapshot));
      loop_temporal_expLoopScheduler.add(hg_midRoutineEachFrame());
      loop_temporal_expLoopScheduler.add(hg_midRoutineEnd(snapshot));
      loop_temporal_expLoopScheduler.add(hg_endRoutineBegin(snapshot));
      loop_temporal_expLoopScheduler.add(hg_endRoutineEachFrame());
      loop_temporal_expLoopScheduler.add(hg_endRoutineEnd(snapshot));
      loop_temporal_expLoopScheduler.add(loop_temporal_expLoopEndIteration(loop_temporal_expLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function loop_temporal_expLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_temporal_exp);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loop_temporal_expLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function exp_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(exp_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function exp_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var fixationcrossesComponents;
function fixationcrossesRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixationcrosses' ---
    t = 0;
    fixationcrossesClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fixationcrossesComponents = [];
    fixationcrossesComponents.push(fixation_cross);
    
    fixationcrossesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function fixationcrossesRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixationcrosses' ---
    // get current time
    t = fixationcrossesClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_cross* updates
    if (t >= 0.0 && fixation_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_cross.tStart = t;  // (not accounting for frame time here)
      fixation_cross.frameNStart = frameN;  // exact frame index
      
      fixation_cross.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_cross.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixationcrossesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixationcrossesRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixationcrosses' ---
    fixationcrossesComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Run 'End Routine' code from counter_code
    trial_counter += 1;
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var targetlinesComponents;
function targetlinesRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'targetlines' ---
    t = 0;
    targetlinesClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    targetlinesComponents = [];
    targetlinesComponents.push(targetline);
    targetlinesComponents.push(distractorline1);
    targetlinesComponents.push(distractorline2);
    
    targetlinesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function targetlinesRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'targetlines' ---
    // get current time
    t = targetlinesClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *targetline* updates
    if (t >= 0.0 && targetline.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      targetline.tStart = t;  // (not accounting for frame time here)
      targetline.frameNStart = frameN;  // exact frame index
      
      targetline.setAutoDraw(true);
    }

    frameRemains = 0.0 + durations - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (targetline.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      targetline.setAutoDraw(false);
    }
    
    if (targetline.status === PsychoJS.Status.STARTED){ // only update if being drawn
      targetline.setPos([(start + (t * jitter)), ystarttarget], false);
      targetline.setSize((t * disp), false);
    }
    
    // *distractorline1* updates
    if (t >= 0.0 && distractorline1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      distractorline1.tStart = t;  // (not accounting for frame time here)
      distractorline1.frameNStart = frameN;  // exact frame index
      
      distractorline1.setAutoDraw(true);
    }

    frameRemains = 0.0 + durationsdistractor1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (distractorline1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      distractorline1.setAutoDraw(false);
    }
    
    if (distractorline1.status === PsychoJS.Status.STARTED){ // only update if being drawn
      distractorline1.setPos([(xstartdistractor1 + (t * jitterdistractor1)), ystartdistractor1], false);
      distractorline1.setSize((t * dispdistractor1), false);
    }
    
    // *distractorline2* updates
    if (t >= 0.0 && distractorline2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      distractorline2.tStart = t;  // (not accounting for frame time here)
      distractorline2.frameNStart = frameN;  // exact frame index
      
      distractorline2.setAutoDraw(true);
    }

    frameRemains = 0.0 + durationsdistractor2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (distractorline2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      distractorline2.setAutoDraw(false);
    }
    
    if (distractorline2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      distractorline2.setPos([(xstartdistractor2 + (t * jitterdistractor2)), ystartdistractor2], false);
      distractorline2.setSize((t * dispdistractor2), false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    targetlinesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function targetlinesRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'targetlines' ---
    targetlinesComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "targetlines" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var promptComponents;
function promptRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prompt' ---
    t = 0;
    promptClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.750000);
    // update component parameters for each repeat
    prompt_text.setText(display);
    // keep track of which components have finished
    promptComponents = [];
    promptComponents.push(prompt_text);
    
    promptComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function promptRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prompt' ---
    // get current time
    t = promptClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prompt_text* updates
    if (t >= 0 && prompt_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prompt_text.tStart = t;  // (not accounting for frame time here)
      prompt_text.frameNStart = frameN;  // exact frame index
      
      prompt_text.setAutoDraw(true);
    }

    frameRemains = 0 + 0.75 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prompt_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prompt_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    promptComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function promptRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prompt' ---
    promptComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var start_xComponents;
function start_xRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'start_x' ---
    t = 0;
    start_xClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    startx.setFillColor(new util.Color([1.0, 1.0, 1.0]));
    startx.setPos(x_loc);
    startx.setLineColor(new util.Color([(- 1.0), (- 1.0), (- 1.0)]));
    // setup some python lists for storing info about the mouse_startx
    // current position of the mouse:
    mouse_startx.x = [];
    mouse_startx.y = [];
    mouse_startx.leftButton = [];
    mouse_startx.midButton = [];
    mouse_startx.rightButton = [];
    mouse_startx.time = [];
    mouse_startx.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from mouse_code_4
    
    
    
    // keep track of which components have finished
    start_xComponents = [];
    start_xComponents.push(startx);
    start_xComponents.push(mouse_startx);
    
    start_xComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function start_xRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'start_x' ---
    // get current time
    t = start_xClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *startx* updates
    if (t >= 0.0 && startx.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startx.tStart = t;  // (not accounting for frame time here)
      startx.frameNStart = frameN;  // exact frame index
      
      startx.setAutoDraw(true);
    }

    // *mouse_startx* updates
    if (t >= 0.0 && mouse_startx.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_startx.tStart = t;  // (not accounting for frame time here)
      mouse_startx.frameNStart = frameN;  // exact frame index
      
      mouse_startx.status = PsychoJS.Status.STARTED;
      mouse_startx.mouseClock.reset();
      prevButtonState = mouse_startx.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_startx.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_startx.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [startx]) {
            if (obj.contains(mouse_startx)) {
              gotValidClick = true;
              mouse_startx.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse_startx.getPos();
          mouse_startx.x.push(_mouseXYs[0]);
          mouse_startx.y.push(_mouseXYs[1]);
          mouse_startx.leftButton.push(_mouseButtons[0]);
          mouse_startx.midButton.push(_mouseButtons[1]);
          mouse_startx.rightButton.push(_mouseButtons[2]);
          mouse_startx.time.push(mouse_startx.mouseClock.getTime());
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    if (mouse_startx.isPressedIn(startx)) {
        startx.fillColor = [1.000,0.004,1.000];
    }
    
    
    
    
    
    
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    start_xComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function start_xRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'start_x' ---
    start_xComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse_startx.x) {  psychoJS.experiment.addData('mouse_startx.x', mouse_startx.x[0])};
    if (mouse_startx.y) {  psychoJS.experiment.addData('mouse_startx.y', mouse_startx.y[0])};
    if (mouse_startx.leftButton) {  psychoJS.experiment.addData('mouse_startx.leftButton', mouse_startx.leftButton[0])};
    if (mouse_startx.midButton) {  psychoJS.experiment.addData('mouse_startx.midButton', mouse_startx.midButton[0])};
    if (mouse_startx.rightButton) {  psychoJS.experiment.addData('mouse_startx.rightButton', mouse_startx.rightButton[0])};
    if (mouse_startx.time) {  psychoJS.experiment.addData('mouse_startx.time', mouse_startx.time[0])};
    if (mouse_startx.clicked_name) {  psychoJS.experiment.addData('mouse_startx.clicked_name', mouse_startx.clicked_name[0])};
    
    
    
    // the Routine "start_x" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crosses;
var end_xComponents;
function end_xRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end_x' ---
    t = 0;
    end_xClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    startx_ph.setFillColor(new util.Color([(- 1.0), (- 1.0), (- 1.0)]));
    startx_ph.setPos(x_loc);
    startx_ph.setLineColor(new util.Color([(- 1.0), (- 1.0), (- 1.0)]));
    polygon.setPos(box_loc);
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from mouse_code
    crosses = [];
    
    
    // keep track of which components have finished
    end_xComponents = [];
    end_xComponents.push(startx_ph);
    end_xComponents.push(polygon);
    end_xComponents.push(mouse);
    
    end_xComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var cross;
function end_xRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end_x' ---
    // get current time
    t = end_xClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *startx_ph* updates
    if (t >= 0.0 && startx_ph.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startx_ph.tStart = t;  // (not accounting for frame time here)
      startx_ph.frameNStart = frameN;  // exact frame index
      
      startx_ph.setAutoDraw(true);
    }

    
    // *polygon* updates
    if (t >= 0.0 && polygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon.tStart = t;  // (not accounting for frame time here)
      polygon.frameNStart = frameN;  // exact frame index
      
      polygon.setAutoDraw(true);
    }

    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [polygon]) {
            if (obj.contains(mouse)) {
              gotValidClick = true;
              mouse.clicked_name.push(obj.name)
            }
          }
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // Run 'Each Frame' code from mouse_code
    if (mouse.isPressedIn(polygon)) {
        cross = new visual.ShapeStim({win: psychoJS.window, pos: mouse.getPos(), vertices: 'cross', size: [50, 50], ori: 45.0, fillColor: [1.000, 1.000, 1.000]});
        cross.setAutoDraw(true);
        crosses.append(cross);
    }
    
    
    
    
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    end_xComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_xRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end_x' ---
    end_xComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    if (mouse.x) {  psychoJS.experiment.addData('mouse.x', mouse.x[0])};
    if (mouse.y) {  psychoJS.experiment.addData('mouse.y', mouse.y[0])};
    if (mouse.leftButton) {  psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton[0])};
    if (mouse.midButton) {  psychoJS.experiment.addData('mouse.midButton', mouse.midButton[0])};
    if (mouse.rightButton) {  psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton[0])};
    if (mouse.time) {  psychoJS.experiment.addData('mouse.time', mouse.time[0])};
    if (mouse.clicked_name) {  psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name[0])};
    
    
    
    // the Routine "end_x" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var pauseComponents;
function pauseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'pause' ---
    t = 0;
    pauseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.750000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from mouse_code_6
    
    
    
    startx_4.setFillColor(new util.Color([(- 1.0), (- 1.0), (- 1.0)]));
    startx_4.setPos(x_loc);
    startx_4.setLineColor(new util.Color([(- 1.0), (- 1.0), (- 1.0)]));
    // keep track of which components have finished
    pauseComponents = [];
    pauseComponents.push(startx_4);
    
    pauseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function pauseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'pause' ---
    // get current time
    t = pauseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    
    
    
    // *startx_4* updates
    if (t >= 0.0 && startx_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startx_4.tStart = t;  // (not accounting for frame time here)
      startx_4.frameNStart = frameN;  // exact frame index
      
      startx_4.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.75 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (startx_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      startx_4.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    pauseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function pauseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pause' ---
    pauseComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Run 'End Routine' code from mouse_code_6
    for (var across, _pj_c = 0, _pj_a = crosses, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        across = _pj_a[_pj_c];
        across.setAutoDraw(false);
    }
    
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var hg_startComponents;
function hg_startRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'hg_start' ---
    t = 0;
    hg_startClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    hg_bottom.setFillColor(new util.Color([0.004, 0.004, 0.004]));
    hg_bottom.setPos(bottom_hg_loc);
    hg_bottom.setLineColor(new util.Color([0.004, 0.004, 0.004]));
    // setup some python lists for storing info about the mouse_hg
    mouse_hg.clicked_name = [];
    gotValidClick = false; // until a click is received
    hg_top.setFillColor(new util.Color([0.004, 0.004, 0.004]));
    hg_top.setPos(top_hg_loc);
    hg_top.setLineColor(new util.Color([0.004, 0.004, 0.004]));
    // keep track of which components have finished
    hg_startComponents = [];
    hg_startComponents.push(hg_bottom);
    hg_startComponents.push(mouse_hg);
    hg_startComponents.push(hg_top);
    
    hg_startComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function hg_startRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'hg_start' ---
    // get current time
    t = hg_startClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *hg_bottom* updates
    if (t >= 0.0 && hg_bottom.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      hg_bottom.tStart = t;  // (not accounting for frame time here)
      hg_bottom.frameNStart = frameN;  // exact frame index
      
      hg_bottom.setAutoDraw(true);
    }

    // *mouse_hg* updates
    if (t >= 0.0 && mouse_hg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_hg.tStart = t;  // (not accounting for frame time here)
      mouse_hg.frameNStart = frameN;  // exact frame index
      
      mouse_hg.status = PsychoJS.Status.STARTED;
      mouse_hg.mouseClock.reset();
      prevButtonState = mouse_hg.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_hg.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_hg.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [hg_bottom, hg_top]) {
            if (obj.contains(mouse_hg)) {
              gotValidClick = true;
              mouse_hg.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *hg_top* updates
    if (t >= 0.0 && hg_top.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      hg_top.tStart = t;  // (not accounting for frame time here)
      hg_top.frameNStart = frameN;  // exact frame index
      
      hg_top.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    hg_startComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function hg_startRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'hg_start' ---
    hg_startComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse_hg.getPos();
    _mouseButtons = mouse_hg.getPressed();
    psychoJS.experiment.addData('mouse_hg.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_hg.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_hg.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_hg.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_hg.rightButton', _mouseButtons[2]);
    if (mouse_hg.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_hg.clicked_name', mouse_hg.clicked_name[0]);}
    // the Routine "hg_start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var StartTime;
var hg_midComponents;
function hg_midRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'hg_mid' ---
    t = 0;
    hg_midClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    hg_bottom_2.setFillColor(new util.Color([(- 1.0), (- 1.0), (- 1.0)]));
    hg_bottom_2.setPos(bottom_hg_loc);
    hg_bottom_2.setLineColor(new util.Color([(- 1.0), (- 1.0), (- 1.0)]));
    // setup some python lists for storing info about the mouse_hg_2
    mouse_hg_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    hg_top_2.setFillColor(new util.Color([(- 1.0), (- 1.0), (- 1.0)]));
    hg_top_2.setPos(top_hg_loc);
    hg_top_2.setLineColor(new util.Color([(- 1.0), (- 1.0), (- 1.0)]));
    // Run 'Begin Routine' code from code_5
    StartTime = GlobalClock.getTime();
    psychoJS.experiment.addData("StartTime", StartTime);
    
    // keep track of which components have finished
    hg_midComponents = [];
    hg_midComponents.push(hg_bottom_2);
    hg_midComponents.push(mouse_hg_2);
    hg_midComponents.push(hg_top_2);
    
    hg_midComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function hg_midRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'hg_mid' ---
    // get current time
    t = hg_midClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *hg_bottom_2* updates
    if (t >= 0.0 && hg_bottom_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      hg_bottom_2.tStart = t;  // (not accounting for frame time here)
      hg_bottom_2.frameNStart = frameN;  // exact frame index
      
      hg_bottom_2.setAutoDraw(true);
    }

    // *mouse_hg_2* updates
    if (t >= 0.0 && mouse_hg_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_hg_2.tStart = t;  // (not accounting for frame time here)
      mouse_hg_2.frameNStart = frameN;  // exact frame index
      
      mouse_hg_2.status = PsychoJS.Status.STARTED;
      mouse_hg_2.mouseClock.reset();
      prevButtonState = mouse_hg_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_hg_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_hg_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [hg_bottom_2, hg_top_2]) {
            if (obj.contains(mouse_hg_2)) {
              gotValidClick = true;
              mouse_hg_2.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *hg_top_2* updates
    if (t >= 0.0 && hg_top_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      hg_top_2.tStart = t;  // (not accounting for frame time here)
      hg_top_2.frameNStart = frameN;  // exact frame index
      
      hg_top_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    hg_midComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var EndTime;
function hg_midRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'hg_mid' ---
    hg_midComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse_hg_2.getPos();
    _mouseButtons = mouse_hg_2.getPressed();
    psychoJS.experiment.addData('mouse_hg_2.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_hg_2.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_hg_2.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_hg_2.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_hg_2.rightButton', _mouseButtons[2]);
    if (mouse_hg_2.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_hg_2.clicked_name', mouse_hg_2.clicked_name[0]);}
    // Run 'End Routine' code from code_5
    EndTime = GlobalClock.getTime();
    psychoJS.experiment.addData("EndTime", EndTime);
    
    // the Routine "hg_mid" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var hg_endComponents;
function hg_endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'hg_end' ---
    t = 0;
    hg_endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    hg_bottom_3.setFillColor(new util.Color([0.004, 0.004, 0.004]));
    hg_bottom_3.setPos(bottom_hg_loc);
    hg_bottom_3.setLineColor(new util.Color([0.004, 0.004, 0.004]));
    hg_top_3.setFillColor(new util.Color([0.004, 0.004, 0.004]));
    hg_top_3.setPos(top_hg_loc);
    hg_top_3.setLineColor(new util.Color([0.004, 0.004, 0.004]));
    // keep track of which components have finished
    hg_endComponents = [];
    hg_endComponents.push(hg_bottom_3);
    hg_endComponents.push(hg_top_3);
    
    hg_endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function hg_endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'hg_end' ---
    // get current time
    t = hg_endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *hg_bottom_3* updates
    if (t >= 0.0 && hg_bottom_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      hg_bottom_3.tStart = t;  // (not accounting for frame time here)
      hg_bottom_3.frameNStart = frameN;  // exact frame index
      
      hg_bottom_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (hg_bottom_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      hg_bottom_3.setAutoDraw(false);
    }
    
    // *hg_top_3* updates
    if (t >= 0.0 && hg_top_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      hg_top_3.tStart = t;  // (not accounting for frame time here)
      hg_top_3.frameNStart = frameN;  // exact frame index
      
      hg_top_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (hg_top_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      hg_top_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    hg_endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function hg_endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'hg_end' ---
    hg_endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_allKeys;
var readyComponents;
function readyRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ready' ---
    t = 0;
    readyClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    readyComponents = [];
    readyComponents.push(text);
    readyComponents.push(instruction_req);
    readyComponents.push(key_resp);
    
    readyComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function readyRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ready' ---
    // get current time
    t = readyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *instruction_req* updates
    if (t >= 0.0 && instruction_req.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_req.tStart = t;  // (not accounting for frame time here)
      instruction_req.frameNStart = frameN;  // exact frame index
      
      instruction_req.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space', 'i', 't'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    readyComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function readyRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ready' ---
    readyComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "ready" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_6_allKeys;
var reminderComponents;
function reminderRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder' ---
    t = 0;
    reminderClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // keep track of which components have finished
    reminderComponents = [];
    reminderComponents.push(text_4);
    reminderComponents.push(key_resp_6);
    
    reminderComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function reminderRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder' ---
    // get current time
    t = reminderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // Run 'Each Frame' code from code_3
    if ((trial_counter !== 2)) {
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    reminderComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminderRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder' ---
    reminderComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_6.corr, level);
    }
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // the Routine "reminder" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_11_allKeys;
var troubleshootingComponents;
function troubleshootingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'troubleshooting' ---
    t = 0;
    troubleshootingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_11.keys = undefined;
    key_resp_11.rt = undefined;
    _key_resp_11_allKeys = [];
    // keep track of which components have finished
    troubleshootingComponents = [];
    troubleshootingComponents.push(troubleshooting_text);
    troubleshootingComponents.push(key_resp_11);
    
    troubleshootingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function troubleshootingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'troubleshooting' ---
    // get current time
    t = troubleshootingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *troubleshooting_text* updates
    if (t >= 0.0 && troubleshooting_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      troubleshooting_text.tStart = t;  // (not accounting for frame time here)
      troubleshooting_text.frameNStart = frameN;  // exact frame index
      
      troubleshooting_text.setAutoDraw(true);
    }

    // Run 'Each Frame' code from code_trblsht
    if ((key_resp.keys[0] !== "t")) {
        continueRoutine = false;
    }
    
    
    // *key_resp_11* updates
    if (t >= 0.0 && key_resp_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_11.tStart = t;  // (not accounting for frame time here)
      key_resp_11.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_11.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.clearEvents(); });
    }

    if (key_resp_11.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_11.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_11_allKeys = _key_resp_11_allKeys.concat(theseKeys);
      if (_key_resp_11_allKeys.length > 0) {
        key_resp_11.keys = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].name;  // just the last key pressed
        key_resp_11.rt = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    troubleshootingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function troubleshootingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'troubleshooting' ---
    troubleshootingComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_11.corr, level);
    }
    psychoJS.experiment.addData('key_resp_11.keys', key_resp_11.keys);
    if (typeof key_resp_11.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_11.rt', key_resp_11.rt);
        routineTimer.reset();
        }
    
    key_resp_11.stop();
    // the Routine "troubleshooting" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_9_allKeys;
var request_instComponents;
function request_instRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'request_inst' ---
    t = 0;
    request_instClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_9.keys = undefined;
    key_resp_9.rt = undefined;
    _key_resp_9_allKeys = [];
    // keep track of which components have finished
    request_instComponents = [];
    request_instComponents.push(instruction_re_text);
    request_instComponents.push(key_resp_9);
    
    request_instComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function request_instRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'request_inst' ---
    // get current time
    t = request_instClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction_re_text* updates
    if (t >= 0.0 && instruction_re_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_re_text.tStart = t;  // (not accounting for frame time here)
      instruction_re_text.frameNStart = frameN;  // exact frame index
      
      instruction_re_text.setAutoDraw(true);
    }

    // Run 'Each Frame' code from code_ir
    if ((key_resp.keys[0] !== "i")) {
        continueRoutine = false;
    }
    
    
    // *key_resp_9* updates
    if (t >= 0.0 && key_resp_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_9.tStart = t;  // (not accounting for frame time here)
      key_resp_9.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_9.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.clearEvents(); });
    }

    if (key_resp_9.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_9.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_9_allKeys = _key_resp_9_allKeys.concat(theseKeys);
      if (_key_resp_9_allKeys.length > 0) {
        key_resp_9.keys = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].name;  // just the last key pressed
        key_resp_9.rt = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    request_instComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function request_instRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'request_inst' ---
    request_instComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_9.corr, level);
    }
    psychoJS.experiment.addData('key_resp_9.keys', key_resp_9.keys);
    if (typeof key_resp_9.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_9.rt', key_resp_9.rt);
        routineTimer.reset();
        }
    
    key_resp_9.stop();
    // the Routine "request_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _practicetrialend_key_resp_allKeys;
var practicetrialendscreenComponents;
function practicetrialendscreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practicetrialendscreen' ---
    t = 0;
    practicetrialendscreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    practicetrialend_key_resp.keys = undefined;
    practicetrialend_key_resp.rt = undefined;
    _practicetrialend_key_resp_allKeys = [];
    // keep track of which components have finished
    practicetrialendscreenComponents = [];
    practicetrialendscreenComponents.push(practicetrialend_text);
    practicetrialendscreenComponents.push(practicetrialend_key_resp);
    
    practicetrialendscreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practicetrialendscreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practicetrialendscreen' ---
    // get current time
    t = practicetrialendscreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practicetrialend_text* updates
    if (t >= 0.0 && practicetrialend_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practicetrialend_text.tStart = t;  // (not accounting for frame time here)
      practicetrialend_text.frameNStart = frameN;  // exact frame index
      
      practicetrialend_text.setAutoDraw(true);
    }

    
    // *practicetrialend_key_resp* updates
    if (t >= 0.0 && practicetrialend_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practicetrialend_key_resp.tStart = t;  // (not accounting for frame time here)
      practicetrialend_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { practicetrialend_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { practicetrialend_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { practicetrialend_key_resp.clearEvents(); });
    }

    if (practicetrialend_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = practicetrialend_key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _practicetrialend_key_resp_allKeys = _practicetrialend_key_resp_allKeys.concat(theseKeys);
      if (_practicetrialend_key_resp_allKeys.length > 0) {
        practicetrialend_key_resp.keys = _practicetrialend_key_resp_allKeys[_practicetrialend_key_resp_allKeys.length - 1].name;  // just the last key pressed
        practicetrialend_key_resp.rt = _practicetrialend_key_resp_allKeys[_practicetrialend_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practicetrialendscreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practicetrialendscreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practicetrialendscreen' ---
    practicetrialendscreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(practicetrialend_key_resp.corr, level);
    }
    psychoJS.experiment.addData('practicetrialend_key_resp.keys', practicetrialend_key_resp.keys);
    if (typeof practicetrialend_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('practicetrialend_key_resp.rt', practicetrialend_key_resp.rt);
        routineTimer.reset();
        }
    
    practicetrialend_key_resp.stop();
    // the Routine "practicetrialendscreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_2_allKeys;
var catchtrialsComponents;
function catchtrialsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'catchtrials' ---
    t = 0;
    catchtrialsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    catch_text.setText(catchd);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    catchtrialsComponents = [];
    catchtrialsComponents.push(catch_text);
    catchtrialsComponents.push(key_resp_2);
    
    catchtrialsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function catchtrialsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'catchtrials' ---
    // get current time
    t = catchtrialsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *catch_text* updates
    if (t >= 0.0 && catch_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      catch_text.tStart = t;  // (not accounting for frame time here)
      catch_text.frameNStart = frameN;  // exact frame index
      
      catch_text.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['c', 'l', 's', 'space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // Run 'Each Frame' code from catch_code
    if (((trial_counter === 0) || (((trial_counter + 1) % 20) !== 0))) {
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    catchtrialsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function catchtrialsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'catchtrials' ---
    catchtrialsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "catchtrials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _break_key_resp_allKeys;
var breakscreenComponents;
function breakscreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'breakscreen' ---
    t = 0;
    breakscreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    breakscreen_text.setText('You are now half way done with the trials. You can take a quick break if you\'d like. Once you are ready to proceed with the rest of the experiment you can press "space".');
    break_key_resp.keys = undefined;
    break_key_resp.rt = undefined;
    _break_key_resp_allKeys = [];
    // keep track of which components have finished
    breakscreenComponents = [];
    breakscreenComponents.push(breakscreen_text);
    breakscreenComponents.push(break_key_resp);
    
    breakscreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function breakscreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'breakscreen' ---
    // get current time
    t = breakscreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *breakscreen_text* updates
    if (t >= 0.0 && breakscreen_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      breakscreen_text.tStart = t;  // (not accounting for frame time here)
      breakscreen_text.frameNStart = frameN;  // exact frame index
      
      breakscreen_text.setAutoDraw(true);
    }

    
    // *break_key_resp* updates
    if (t >= 0.0 && break_key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      break_key_resp.tStart = t;  // (not accounting for frame time here)
      break_key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { break_key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { break_key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { break_key_resp.clearEvents(); });
    }

    if (break_key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = break_key_resp.getKeys({keyList: ['space', 'i'], waitRelease: false});
      _break_key_resp_allKeys = _break_key_resp_allKeys.concat(theseKeys);
      if (_break_key_resp_allKeys.length > 0) {
        break_key_resp.keys = _break_key_resp_allKeys[_break_key_resp_allKeys.length - 1].name;  // just the last key pressed
        break_key_resp.rt = _break_key_resp_allKeys[_break_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // Run 'Each Frame' code from code_2
    if ((trial_counter !== 81)) {
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    breakscreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function breakscreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'breakscreen' ---
    breakscreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(break_key_resp.corr, level);
    }
    psychoJS.experiment.addData('break_key_resp.keys', break_key_resp.keys);
    if (typeof break_key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('break_key_resp.rt', break_key_resp.rt);
        routineTimer.reset();
        }
    
    break_key_resp.stop();
    // the Routine "breakscreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var end_screenComponents;
function end_screenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end_screen' ---
    t = 0;
    end_screenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    end_screenComponents = [];
    end_screenComponents.push(text_7);
    
    end_screenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function end_screenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end_screen' ---
    // get current time
    t = end_screenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_7* updates
    if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_7.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    end_screenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_screenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end_screen' ---
    end_screenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
