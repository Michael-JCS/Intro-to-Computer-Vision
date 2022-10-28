import cv2


#we are using a hard cascade is a .xml that has
#been used on 1000 of faces to get the accuracy it has now
capture = cv2.VideoCapture('vid2.mp4')
#capture = cv2.VideoCapture(0) uses your webcam and it will detect your face :)

cv2.namedWindow('video', cv2.WINDOW_NORMAL)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(True):
    ret, frame = capture.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    faces = face_cascade.detectMultiScale(image=gray, minSize=(200, 200), flags=cv2.CASCADE_SCALE_IMAGE)
#bigger the value in min size the more accurate it is
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('video', frame)

    cv2.waitKey(10)



