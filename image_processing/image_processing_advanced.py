import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# canny
# cap = cv.VideoCapture(0)
# low = 130
# high = 230
# while(cap.isOpened()):
#     _, img = cap.read()
#     img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     img_edge = cv.Canny(img, low, high)
#     cv.imshow('img', img)
#     cv.imshow('img_edge', img_edge)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
# cv.destroyAllWindows()

# contours
# img = cv.imread('image2.jpg')
# boundary = 100
# img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# _, mask = cv.threshold(img_gray, boundary, 255, 0)
# cv.imshow('mask', mask)
# cv.waitKey(0)
# contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# img_cont = cv.drawContours(img, contours, -1, (0,0,255), 1)
# cv.imshow('img_cont', img_cont)
# print(len(contours))
# cv.waitKey(0)
# cv.destroyAllWindows()

# histogram equalize, CLAHE
# img = cv.imread('image5.jpg', 0)
# equ = cv.equalizeHist(img)
# cv.imshow('equ', equ)
# cv.imshow('img', img)
# cv.imwrite('image7.jpg', equ)
# cv.waitKey(0)
# cv.destroyAllWindows()

# calchistogram
# img = cv.imread('image3.jpg')
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
# plt.imshow(hist,interpolation = 'nearest')
# plt.show()
# cv.waitKey(0)
# cv.destroyAllWindows()

# hough line p
# img = cv.imread('image2.jpg')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# edges = cv.Canny(gray, 50, 150)
# cv.imshow('edges', edges)
#
# minLineLength = 5
# maxLineGap = 5
#
# lines = cv.HoughLinesP(edges, 1, np.pi/180, 10, minLineLength, maxLineGap)
#
# for i in range(len(lines)):
#     x1 = lines[i][0][0]
#     y1 = lines[i][0][1]
#     x2 = lines[i][0][2]
#     y2 = lines[i][0][3]
#     cv.line(img,(x1,y1),(x2,y2),(255,255,255),5)
# cv.imshow('lines drawn', img)
# cv.waitKey(0)
# cv.destroyAllWindows()


# hough line
# img = cv.imread('image2.jpg')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# edges = cv.Canny(gray, 50, 150)
#
# lines = cv.HoughLines(edges,1,np.pi/180,200)
# for i in range(len(lines)):
#     rho = lines[i][0][0]
#     theta = lines[i][0][1]
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000*(a))
#     x2 = int(x0 - 1000*(-b))
#     y2 = int(y0 - 1000*(a))
#     cv.line(img, (x1, y1), (x2, y2), (255, 255, 255), 5)
#
# cv.imshow('lines drawn', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# # histogram backproject
# img5 = cv.imread('image6.jpg')
# img5 = cv.pyrDown(cv.pyrDown(img5))
# img5_hsv = cv.cvtColor(img5, cv.COLOR_BGR2HSV)
# img51 = img5[:200, :200]
# img51_hsv = cv.cvtColor(img51, cv.COLOR_BGR2HSV)
# img51_hsv_hist = cv.calcHist([img51_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
# cv.normalize(img51_hsv_hist, img51_hsv_hist, 0, 255, cv.NORM_MINMAX)
# dst = cv.calcBackProject([img5_hsv], [0,1], img51_hsv_hist, [0,180,0,256], 1)
# kernel = np.ones((5,5),np.uint8)
# cv.filter2D(dst,-1, kernel, dst)
# cv.imshow('backprojected', dst)
# cv.waitKey(0)
# cv.destroyAllWindows()


