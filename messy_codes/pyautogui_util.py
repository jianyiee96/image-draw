import pyautogui, time
import numpy as np 
import keyboard

pyautogui.PAUSE = 0.001

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

def draw_binary_image(image, verbose=False, fast_mode=False):
    offset_x, offset_y = get_mouse_pos()

    print(image.shape)
    print("Position x: ", offset_x)
    print("Position y: ", offset_y)

    start = input("Start drawing? [Y/n]: ")
    if(start == 'n' or start == 'N'):
        print("Exiting")
        return

    print("Starting in 5 seconds...")
    time.sleep(1) 
    print("Starting in 4 seconds...")
    time.sleep(1) 
    print("Starting in 3 seconds...")
    time.sleep(1) 
    print("Starting in 2 seconds...")
    time.sleep(1) 
    print("Starting in 1 seconds...")
    time.sleep(1) 
    
    line_state = False
    start = 0
    end = 0
    if (fast_mode):
        for idx, value in np.ndenumerate(image):
            
            if(verbose):
                print(idx[0], idx[1], "---", value)

            if(not line_state and value == 0):
                line_state = True
                start = (idx[1]+offset_x, idx[0]+offset_y)
            
            elif(line_state and value == 0):
                end = (idx[1]+offset_x, idx[0]+offset_y)

            elif(line_state and value == 255):
                line_state = False
                pyautogui.moveTo(start[0], start[1])
                pyautogui.dragTo(end[0], end[1], button='left') 
    else:
    
        for idx, value in np.ndenumerate(image):
            if(verbose):
                print(idx[0], idx[1], "---", value)
            if value == 0:
                pyautogui.click(x=idx[1]+offset_x, y=idx[0]+offset_y)

    print("Done!")


def draw2(image):
    offset_x, offset_y = get_mouse_pos()

    print(image.shape)
    print("Position x: ", offset_x)
    print("Position y: ", offset_y)

    start = input("Start drawing? [Y/n]: ")
    if(start == 'n' or start == 'N'):
        print("Exiting")
        return

    print("Starting in 5 seconds...")
    time.sleep(1) 
    print("Starting in 4 seconds...")
    time.sleep(1) 
    print("Starting in 3 seconds...")
    time.sleep(1) 
    print("Starting in 2 seconds...")
    time.sleep(1) 
    print("Starting in 1 seconds...")
    time.sleep(1) 
    
    curr_idx = 1
    counter = 0

    for x in range(0,len(image)):
        for y in range(0,len(image[x])):
            if(image[x][y] == 0):
                queue = []
                queue.append((x,y))
                while queue:

                    s = queue.pop()
                    x = s[0]
                    y = s[1]
                    pyautogui.click(x=y+offset_x, y=x+offset_y)

                    if(x != 0 and image[x-1][y] == 0):
                        queue.append((x-1,y))
                        image[x-1][y] = curr_idx

                    if(y != 0 and image[x][y-1] == 0):
                        queue.append((x,y-1))
                        image[x][y-1] = curr_idx

                    if(x != len(image)-1 and image[x+1][y] == 0):
                        queue.append((x+1,y))
                        image[x+1][y] = curr_idx

                    if(y != len(image[x])-1 and image[x][y+1] == 0):
                        queue.append((x,y+1))
                        image[x][y+1] = curr_idx

                    if keyboard.is_pressed("p"):
                        print("Paused. Press r to continue")
                        keyboard.wait("r")
