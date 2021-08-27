import numpy as np
import cv2
import cv2_util, pyautogui_util

# Ensure file is jpg format and in images
jpg_file = "pikachu"

image = cv2.imread(f"./images/{jpg_file}.jpg")

image = cv2_util.crop_image(image)

# cv2.imshow('Input Image', image) 
# cv2.waitKey(0)

binary_image = cv2_util.convert_to_binary_image(image)
# cv2.imshow('Binary Image', binary_image) 
# cv2.waitKey(0)

pyautogui_util.draw_binary_image(binary_image)