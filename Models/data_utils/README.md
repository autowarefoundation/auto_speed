## augmentations.py
Image augmentation is an essential part of training visual neural networks. It helps harden the network to various noise effects during training and helps to reduce data over-fitting. The [albumentations library](https://albumentations.ai/) is used to create different image augmentations effects simulation weather, debris, lens effects, noise, colour shifting, and mixing of image patches

![Augmentations Network Diagram](../../Media/Augmentations.jpg)

## check_data.py
Helper class to perform a sanity check on data for processing, ensuring that data is read and that number of ground-truth samples match the number of training images

## load_data_scene_seg.py
Helper class for the [auto_speed neural network]() to load dataset
