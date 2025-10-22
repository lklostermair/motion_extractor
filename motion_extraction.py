import sys
import cv2
import numpy
import pathlib as path


def main():
    # define file path
    file_path = sys.argv[2]
    
    if path(file_path).exists() == False or file_path is None:

