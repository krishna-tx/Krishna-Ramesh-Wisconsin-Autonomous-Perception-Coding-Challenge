'''
Online Resources Used: 
    https://techvidvan.com/tutorials/detect-objects-of-similar-color-using-opencv-in-python/
    https://stackoverflow.com/
    https://www.geeksforgeeks.org/
    https://docs.opencv.org/
'''
# Importing useful libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt

# reading image and converting the color scale to RBG and HSV
img = cv2.imread("red.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# lower and upper thresholds for the red/orange color to filter out the cones
lower = np.array([115, 200, 150])
upper = np.array([180, 255, 255])

# creating the mask and removing any extra noise from the image
kernel = np.ones((8, 8))
mask = cv2.inRange(hsv, lower, upper)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# finding the contours from the mask (all the cones)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# modifying the array to have only two dimensions (each row is a contour and each contour has an x and y coordinate)
new_contours = []
for i in range(len(contours)):
    new_contours.append(contours[i].squeeze(axis=1))

# finding the average x and y coordinate values of each contour. This will give us the approximate mid point of the 4 cones
points = []
for i in range(4):
    contour = new_contours[i]
    x_mean = int(np.mean(contour, axis=0)[0])
    y_mean = int(np.mean(contour, axis=0)[1])
    points.append((x_mean, y_mean))

# using mid point of the 4 cones, we can use the slope formula to find the slope between the 2 cones on the right and left
slope1 = (points[2][1]-points[0][1])/(points[2][0]-points[0][0])
slope2 = (points[3][1]-points[1][1])/(points[3][0]-points[1][0])

# finding the y-intercept of the line that will go through the 2 cones on the right and the 2 cones on the left
y_int1 = points[0][1] - (points[0][0] * slope1)
y_int2 = points[1][1] - (points[1][0] * slope2)

# drawing the 2 lines on the image using the equation for the line and two points that lie on the line
answer = cv2.line(img, (0, int(0 * slope1 + y_int1)), (img.shape[0], int(img.shape[0] * slope1 + y_int1)), (255, 0, 0), 5)
answer = cv2.line(answer, (0, int(0 * slope2 + y_int2)), (img.shape[0], int(img.shape[0] * slope2 + y_int2)), (255, 0, 0), 5)

# converting the color scale back to BGR and writing the image as an output
answer = cv2.cvtColor(answer, cv2.COLOR_RGB2BGR)
cv2.imwrite("answer.png", answer)