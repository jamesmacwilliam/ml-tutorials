import sys
import os
import cv2

from PIL import Image

directory = sys.argv[1]
imagecount = int(sys.argv[2])

os.makedirs(directory, exist_ok=True)

video = cv2.VideoCapture(0)

filename = len(os.listdir(directory))
count = 0

while True and count < imagecount:
    filename += 1
    count += 1
    _read_flag, frame = video.read()
    im = Image.fromarray(frame, 'RGB')
    im = im.resize((128,128))
    im.save(os.path.join(directory, str(filename) + ".jpg"), "JPEG") # 0.jpg...etc

    cv2.imshow("Capturing", frame) # display webcam with `capturing` header
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
