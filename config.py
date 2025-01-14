# Debug settings
debug_level =  0  # 0 (off), 1 (info), 2 (detailed)
debug_max = 2     # max debug level

# Hardware settings
video_capture_device = 0 # TODO: make this better

# Virtual shooting range and session options
real_range_length = 3       # (units must match simulated range length)
shot_calibre = 5.6          # mm (0.22")
session_name = 'Practice 13/01/23'
auto_reset = True           # reset after shot taken
auto_reset_time = 3         # Number of seconds after the shot before resetting
# calibration_shots_req = 3 # Number of shots to average to calibrate the system (deprecated)
shots_per_series = 5        # How many shots before auto-resetting
series_reset_pause = 3      # seconds to pause before starting a new series
target_index = 0            # Target to use (see below)
inward = True               # How gauging
outward = not inward        # is defined

# Target dimensions
# (name, diameter (mm), filename, simulated_range_length, (ring scores hi->low), gauging)
# TODO: add dimensions for scoring rings
target = (('25 yard prone', 51.39, '1989 25yard Outward Gauging.png', 25, (12.92, 20.23, 27.55, 34.86, 42.18, 49.49, 56.81, 64.12, 71.44, 78.75), outward),
          ('50 yard prone', 102.79, '1989 50yard Inward Gauging.png', 50, (9.03, 23.66, 38.29, 52.92, 67.55, 82.18, 96.81), inward),
          ('100 yard prone', 205.55, '1989 100yard Inward Gauging.png', 100, (26.48, 57.32, 88.16, 119.00, 149.84, 180.68, 211.52, 242.36, 273.20), inward))

target_name = target[target_index][0]
target_diameter = target[target_index][1]
target_filename = target[target_index][2]
simulated_range_length = target[target_index][3]
target_scoring_rings = target[target_index][4]
target_scoring_scheme = target[target_index][5]

# Scaling variables
scale_factor = simulated_range_length / real_range_length
  
# video capture object
captured_image_flip_needed = False # Whether the camera is mounted upside down
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
display_shot_time = True # Overlay a timer onto the trace

# Initialise tuples and variables
composite_shots = []
calibration_shots = []

# Coordinates of the 'fired' shot
recorded_shot_loc = []

# Calibration / scaling
calib_XY = (0, 0)

# Font details
font_thickness = 1
line_type = 1

# Fancy printing of 'calibration'
calib_text_red = 255
d_calib_text_red = -2
calib_text_red_min = 127

# Sound capture parameters
audio_chunk_size = 4096