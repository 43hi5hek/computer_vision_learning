import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# img = cv.imread('LR.png', 0)
# L = img[:, 1:300]
# R = img[:, 301:600]
# stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
# disparity = stereo.compute(L, R)
# disparity = cv.normalize(disparity, disparity, 0, 255, cv.NORM_MINMAX)
#
# plt.imshow(disparity,'gray')
# plt.show()