import numpy as np
import cv2
import cv2_util, pyautogui_util

# Ensure file is jpg format and in images
jpg_file = "gudetama-mini"
image = cv2.imread(f"./images/{jpg_file}.jpg")

cv2.imshow("Input Image", image)
cv2.waitKey(0)

crop = input("Crop image? [y/N]: ")
if(crop == 'y' or crop == 'Y'):
    image = cv2_util.crop_image(image)

binary_image = cv2_util.convert_to_binary_image(image, preview=True)

pyautogui_util.draw_binary_image(binary_image)