import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# harris
# img = cv.imread('image1.jpg')
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# gray = np.float32(gray)
# dst = cv.cornerHarris(gray, 5, 3, 0.04)
# img[dst > 0.01*dst.max()] = [0,0,255]
# cv.imshow('corners', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# shi tomasi corner
# img = cv.imread('image1.jpg')
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# corners = cv.goodFeaturesToTrack(gray, 36, 0.01, 10)
# corners = np.int0(corners)
# for i in corners:
#     x,y = i.ravel()
#     cv.circle(img,(x,y),3,255,-1)
# plt.imshow(img)
# plt.show()

# FAST, ORB (Process finished with exit code -1073741819)
# img = cv.imread('image1.jpg', 0)
# fast = cv.FastFeatureDetector()
# kp = fast.detect(img, None)
# img2 = cv.drawKeypoints(img, kp, color=(255,0,0))
# cv.imshow('keypoints', img2)
# cv.waitKeyEx(0)
# cv.destroyAllWindows()