import numpy as np
import cv2
import cv2_util, pyautogui_util

# Ensure file is in \images folder. Include format
jpg_file = "pikachu.jpg"
image = cv2.imread(f"./images/{jpg_file}")

cv2.imshow("Input Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

crop = input("Crop image? [y/N]: ")
if(crop == 'y' or crop == 'Y'):
    image = cv2_util.crop_image(image)

binary_image = cv2_util.convert_to_binary_image(image, preview=True)

# pyautogui_util.draw_binary_image(binary_image, verbose=False, fast_mode=True)

pyautogui_util.draw2(binary_image)