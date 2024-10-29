import cv2

face_detector = cv2.CascadeClassifier('') #haarcascade_frontalface, harr_cascade_eye

cap = cv2.VideoCapture(0)

while True:
    _, image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face = face_detector.detectMultiScale(gray, 1.1, 4)
    
    for(x, y, w, h) in face:
        cv2.rectangle(image, pt1=(x, y), pt2=(x+w, y+h), color=(255, 0, 0), thickness=3, )


    #mostrar a imagem cinza
    cv2.imshow("Cinza", gray)
    cv2.imshow("Color", image)

    #parar o programa
    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
cv2.release()
