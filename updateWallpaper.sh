#!/bin/bash

echo "Creating wallpaper..."

source ./venv/bin/activate
nice python3 generateWallpaper.py
nice python3 addClock.py
nice python3 addStats.py
deactivate
echo ""