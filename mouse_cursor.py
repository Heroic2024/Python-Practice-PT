import pyautogui
import time
import os
import random

# Get screen size to define boundaries for random movement
screen_width, screen_height = pyautogui.size()

print("Mouse mover script started. Press Ctrl+C to stop.")

try:
    while True:
        # Generate random coordinates within screen dimensions
        x = random.randrange(0, screen_width)
        y = random.randrange(0, screen_height)
        
        # Move the mouse to the new location instantly (duration=0 for no visible movement)
        pyautogui.moveTo(x, y, duration=0)
        
        # Wait for 60 seconds before the next move
        time.sleep(60)

except KeyboardInterrupt:
    print("\nMouse mover script stopped by user.")
except Exception as e:
    print(f"An error occurred: {e}")