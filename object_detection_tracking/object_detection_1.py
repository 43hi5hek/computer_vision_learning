import cv2 as cv
import numpy as np
import imutils

# face and eye detection
# face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
# cap = cv.VideoCapture(0)
# while(cap.isOpened()):
#     _, frame = cap.read()
#     frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)
#     for (x,y,w,h) in faces:
#         cv.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
#         face_region_gray = frame_gray[y:y+h, x:x+w]
#         face_region_color = frame[y:y+h, x:x+w]
#         eyes = eye_cascade.detectMultiScale(face_region_gray)
#         for (ex, ey, ew, eh) in eyes:
#             cv.rectangle(face_region_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
#     cv.imshow('frame', frame)
#     if cv.waitKey(30) & 0xff == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()

# pedestrian detection
# hog = cv.HOGDescriptor()
# hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())
# img = cv.imread('image1.jpg')
# img = imutils.resize(img, width=min(400, img.shape[1]))
# (rects, weights) = hog.detectMultiScale(img, winStride=(4,4), padding=(8,8), scale=1.05)
# for (x, y, w, h) in rects:
#     cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
# cv.imshow('img', img)
# cv.waitKey(0)
# cv.destroyAllWindows()
