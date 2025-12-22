import glob
import cv2

def main():

    # Frames per second of the output video.
    video_fps = 2
    
    # Directory containing input images (frames).
    inputfile_path = "./images"
    
    # File extension of input images to include.
    inputfile_exp  = ".png"
    
    # Output directory and base filename (without extension).
    outputfile_path = "./"
    outputfile_name = "anyname"

    # Collect image files and sort them in ascending (lexicographic) order.
    image_files = sorted(glob.glob(inputfile_path + "/*" + inputfile_exp))

    # If no matching images are found, abort with a error message.
    if not image_files:
        print("No image files (" + inputfile_exp + ") were found in the directory " + inputfile_path)
        return
    
    # Read the first image to determine the required frame size for the video.
    image_H0, image_W0, _ = cv2.imread(image_files[0]).shape

    # Select a codec. 'mp4v' is commonly used for MP4 output.
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Construct the output filename (MP4).
    outputfile = outputfile_path + outputfile_name + ".mp4"

    # Create the VideoWriter object.
    writer = cv2.VideoWriter(outputfile, fourcc, video_fps, (image_W0, image_H0))
    if not writer.isOpened():
        print("Failed to open VideoWriter. Check codec and output path.")
        return
    
    # Loop through all images and write them as video frames.
    for image in image_files:

        frame = cv2.imread(image)
        if frame is None:
            print("Failed to read image: " + image)
            writer.release()
            return
    
        # Check whether the current image has the same resolution as the first frame.
        image_H, image_W, _ = cv2.imread(image).shape
        if image_H == image_H0 and image_W == image_W0:
            # Write the frame to the output video.
            writer.write(frame)
        else:
            # VideoWriter cannot handle variable frame sizes within one video stream.
            print("The image dimensions are not consistent.")
            print("Expected: " + str((image_W0, image_H0)) + ", got: " + str((image_W, image_H)) + " in " + image)
            writer.release()
            return

    # Finalize and close the video file properly.
    writer.release()
    print("Saved video to: " + outputfile)

if __name__ == "__main__":
    main()