'''
This program simulates the pressing of the 'L' key on a keyboard using the pynput library.
'''
#? Use the following command to install the required libraries:
#! pip install pyautogui
#! pip install pynput

from pynput.keyboard import Controller
import time

# Crear un controlador de teclado
# Make a keyboard controller
keyboard = Controller()

# Esperar un momento antes de presionar la tecla
# Wait a moment before pressing the key
time.sleep(2)

# Presionar y soltar la tecla 'L' 100 veces
# Press and release the 'L' key 100 times
for _ in range(10000):
    keyboard.press('l')
    keyboard.release('l')
    time.sleep(0.03)  # Pequeña pausa entre cada pulsación
                        # Small pause between each press

print("Se presionó la tecla 'L' 100 veces")
