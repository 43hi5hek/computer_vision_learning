import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# meanshift, camshift
# cap = cv.VideoCapture('video1.mp4')
# ret, first_frame = cap.read()
# cv.imshow('first_frame', first_frame)
# code for thresholding the ROI, creating its mask,
# finding its center, and finding the bounding box dimensions
# while True:
#     backproject the ROI
#     meanshift/camshift
#     draw bounding box
# cv.waitKey(0)
# # cap.release()
# cv.destroyAllWindows()

# dense optic flow
# cap = cv.VideoCapture(0)
# ret, frame1 = cap.read()
# prvs = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
# hsv = np.zeros_like(frame1)
# hsv[..., 1] = 255
# while(cap.isOpened()):
#     ret, frame2 = cap.read()
#     next = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)
#     flow = cv.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
#     mag, ang = cv.cartToPolar(flow[...,0], flow[...,1])
#     hsv[...,0] = ang*180/np.pi/2
#     hsv[...,2] = cv.normalize(mag,None,0,255,cv.NORM_MINMAX)
#     rgb = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
#     cv.imshow('frame2', rgb)
#     if cv.waitKey(30) & 0xFF == ord('q'):
#         break
#     prvs = next
# cap.release()
# cv.destroyAllWindows()


# background subtraction
# cap = cv.VideoCapture(0)
# fgbg = cv.createBackgroundSubtractorMOG2(10, 10, 0)
# kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))
#
# while(cap.isOpened()):
#     _, frame = cap.read()
#     fg_mask = fgbg.apply(frame)
#     fg_mask = cv.morphologyEx(fg_mask, cv.MORPH_OPEN, kernel)
#     cv.imshow('fg_mask', fg_mask)
#     if cv.waitKey(30) & 0xFF == ord('q'): break
# cap.release()
# cv.destroyAllWindows()





