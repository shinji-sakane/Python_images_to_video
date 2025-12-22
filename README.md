# Python_images_to_video
Convert a time-ordered image sequence into a video using Python and OpenCV.

## Overview
This repository provides a simple Python script that converts a sequence of images stored in a directory into a video file (MP4 format) using OpenCV.
The images are assumed to represent a time series and must all have the same resolution.

## Requirements
- Python 3.x
- OpenCV (cv2)

Install OpenCV using ```pip```:

### With administrator privileges
```bash
pip install opencv-python
```

### Without administrator privileges
```bash
pip install --user opencv-python
```

## Directory Structure

Example:
```bash
Python_images_to_video/
  images2video.py
  images/
    images_0001.png
    images_0002.png
    images_0003.png
    ...
```

- All input images must be stored in the images/ directory.
- Filenames should be sortable in time order (e.g., zero-padded numbering).

## Usage
Run the script from the repository root:
```bash
python images2video.py
```

By default:

- Input directory: ./images
- Image format: .png
- Output file: anyname.mp4
- Frame rate: 2 fps

These parameters can be modified directly in the script:

```bash
video_fps = 2
inputfile_path = "./images"
inputfile_exp  = ".png"
outputfile_path = "./"
outputfile_name = "anyname"
```

## Notes and Limitations
### Image resolution

All images must have identical dimensions (width and height).
If inconsistent image sizes are detected, the script stops with the message:
```bash
The image dimensions are not consistent.
```
If automatic resizing is required, the script must be modified accordingly.

### Image ordering

Images are sorted lexicographically using glob and sorted().
To ensure correct time ordering, use filenames such as:
```bash
images_0001.png
images_0002.png
images_0003.png
...
```

### Codec

The script uses the mp4v codec to generate an MP4 file.
If the output video cannot be played on your system, try a different codec (e.g., XVID) and change the file extension accordingly.

## Output

Output video file: anyname.mp4

Location: repository root (default)

## License

This project is licensed under the MIT License.