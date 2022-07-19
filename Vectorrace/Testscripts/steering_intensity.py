import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# facetracking
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def translate(value, width, offset_line_from_center):
    right_line = int(width/2) + offset_line_from_center
    left_line = int(width/2) - offset_line_from_center
    if value > right_line:
        valueScaled = (value - right_line)/(width-right_line) # convert to range 0-1
        return int(valueScaled * 100) # convert to range 0-100
    if value < left_line:
        valueScaled = (left_line - value)/left_line # convert to range 0-1
        return int(-valueScaled * 100) # convert to range -100-0
    else:
        return 0

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    offset_line_from_center = 40
    left_line_coordinates = int(width/2) - offset_line_from_center
    right_line_coordinates = int(width/2) + offset_line_from_center

    # drawing center lines on canvas
    img = cv2.line(frame, (left_line_coordinates, 0), (left_line_coordinates, height), (0, 255, 0), 2)
    img = cv2.line(frame, (right_line_coordinates, 0), (right_line_coordinates, height), (0, 255, 0), 2)
    
    # facetracking - (x, y) are the top left coordinates of the face frame
    faces = face_cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 1.3, 5)
    #faces = face_cascade.detectMultiScale(cv2.COLOR_BGR2GRAY, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)

        output = translate(x + w/2, width, offset_line_from_center)
        font = cv2.FONT_HERSHEY_SIMPLEX
        img = cv2.putText(img, str(output), (10, height - 10), font, 2, (255, 255, 255), 5, cv2.LINE_AA)

    cv2.imshow('Fenster', img)


    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()