import cv2

def crop_image(image):

    ref = []
    def callback(event, x, y, flags, param):
        nonlocal ref
        if event == cv2.EVENT_LBUTTONDOWN:
            ref = [(x, y)]
        elif event == cv2.EVENT_LBUTTONUP:
            ref.append((x, y))
            cv2.rectangle(image, ref[0], ref[1], (0, 255, 0), 2)

    image_copy = image.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", callback)

    while True:
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("r"):
            image = image_copy.copy()
        elif key == ord("c"):
            break

    cv2.destroyAllWindows()

    if len(ref) == 2:
        roi = image_copy[min(ref[0][1],ref[1][1]):max(ref[0][1],ref[1][1]),
                            min(ref[0][0],ref[1][0]):max(ref[0][0],ref[1][0])]
    else:
        roi = image_copy

    cv2.imshow("Final", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return roi

def convert_to_binary_image(image, treshold=150, preview=False):
    if preview:
        cv2.imshow('Input Image', image)
        cv2.waitKey(0)

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #change to grayscale
    ret, image_binary = cv2.threshold(image_gray, treshold, 255, cv2.THRESH_BINARY)
    if preview:    
        cv2.imshow('Binary Image', image_binary)
        cv2.waitKey(0)
    cv2.destroyAllWindows()
    return image_binary

def apply_contours(image, treshold=150, preview=False):
    image_binary = convert_to_binary_image(image, treshold, preview)
    contours, hierarchy = cv2.findContours(image=image_binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    image_copy = image.copy()
    cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    if preview:
        cv2.imshow('Applied Contour', image_copy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return image_copy
