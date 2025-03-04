# Face-Detection-LED-Control

This project uses Google Teachable Machine and OpenCV to detect a user's face via a webcam and control an LED on an Arduino Mega 2560. When the trained model detects a face, the Python script sends a signal to the Arduino via serial communication, turning the LED ON. If no face is detected, the LED turns OFF.

Features
Face detection using Google Teachable Machine
Real-time processing with OpenCV
Serial communication between Python & Arduino
Automatic LED control based on detection

1. Requirements:
Hardware
Arduino Mega 2560
USB Cable (for Arduino)
LED (optional, can use built-in LED on pin 13)
Webcam
Software
Python 3.12.8
Arduino IDE
Visual Studio Code (recommended)
Google Teachable Machine (for training model)

2. Installation:
Step 1: Install Dependencies
Run the following command in your terminal to install the required Python libraries:
pip install opencv-python tensorflow numpy pyserial
Step 2: Train Your Model on Teachable Machine
Train an image classification model with two classes:
Class 0: Face Detected
Class 1: No Face
Export the model as TensorFlow Lite (Floating Point).
Download and extract the converted_tflite.zip.
Place model_unquant.tflite in the same folder as the Python script.
Step 3: Upload the Arduino Code
Open Arduino IDE.
Copy & paste the face_control.ino code.
Select the Arduino Mega 2560 board.
Upload the sketch to the board.

3. Running the Project:
Start the Python Script
Run the following command:
python face_detection.py
Look at the webcam—if your face is detected, the LED turns ON.
Move away or cover your face—the LED turns OFF.
Press q to stop the program.

6. Troubleshooting:
- LED not turning on?
Ensure the Arduino is connected via USB and the correct COM port is set in Python.
Try using a different USB cable or restarting the Arduino.
- Python script throws an error?
Check that model_unquant.tflite is in the correct folder.
Run pip install opencv-python tensorflow numpy pyserial to reinstall the dependencies.
- Face not detected properly?
Make sure there is good lighting and adjust the webcam angle.
Retrain the model with more images in Teachable Machine.
- Dependencies not found?
Make sure you're using the correct version of python as other versions face many issues.

