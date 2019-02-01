# Keras project to find me using my webcam

## Dependencies
- pyenv `brew install pyenv`
- python 3.7.2 (`pyenv install 3.7.2`) - may need to cure zlib warnings

## Setup
- from within the project dir
- install packages `pipenv install`
- setup env `pipenv shell`

## Training
- with camera pointed away from subject
  * `python capture_images.py data/valid/0 200`
  * `python capture_images.py data/train/0 2000`
- with camera pointed at subject
  * `python capture_images.py data/valid/1 200`
  * `python capture_images.py data/train/1 2000`

- run `python train.py`

## Predictions

- run `python predict.py`

## Caveats
- this is not an object detection network, therefore it will take the whole image from the webcam into account, not just your face.  A more advanced form of neural network will detect you within the picture, so it would not matter what your surroundings are, but we're starting basic first.

* tutorial: https://medium.com/@jinilcs/a-simple-keras-model-on-my-laptop-webcam-dda77521e6a0
