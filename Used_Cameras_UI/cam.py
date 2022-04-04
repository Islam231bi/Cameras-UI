import cv2
import sys

# Open the device at the ID 0

cap = cv2.VideoCapture(sys.argv[1])

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)#
# Check whether user selected camera is opened successfully.

if not (cap.isOpened()):
    print("couldn't open")

cv2.namedWindow(sys.argv[1], cv2.WINDOW_FREERATIO)

while (True):

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame

    cv2.imshow(sys.argv[1], frame)
    cv2.moveWindow(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    cv2.setWindowProperty(sys.argv[1], cv2.WND_PROP_TOPMOST, 1)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    fps = cap.get(cv2.CAP_PROP_FPS)

    print(width, height, fps)
    # Waits for a user input to quit the application

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture

cap.release()

cv2.destroyAllWindows()
