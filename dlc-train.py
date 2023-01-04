import deeplabcut

iterations = 500000

ProjectFolderName = '//wsl$/Ubuntu-20.04/home/nghess/Hand Test-NG Hess-2022-06-30'
VideoType = '.mp4'

# Set paths
videofile_path = [ProjectFolderName + '/videos']
path_config_file = ProjectFolderName+'/config.yaml'

# Set the shuffle you want to create, train, evaluate, use for analysis, etc (1 is default):
SHUF = 1

# Create training data
# There are a lot of other arguments for this function. Might be worth trying some variations
# DLC-Live appears to run faster using MobileNetV2-0.35 networks
deeplabcut.create_training_dataset(path_config_file, net_type='resnet_50', augmenter_type='imgaug')

# Train
deeplabcut.train_network(path_config_file, shuffle=SHUF, displayiters=10, saveiters=500, maxiters=iterations)

# Evaluate
deeplabcut.evaluate_network(path_config_file, Shuffles=[SHUF], plotting=False)
