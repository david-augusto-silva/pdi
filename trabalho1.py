import cv2
import numpy as np
import time

"""
    PDI - Trabalho 1 - Capa de Invisibilidade
    Alunos: David Augusto e Sabrina Milane
"""

cap = cv2.VideoCapture(0)
time.sleep(3)  

# fundo para o primeiro frame
ret, fundo = cap.read()
fundo = np.flip(fundo, axis=1) 

# Intervalo do padrão HSV (cor azul)
lower_hsv = np.array([100, 150, 0]) 
upper_hsv = np.array([130, 255, 255]) 

while cap.isOpened():
    ret, frame = cap.read() 
    if not ret:
        break
    frame = np.flip(frame, axis=1) 

    #detecção da cor
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)


    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, iterations=1)

    #aplicação da máscara
    mask_inv = cv2.bitwise_not(mask)
    fundo_mascarado = cv2.bitwise_and(fundo, fundo, mask=mask)
    objeto_visivel = cv2.bitwise_and(frame, frame, mask=mask_inv)
    resultado = cv2.addWeighted(fundo_mascarado, 1, objeto_visivel, 1, 0)

    cv2.imshow("Capa de Invisibilidade: David e Sabrina", resultado)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
