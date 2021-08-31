import cv2
import pyautogui
import time
import keyboard
pyautogui.PAUSE = 0.001

def read_image():
    image = None
    while True:
        image_name = input("Input image name : ")
        image = cv2.imread(f"./images/{image_name}")
        if image is not None:
            print(f"\n Loaded: '{image_name}'\n")
            return image
        else:
            print(f"\n  Unable to find '{image_name}' \n  Try again\n")


def process_binary(image, treshold):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image_binary = cv2.threshold(image_gray, treshold, 255, cv2.THRESH_BINARY)
    return image_binary

def countdown(message, seconds):
    while seconds > 0:
        print(message.format(s=seconds))
        seconds = seconds - 1
        time.sleep(1) 

def get_screen_offset():
    input("Press Enter to capture offset > ")
    countdown("Capturing offset in {s} seconds...", 3)
    x, y = pyautogui.position()
    print(f"\n offset x: {x} y: {y}\n")
    return x, y

def basic_draw():
    
    image = read_image()
    image = process_binary(image, 150)
    offset_x, offset_y = get_screen_offset();
    print("Preview image")
    cv2.imshow("Preview", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    while True:
        command = input("(D)raw or (E)xit : ")
        if(command == 'd' or command == 'D'):

            input("Press Enter to start countdown > ")
            countdown("Starting in {s} seconds...", 5)
            for y in range(0,len(image)):
                for x in range(0,len(image[y])):
                    if(image[y][x] == 0):
                        queue = []
                        queue.append((x,y))
                        while queue:
                            s = queue.pop()
                            x = s[0]
                            y = s[1]
                            pyautogui.click(x=x+offset_x, y=y+offset_y)
                            if(x != 0 and image[y-1][x] == 0):
                                queue.append((x,y-1))
                                image[y-1][x] = 1
                            if(y != 0 and image[y][x-1] == 0):
                                queue.append((x-1,y))
                                image[y][x-1] = 1
                            if(x != len(image)-1 and image[y+1][x] == 0):
                                queue.append((x,y+1))
                                image[y+1][x] = 1
                            if(y != len(image[y])-1 and image[y][x+1] == 0):
                                queue.append((x+1,y))
                                image[y][x+1] = 1

                            if keyboard.is_pressed("p"):
                                print("Paused. Press 'r' to continue")
                                keyboard.wait("r")
            print("Done")

            return
        elif(command == 'e' or command == 'E'):
            return

