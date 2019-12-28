import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# hsv thresholding red
# lower = np.array([160, 100, 100])
# upper = np.array([179, 255, 255])
# cap = cv.VideoCapture(0)
# while(cap.isOpened()):
#     _, frame = cap.read()
#     hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
#     mask_blue = cv.inRange(hsv, lower, upper)
#     cv.imshow('mask_blue', mask_blue)
#     cv.imshow('frame', frame)
#     flag = cv.waitKey(5) & 0xFF
#     if flag == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()

# adaptive thresholding (mean done, gaussian done, otsu not done)
# cap = cv.VideoCapture(0)
# while(cap.isOpened()):
#     _, original = cap.read()
#     gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
#     gray_meanthresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
#     gray_gaussthresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
#     cv.imshow('gray', gray)
#     cv.imshow('gray_meanthresh', gray_meanthresh)
#     cv.imshow('gray_guassthresh', gray_gaussthresh)
#     flag = cv.waitKey(5) & 0xFF
#     if flag == ord('q'):
#         break
# cv.destroyAllWindows()

# geometric transforms (affine done, perspective not done)
# img = cv.imread('image1.jpg', 0)
# rows,cols = img.shape
# pts1 = np.float32([[100, 50], [100, 100], [50, 100]])
# pts2 = np.float32([[100, 50], [100, 100], [150, 100]])
# M = cv.getAffineTransform(pts1,pts2)
# dst = cv.warpAffine(img,M,(cols,rows))
# cv.imshow('img', img)
# cv.imshow('dst', dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

# blurring (gaussian, median, bilateral)

# morphological transforms (erosion, dilation)
# cap = cv.VideoCapture(0)
# kernel = np.ones((3,3), np.uint8)
# while(cap.isOpened()):
#     _, original = cap.read()
#     gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
#     gray_meanthresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7, 4)
#     gray_meanthresh_clos = cv.morphologyEx(gray_meanthresh, cv.MORPH_CLOSE, kernel)
#     gray_gaussthresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 7, 4)
#     gray_gaussthresh_clos = cv.morphologyEx(gray_gaussthresh, cv.MORPH_CLOSE, kernel)
#     cv.imshow('gray', gray)
#     cv.imshow('gray_meanthresh_clos', gray_meanthresh_clos)
#     cv.imshow('gray_guassthresh_clos', gray_gaussthresh_clos)
#     flag = cv.waitKey(5) & 0xFF
#     if flag == ord('q'):
#         break
# cv.destroyAllWindows()

# gradients, sobel, laplacian

# image pyramids











