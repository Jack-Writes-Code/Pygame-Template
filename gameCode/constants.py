"""
UNCHANGING GAME VARIABLES
"""
import os
import json
import sys


def resource_path(relative_path):
    """
    GET ABSOLUTE PATH TO RESOURCE, WORKS FOR DEV AND FOR PYINSTALLER
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


with open(resource_path(os.path.join("gameCode/configs", "settings.json")), 'r') as settings_file:
    settings = json.load(settings_file)


FPS = settings["FPS"]
SCREENWIDTH = settings["SCREENWIDTH"]
SCREENHEIGHT = settings["SCREENHEIGHT"]
