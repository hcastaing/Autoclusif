# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 21:28:32 2023

@author: hugoc
"""

import pyperclip
import keyboard
import time
import re
import pyautogui

# Function to check if the shortcut is activated
def check_shortcut():
    if keyboard.is_pressed('ctrl+shift+v'):
        # Get clipboard content 
        text = pyperclip.paste()
        # Make test inclusive
        text = inclusive_text(text)
        # Copy the inclusive text to the clipboard
        pyperclip.copy(text)
        # Remove existing text 
        pyautogui.press('backspace')
        # Simulate pressing Ctrl+V key
        pyautogui.hotkey('ctrl', 'v')
        
def inclusive_text(text):
    # Define regular expressions to match gendered words
    regex = r"\b(\w+)(e|s)?\b"

    # Replace gendered words with inclusive alternatives
    text = re.sub(regex, r"\1·\2", text)
    
    # Replace masculine words with inclusive words
    text = text.replace("il", "il·elle")
    text = text.replace("ils", "ils·elles")
    text = text.replace("son", "son·sa")
    text = text.replace("sa", "son·sa")
    text = text.replace("leur", "leur·leurs")
    text = text.replace("eux", "eux·elles")

    return text
    
# Continuously check for the shortcut activation
while True:
    check_shortcut()
    time.sleep(0.1)