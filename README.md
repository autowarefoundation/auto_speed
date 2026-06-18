# AutoSpeed - In-path objects detection
[![Watch the Video](/Media/auto_speed_thumbnail.jpg)](https://drive.google.com/file/d/1ehH3nRKsZLmPqZsqoqFuwyx6HCy2EVxe/preview)

For autonomous cruise control applications, it is crucial to maintain a safe following distance from the vehicle in front, known as the closest-in-path object. Detecting the closest-in-path object therefore becomes a very important task for any self-driving or driver assitance application, as it also supports important safety features such as forward collision warning and autonomous emergency braking. The AutoSpeed network is a bounding box detection model inspired by the YOLOv11 architecture, in which the backbone c3k2 blocks are substitued by a custom designed 'context' block for improved overall scene understanding.

The AutoSpeed model detects all foreground objects and classifies objects into three categories depending on the object's position with respect to the predicted future driving path of the ego-car:

- objects directly within the future driving path of the ego-car 
- objects cutting-in/cutting-out of the future driving path of the ego-car
- objects outside of the future driving path of the ego-car

### Performance Results

The AutoSpeed 2.0 network is trained on the [OpenLane](https://github.com/OpenDriveLab/OpenLane) dataset on the CIPO detection task. We modify the ground-truth labels by merging 'Level 3' and 'Level 4' category objects in the ground truth dataset into a single class. We use a 90:10 ratio for train:val split, and we achieve a **mAP@50 score of 0.74** and a **mAP score of 0.56** on validation data. We also provide the INT8 quantized version of the AutoSpeed 2.0 network which achieves a **mAP@50 score of 0.73** and a **mAP score of 0.54**.

## Model variants
The AutoSpeed network is trained in two variants, the original AutoSpeed network processess frames in square aspect ratio with size 640px by 640px. AutoSpeed 2.0 processess frames in a 2:1 aspect ratio with size 512px by 1024 px, allowing for objects to be detected further away and a wider viewing angle of the scene which is more suited to autonomous driving applications. We recommend you work with AutoSpeed 2.0 for new applications and developments.

**AutoSpeed 2.0 model weights - 2:1 aspect ratio, 512px by 1024px input image**
- [Link to Download Pytorch Model Weights *.pth](https://drive.google.com/file/d/1L8oiuszUKFmLZxsgIp1wtzgSkj2pr6n7/view?usp=drive_link)
- [Link to Download ONNX FP32 Weights *.onnx](https://drive.google.com/file/d/1bKYsnKbHD8DvQB2w3x6yu0Htup4KL2l5/view?usp=drive_link)
- [Link to Download ONNX INT8 Weights *.onnx](https://drive.google.com/file/d/1hewlP5VILrUTY4t7NBhT-iNn3j4KF55E/view?usp=sharing)

AutoSpeed model weights - 1:1 aspect ratio, 640px by 640px input image
- [Link to Download Pytorch Model Weights (*.pth)](https://drive.google.com/file/d/1iD-LKf5wSuvf0F5OHVHH3znGEvSIS8LY/view?usp=drive_link)
- [Link to Download ONNX FP32 Moel Height (*.onnx)](https://drive.google.com/file/d/1Zhe8uXPbrPr8cvcwHkl1Hv0877HHbxbB/view?usp=drive_link)

## Get Started

To easily try out the model on your own images and videos, please follow the steps in the [tutorial](tutorial.ipynb). For the best results, please ensure that your input video matches the aspect ratio of the model.

### Tutorial

The tutorial walk you through how to download model weights, run inference on test images and videos, and train the model from scratch or using our pre-trained checkpoints, on our prepared datasets, or your own data.

![Watch the Video](./Media/auto_speed.gif)

#### Test resources

Example images and videos are provided in the `Media` directory, which you can use to easily try out these networks (they are also being used in each of the tutorial notebooks by default).

**Note:** 

- All of our networks are trained with a single monocular camera, and only require single-camera images to run. 
- For best results, please ensure that your camera image is 2:1 aspect ratio, and that the ego car hood/bonnet is not visible in the camera image which you provided to the network.
- Please also try and ensure that your camera is mounted similar to typical dash-cam setups. In particular:
    - Facing forward.
    - Center-aligned to the vehicle.
    - Approximately mounted near the top of the wind screen.

#### Compatibility

Tested with Python 3.10.12.

(Additional Python distributions will likely also be compatible)
