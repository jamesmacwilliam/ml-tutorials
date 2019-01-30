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

* tutorial: https://medium.com/@jinilcs/a-simple-keras-model-on-my-laptop-webcam-dda77521e6a0
