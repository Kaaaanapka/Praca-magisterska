import cv2
import numpy as np

# Wczytaj obraz
image = cv2.imread('chonky_boi.png')

# Sprawdzenie wymiarów obrazu
height, width, _ = image.shape

# Definicja pierwszego ROI (np. górna lewa część obrazu)
x1, y1, w1, h1 = 350, 250, 25, 25  # (x, y, szerokość, wysokość)
cv2.rectangle(image, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)  # Zielony kwadrat

# Definicja drugiego ROI (np. dolna prawa część obrazu)
x2, y2, w2, h2 = 300, 400, 25, 25
cv2.rectangle(image, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 0), 2)  # Niebieski kwadrat

# Pokazanie wyciętych fragmentów

cv2.imshow('Obrazek', image)

# Oczekiwanie na zamknięcie okien
cv2.waitKey(0)
cv2.destroyAllWindows()
