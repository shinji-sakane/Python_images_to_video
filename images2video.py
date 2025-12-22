import glob
import cv2

def main():

    video_fps = 2
    inputfile_path = "./images"
    inputfile_exp  = ".png"
    outputfile_path = "./"
    outputfile_name = "anyname"

    image_files = sorted(glob.glob(inputfile_path + "/*" + inputfile_exp))

    if not image_files:
        print("No image files (" + inputfile_exp + ") were found in the directory " + inputfile_path)
        return
    
    image_H0, image_W0, _ = cv2.imread(image_files[0]).shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    outputfile = outputfile_path + outputfile_name + ".mp4"
    writer = cv2.VideoWriter(outputfile, fourcc, video_fps, (image_W0, image_H0))

    for image in image_files:
        image_H, image_W, _ = cv2.imread(image).shape

        if image_H == image_H0 and image_W == image_W0:

            frame = cv2.imread(image)
            writer.write(frame)

        else:
            print("The image resolutions are not consistent.")
            return

    writer.release()

if __name__ == "__main__":
    main()