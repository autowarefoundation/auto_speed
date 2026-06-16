# Visualizations
Contains scripts to run inference using trained models and create single image visualization or video visualization

# Examples

## image_visualization.py
Read an image using OpenCV, run the network and visualize the output and display in an OpenCV window

### Example usage

```bash
  python3 image_visualization.py -p /path/to/AutoSpeed/weights.pth -i /path/to/image.jpg
```
### Parameters:

*-p , --model_checkpoint_path* : path to model weights *.pth* file

*-i , --input_image_filepath* : path input image to be processed and visualized (.jpg and .png formats supported)

## video_visualization.py
Read a video file using OpenCV, run the network and visualize the output and save the visualization frames as a video in *.avi* format, optionally display in-progress frames in an OpenCV window

### Example usage

```bash
  python3 video_visualization.py -p /path/to/AutoSpeed/weights.pth -i /path/to/raw_video.mp4 -o /path/to/output/video_name -v
```
### Parameters:

*-p , --model_checkpoint_path* : path to model weights *.pth* file

*-i , --video_filepath* : path to input video which will be processed

*-o , --output_file* : path to output video visualization file, must include output file name

*-v , --vis* : flag for whether to show frame by frame visualization while processing is occuring