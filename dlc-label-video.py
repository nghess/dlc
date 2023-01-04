import deeplabcut

ProjectFolderName = 'D:/Smear Bulb Data/LEDtracking-Aldis-2022-05-06'
VideoType = '.mp4'

# Set paths
videofile_path = [ProjectFolderName+'/videos']
path_config_file = ProjectFolderName+'/config.yaml'
dfolder = ProjectFolderName+'/labeled_video'

# Set the shuffle you want to create, train, evaluate, use for analysis, etc (1 is default):
SHUF = 1

# Create labeled video
deeplabcut.create_labeled_video(path_config_file, videofile_path, videotype=VideoType, filtered=True)

if __name__ == '__main__':
    deeplabcut.freeze_support()

