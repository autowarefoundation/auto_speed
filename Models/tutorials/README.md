# Tutorials for Autoware VisionPilot's End-to-End Models

<div align="center">
<img src="assets/tutorial_index.gif" width="50%">
</div>

## Description

This directory contains Python notebook tutorials to help you get started with the AI models which we have designed in this project.

The tutorials walk you through how to download model weights, run inference on test images and videos, and train the models from scratch or using our pre-trained checkpoints, on our prepared datasets, or your own data.

We provide 5 tutorials where each tutorial corresponds to a specific AI model:
- `AutoSpeed.ipynb` : AutoSpeed - detects bounding boxes on foreground objects and determines the closest-in-path-object (CIPO), cut-in objects, and out-of-path objects.
- `DomainSeg.ipynb` : DomainSeg - performs semantic segmentation of roadwork objects such as traffic cones, traffic barrels, road barriers, etc.
- `EgoLanes.ipynb` : EgoLanes - performs semantic segmentation of lane boundaries, including left egoline, right egoline, and other lines.
- `Scene3D.ipynb` : Scene3D - performs relative depth estimation of the front scene, indicating which pixels are closer vs. further away from the camera.
- `SceneSeg.ipynb` : SceneSeg - performs semantic segmentation of all foreground objects, including cars, pedestrians, etc.

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