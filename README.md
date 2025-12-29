# Python_images_to_video
Convert a time-ordered image sequence into a video using Python and OpenCV.

## Overview
This repository provides a simple Python script that converts a sequence of images stored in a directory into a video file (MP4 format) using OpenCV.
The images are assumed to represent a time series and must all have the same resolution.

<table>
  <tr>
  </tr>
  <tr>
    <td><img src="./images/images_000.png" width="100"></td>
    <td><img src="./images/images_001.png" width="100"></td>
    <td><img src="./images/images_002.png" width="100"></td>
    <td><img src="./images/images_003.png" width="100"></td>
    <td><img src="./images/images_004.png" width="100"></td>
  </tr>
  <tr>
    <td><img src="./images/images_005.png" width="100"></td>
    <td><img src="./images/images_006.png" width="100"></td>
    <td><img src="./images/images_007.png" width="100"></td>
    <td><img src="./images/images_008.png" width="100"></td>
    <td><img src="./images/images_009.png" width="100"></td>
  </tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  <tr>
  
  </tr>
</table>

&dArr;


https://github.com/user-attachments/assets/03583c5d-67fb-427f-9155-7d2e90616824



<!-- <video src="./anyname.mp4" controls="true" width="100"></video> -->

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
    images_001.png
    images_002.png
    images_003.png
    ...
```

- All input images must be stored in the ```images/``` directory.
- Filenames should be sortable in time order (e.g., zero-padded numbering).

## Usage
Run the script from the repository root:
```bash
python images2video.py
```

By default:

- Input directory: ```./images```
- Image format: ```.png```
- Output directory: ```./```
- Output file: ```anyname.mp4```
- Frame rate: ```2 fps```

These parameters can be modified directly in the script:

```bash
video_fps = 2
image_files = sorted(glob.glob("./images/*.png"))
outputfile = "./anyname.mp4"
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
images_001.png
images_002.png
images_003.png
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
