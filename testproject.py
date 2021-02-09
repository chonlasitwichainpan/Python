'''import face_recognition
import cv2

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()'''

'''import os
import cv2
import time

# init camera
execution_path = os.getcwd()
camera = cv2.VideoCapture(0)

while True:
    # Init and FPS process
    start_time = time.time()

    # Grab a single frame of video
    ret, frame = camera.read()

    # calculate FPS >> FPS = 1 / time to process loop
    fpsInfo = "FPS: " + str(1.0 / (time.time() - start_time)) 
    print(fpsInfo)

    cv2.putText(frame, fpsInfo, (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
camera.release()
cv2.destroyAllWindows()'''

import face_recognition
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]

    face_landmarks_list = face_recognition.face_landmarks(rgb_frame)
    for face_landmarks in face_landmarks_list:

        for facial_feature in face_landmarks.keys():
            pts = np.array([face_landmarks[facial_feature]], np.int32) 
            pts = pts.reshape((-1,1,2))
            cv2.polylines(frame, [pts], False, (0,255,0))

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()