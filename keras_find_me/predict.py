from keras.models import load_model
import cv2
import numpy as np
from PIL import Image

model = load_model('model.h5')

video = cv2.VideoCapture(0)

while True:

    _flag, frame = video.read()

    # convert to rgb and resize
    im = Image.fromarray(frame, 'RGB')
    im = im.resize((128,128))
    img_array = np.array(im)

    # convert fom 128x128x3 to 1x128x128x3 because our model uses a 4D tensor
    # images x height x width x channel
    img_array = img_array.reshape(1, 128, 128, 3)

    prediction = int(model.predict(img_array)[0][0])

    if prediction == 0:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
