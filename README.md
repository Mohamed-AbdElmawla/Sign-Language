# Sign-Language

This is a computer vision model that can categorize sign language gestures into 6 different categories. The model is trained on a custom dataset and achieves high accuracy in categorizing sign language gestures.

## Features

* Accuracy: The model achieves 89.8% accuracy on the test data
* Easy to Use: This repo comes with real_time_detection.ipynb file which uses the camera and categorizes real-time video data

## Dataset

The dataset used to train the model consists of ~200 image all created manually via data_collect.ipynb and stored in data folder

# How to Use
## Installtion
To install the dependencies, run:
bash
pip install -r requirements.txt

## Usage
To use your camera to categorize realtime video data of sign language, run:<br>

python real_time_detection.py

This will open a window showing camera, make a gesture with your hand and it will put a box around your hand with the category on it
you have these classes {Help, Water, Game, Movie, me, what}
