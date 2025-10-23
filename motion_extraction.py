import sys
import cv2
import numpy
import pathlib as path
import os
from tqdm import tqdm


def main():
    file_path = path.Path(sys.argv[1])
    
    if file_path.exists() == False or file_path is None:
        print(f"File '{file_path}' is empty or doesn't exist")
        return
    
    if not path.Path("outputs").exists():
        os.mkdir("outputs")
        print("Directory created at: outputs")

    output_path = "outputs/" +file_path.stem + "_motion.mp4"

    cap = cv2.VideoCapture(filename=file_path)
    if not cap.isOpened():
        print("Failed to open file")
        return
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(3))
    height = int(cap.get(4))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    out = cv2.VideoWriter(filename=output_path, fourcc=fourcc, fps=fps, frameSize=(width, height))

    _, prev_frame = cap.read()
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

    first_frame = True

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        curr_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        diff = cv2.absdiff(prev_gray, curr_gray)
        _, diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
        processed_frame = cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR)
        
        if not first_frame:
            out.write(processed_frame)
        first_frame = False
        
        prev_gray = curr_gray
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Success")

    return

if __name__ == "__main__":
    main()