import pyautogui, time
import numpy as np 


def get_mouse_pos():
    print("Capturing position in 5 seconds...")
    time.sleep(1) 
    print("Capturing position in 4 seconds...")
    time.sleep(1) 
    print("Capturing position in 3 seconds...")
    time.sleep(1) 
    print("Capturing position in 2 seconds...")
    time.sleep(1) 
    print("Capturing position in 1 seconds...")
    time.sleep(1) 
    x, y = pyautogui.position()
    return x, y

def draw_binary_image(image):
    offset_x, offset_y = get_mouse_pos()
    print(image.shape)
    print("Position x: ", offset_x)
    print("Position y: ", offset_y)

    start = input("Start drawing? [Y/n]: ")
    if(start == 'n' or start == 'N'):
        print("Exiting")
        return

    for idx, value in np.ndenumerate(image):
        print(idx[0], idx[1], "---", value)
        if value == 0:
            pyautogui.click(x=idx[1]+offset_x, y=idx[0]+offset_y)
