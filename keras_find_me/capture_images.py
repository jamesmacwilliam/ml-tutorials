import sys
import os
import cv2

from PIL import Image

directory = sys.argv[1]
imagecount = int(sys.argv[2])

os.makedirs(directory, exist_ok=True)

video = cv2.VideoCapture(0)
