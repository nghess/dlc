import deeplabcut

ProjectFolderName = 'D:\Smear Bulb Data\LEDtracking-Aldis-2022-05-06'
VideoType = '.mp4'

# Set paths
videofile_path = [ProjectFolderName+'/videos']
path_config_file = ProjectFolderName+'/config.yaml'

# Set the shuffle you want to create, train, evaluate, use for analysis, etc (1 is default):
SHUF = 1

# Analyze
deeplabcut.analyze_videos(path_config_file, videofile_path, videotype=VideoType, shuffle=SHUF)

# Smooth
deeplabcut.filterpredictions(path_config_file, videofile_path, videotype=VideoType, shuffle=SHUF)

# Plot points
deeplabcut.plot_trajectories(path_config_file, videofile_path, videotype=VideoType, shuffle=SHUF, filtered=True)
