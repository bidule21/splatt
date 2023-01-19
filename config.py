# Debug settings
debug_level =  0  # 0 (off), 1 (info), 2 (detailed)
debug_max = 2     # max debug level

# Virtual shooting range and session options
real_range_length = 5       # (units must match simulated range length)
shot_calibre = 5.6          # mm (0.22")
session_name = 'Practice 13/01/23'
auto_reset = True           # reset after shot taken
auto_reset_time = 1         # Number of seconds after the shot before resetting
target_index = 0

# Target dimensions
# (name, diameter (mm), filename, simulated_range_length)
# TODO: add dimensions for scoring rings
target = (('25 yard prone', 51.39, '1989 25yard Outward Gauging.png', 25),
          ('50 yard prone', 102.79, '1989 50yard Inward Gauging.png', 50),
          ('100 yard prone', 205.55, '1989 100yard Inward Gauging.png', 100))

target_name = target[target_index][0]
target_diameter = target[target_index][1]
target_filename = target[target_index][2]
simulated_range_length = target[target_index][3]

# Scaling variables
scale_factor = simulated_range_length / real_range_length
  
# video capture object
captured_image_flip_needed = True # Whether the camera is mounted upside down
video_frames = []

# Recording options
record_video = False # (Do not set to true here)
video_output_file = 'output.avi'
composite_output_file = 'composite.png'

# Audio and video processing options
blur_radius = 11          # must be an odd number, or else GaussianBlur will fail. Lower is better for picking out point sources
detection_threshold = 50  # Trigger value to detect the reference point
click_threshold = 50      # audio level that triggers a 'shot'

# Plotting colours and options
init_line_colour = (0, 0, 255, 0) # (Blue, Green, Red)
shot_colour = (255, 0, 255)       # Magenta
line_thickness = 2
colour_change_rate = (0, 15, -15) # Rates of colour change per frame (b, g, r)

# Initialise tuples and variables
line_colour = []
stored_trace = []
composite_shots = []
start_trace = 1
shots_fired = -1 # The 0th is the calibration shot TODO: reset on keypress
auto_reset_time_expired = False

# Coordinates of the 'fired' shot
recorded_shot_loc = []

# Calibration / scaling
calib_XY = (0, 0)

# Font details
font_thickness = 1
line_type = 1

# Sound capture parameters
audio_chunk_size = 4096