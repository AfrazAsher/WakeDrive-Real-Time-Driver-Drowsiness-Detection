import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
import random
from keras.models import load_model

img_size = 224
new_model = load_model('rtddd.h5')

path = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + path)
cap = cv2.VideoCapture(-1)
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

# while True:
#     ret, frame = cap.read()
#     print("Inside Loop")
#     eye_cascade = cv2.CascadeClassifier(
#         cv2.data.haarcascades + 'haarcascade_eye.xml')
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
#     for (x, y, w, h) in eyes:
#         rol_gray = gray[y:y+h, x:x+w]
#         rol_color = frame[y:y+h, x:x+w]
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#         eyess = eye_cascade.detectMultiScale(rol_gray)
#         if len(eyess) == 0:
#             print('no eyes are detected')
#         else:
#             for (ex, ey, ew, eh) in eyess:
#                 eyes_rol = rol_color[ey:ey+eh, ex:ex+ew]

#     final_image = cv2.resize(eyes_rol, (224, 224))
#     final_image = np.expand_dims(final_image, axis=0)
#     final_image = final_image/255.0
#     predictions = new_model.predict(final_image)
#     print(predictions)
#     if (predictions > 0.5):
#         status = 'close eyes'
#     else:
#         status = 'open eyes'

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     print(face_cascade.empty())
#     faces = face_cascade.detectMultiScale(gray, 1.1, 4)

#     # draw rectangle around the faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

#     font = cv2.FONT_HERSHEY_SIMPLEX

#     cv2.putText(frame, status, (50, 50), font, 3, (0, 0, 255), 2, cv2.LINE_4)
#     cv2.imshow('Drowsiness Detection', frame)

#     if cv2.waitKey(2) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
