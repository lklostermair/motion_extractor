import sys
import cv2
import numpy
import pathlib as path
import os


def main():
    file_path = sys.argv[1]
    
    if path.Path(file_path).exists() == False or file_path is None:
        print(f"File '{file_path}' is empty or doesn't exist")
        return
    

    output_path = numpy.concat(file_path, "_motion")

    cap = cv2.VideoCapture(filename=file_path)
    if not cap.isOpened():
        print("Failed to open file")
        return
    
    print("Success")

    return

if __name__ == "__main__":
os.system('echo "motion_extractor.py home/lukas/Videos/Screencasts/')