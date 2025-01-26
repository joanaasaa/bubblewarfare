#!/bin/sh
pyinstaller --onefile --add-data "assets/:." --paths venv/lib/python3.13/site-packages/ game.py
