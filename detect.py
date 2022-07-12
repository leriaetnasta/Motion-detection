import cv2
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2) #absolute difference between first frame and second frame
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY) #convert into a gray scale mode cause its easier to find the contours in grayscale than in rgb
    blur = cv2.GaussianBlur(gray, (5, 5), 0)#apply gaussiean blurr
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)#we need the second variable
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1,"Status:{}".format('Movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('My Cam', frame1)

cv2.destroyAllWindows()
