import pyautogui
import random
import time
import subprocess

from pywin.scintilla.formatter import operators
from pywinauto import Application
import pygetwindow as gw


def open_valorant():
    valorant_window = gw.getWindowsWithTitle('VALORANT')[0]  # Título da janela padrão

    # Restaurar a janela se estiver minimizada
    if valorant_window.isMinimized:
        valorant_window.restore()  # Restaura a janela


def random_operator_position(role):
    if role == 'iniciador':
        pyautogui.moveTo((150, 250), duration=0.5)
        pyautogui.click()
        operators = [(100, 350), (200, 350), (300, 350), (400, 350), (100, 450), (200, 450)]
        return random.choice(operators)
    elif role == 'duelista':
        pyautogui.moveTo((225, 250), duration=0.5)
        pyautogui.click()
        operators = [(100, 350), (200, 350), (300, 350), (400, 350), (100, 450), (200, 450), (300, 450)]
        return random.choice(operators)
    elif role == 'controlador':
        pyautogui.moveTo((400, 250), duration=0.5)
        pyautogui.click()
        operators = [(100, 350), (200, 350), (300, 350), (400, 350), (100, 450), (200, 450)]
        return random.choice(operators)
    elif role == 'sentinela':
        pyautogui.moveTo((300, 250), duration=0.5)
        pyautogui.click()
        operators = [(100, 350), (200, 350), (300, 350), (400, 350), (100, 450), (200, 450)]
        return random.choice(operators)

def move_and_click(role):
    cordinate = random_operator_position(role)
    pyautogui.moveTo(cordinate, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo((950, 750), duration=0.5)
    pyautogui.click()

role = ["iniciador", "duelista", "controlador", "sentinela"]

open_valorant()
time.sleep(1.5)
move_and_click(random.choice(role))
pyautogui.click()
