'''
This program simulates the pressing of the 'L' key on a keyboard using the pynput library.
'''
#? Use the following command to install the required libraries:
#! pip install pyautogui
#! pip install pynput

from pynput.keyboard import Controller
import time

# Crear un controlador de teclado
keyboard = Controller()

# Esperar un momento antes de presionar la tecla
time.sleep(2)

# Presionar y soltar la tecla 'L' 100 veces
for _ in range(4000):
    keyboard.press('l')
    keyboard.release('l')
    time.sleep(0.05)  # Pequeña pausa entre cada pulsación

print("Se presionó la tecla 'L' 100 veces")
