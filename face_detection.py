import cv2
import serial
import time
import numpy as np
import tensorflow.lite as tflite

# Set up serial communication with Arduino
arduino = serial.Serial('COM3', 9600)  # Change 'COM3' to your Arduino's port

# Load the Teachable Machine model
interpreter = tflite.Interpreter(model_path="model_unquant.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Start video capture
cap = cv2.VideoCapture(0)

def classify_frame(frame):
    # Resize and normalize frame
    frame_resized = cv2.resize(frame, (224, 224))
    frame_resized = np.expand_dims(frame_resized, axis=0).astype(np.float32) / 255.0
    
    interpreter.set_tensor(input_details[0]['index'], frame_resized)
    interpreter.invoke()
    
    output = interpreter.get_tensor(output_details[0]['index'])
    return np.argmax(output)  # Returns class index

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        class_id = classify_frame(frame)

        if class_id == 0:  # If "Face Detected" class
            arduino.write(b"ON\n")
            print("Face detected, LED ON")
        else:
            arduino.write(b"OFF\n")
            print("No face, LED OFF")

        cv2.imshow("Webcam", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Stopped")
finally:
    cap.release()
    cv2.destroyAllWindows()
    arduino.close()
