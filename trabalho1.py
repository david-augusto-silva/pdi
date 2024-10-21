import cv2
import numpy as np
import time

# Leitura da imagem da câmera
video = cv2.VideoCapture(0)

# Armazenamento de um quadro antes do início do loop
_, background = video.read()
time.sleep(2)
_, background = video.read()

# Janela de controle de cores hsv
def mouse(pos):
    pass

janela = "Controle de cores HSV"
cv2.namedWindow(janela)
labels = {"H":["H_min", "H_max"],
          "S":["S_min", "S_max"],
          "V":["V_min", "V_max"]}
cv2.createTrackbar(labels["H"][0], janela, 0, 180, mouse)
cv2.createTrackbar(labels["S"][0], janela, 0, 255, mouse)
cv2.createTrackbar(labels["V"][0], janela, 0, 255, mouse)
cv2.createTrackbar(labels["H"][1], janela, 0, 180, mouse)
cv2.createTrackbar(labels["S"][1], janela, 0, 255, mouse)
cv2.createTrackbar(labels["V"][1], janela, 0, 255, mouse)


# Utilizando detecção de cores
while True:
    ret, frame = video.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos(labels["H"][0], janela)
    s_min = cv2.getTrackbarPos(labels["S"][0], janela)
    v_min = cv2.getTrackbarPos(labels["V"][0], janela)
    h_max = cv2.getTrackbarPos(labels["H"][1], janela)
    s_max = cv2.getTrackbarPos(labels["S"][1], janela)
    v_max = cv2.getTrackbarPos(labels["V"][1], janela)
    mask = cv2.inRange(hsv, np.array([h_min, s_min, v_min]), np.array([h_max, s_max, v_max]))
    
    cv2.imshow("Video", mask)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

video.release()
cv2.destroyAllWindows()
