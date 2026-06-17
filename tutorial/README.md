# Tutorial for Autoware Foundation auto_speed model

![Watch the Video](assets/auto_speed.gif)


## Description

This directory contains Python notebook tutorial to help you get started with the auto_speed model.

The tutorial walk you through how to download model weights, run inference on test images and videos, and train the model from scratch or using our pre-trained checkpoints, on our prepared datasets, or your own data.

## Test assets

We provided example images and videos in the `assets` directory, which you can use to easily try out these networks (they are also being used in each of the tutorial notebooks by default).

**Note:** 

- All of our networks are trained with a single monocular camera, and only require single-camera images to run. 
- For best results, please ensure that your camera image is 2:1 aspect ratio, and that the ego car hood/bonnet is not visible in the camera image which you provided to the network.
- Please also try and ensure that your camera is mounted similar to typical dash-cam setups. In particular:
    - Facing forward.
    - Center-aligned to the vehicle.
    - Approximately mounted near the top of the wind screen.

## Compatibility

Tested with Python 3.10.12.

(Additional Python distributions will likely also be compatible)