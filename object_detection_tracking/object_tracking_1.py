import cv2 as cv
import numpy as np
import time
import imutils

# VIDEO CAPTURE OBJ -- DETECT -- BBOX --
# NEW VIDEO CAPTURE -- TRACKING ALGO

# tracker = cv.TrackerKCF_create()
#
# cap = cv.VideoCapture(0)
# _, frame = cap.read()
# # bbox = (0,0,320,240)
# bbox = cv.selectROI('roi', frame, fromCenter=False)
# ok = tracker.init(frame, bbox)
# while(cap.isOpened()):
#     _, frame = cap.read()
#     ok, bbox = tracker.update(frame)
#     p1 = (int(bbox[0]), int(bbox[1]))
#     p2 = (int(bbox[0]+bbox[2]), int(bbox[1]+bbox[3]))
#     cv.rectangle(frame, p1, p2, (255,0,0), 2)
#     cv.imshow("Tracking", frame)
#     if cv.waitKey(2) & 0xff == ord('q'): break
#
# cap.release()
# cv.destroyAllWindows()



