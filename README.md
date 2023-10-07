# Gesture-Drawing
Overview
Gesture Drawing Argumented Reality(AR) platform  With the help of hand gestures you can draw anything and explore your Creativity.

This project is about using openCV and media pipe libraries to utilize the web camera for drawing in real-time.
The main idea is:

-detect hands using mediapipe


-using hand-gesture to draw 


-use NumPy for data storage of hand coordinates 


-use cV2 to capture live video from the camera


MediaPipe

MediaPipe Hands is a high-fidelity hand and finger tracking solution. It employs machine learning (ML) to infer 21 3D landmarks of a hand from just a single frame. Whereas current state-of-the-art approaches rely primarily on powerful desktop environments for inference, our method achieves real-time performance on a mobile phone and even scales to multiple hands. We hope that providing this hand perception functionality to the wider research and development community will result in an emergence of creative use cases, stimulating new applications and new research avenues.


![68747470733a2f2f6d65646961706970652e6465762f696d616765732f6d6f62696c652f68616e645f747261636b696e675f33645f616e64726f69645f6770752e676966](https://github.com/SAM389/Gesture-Drawing/assets/58984497/83d7e8a8-73d2-4f90-826b-03727f6e7e0b)


Hand Landmark Model
After the palm detection over the whole image our subsequent hand landmark model performs precise keypoint localization of 21 3D hand-knuckle coordinates inside the detected hand regions via regression, that is direct coordinate prediction. The model learns a consistent internal hand pose representation and is robust even to partially visible hands and self-occlusions.


To obtain ground truth data, we have manually annotated ~30K real-world images with 21 3D coordinates, as shown below (we take the Z-value from the image depth map if it exists per the corresponding coordinate). To better cover the possible hand poses and provide additional supervision on the nature of hand geometry, we also render a high-quality synthetic hand model over various backgrounds and map it to the corresponding 3D coordinates.


![68747470733a2f2f6d65646961706970652e6465762f696d616765732f6d6f62696c652f68616e645f6c616e646d61726b732e706e67](https://github.com/SAM389/Gesture-Drawing/assets/58984497/e9b1384f-5f0b-4de8-a005-4521eb467645)





