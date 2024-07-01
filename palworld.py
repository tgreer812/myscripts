import keyboard
import time

DELAY = 2

def hold_key():
    print("Starting 3-second countdown...")
    time.sleep(DELAY)  # 3-second delay
    print("Holding down 'f' key...")
    keyboard.press('f')  # Presses and holds down the 'f' key

def release_key():
    print("Releasing 'f' key...")
    keyboard.release('f')  # Releases the 'f' key

# This variable keeps track of whether the 'f' key is currently being held down
is_holding_key = False

while True:
    if keyboard.is_pressed('['):
        if is_holding_key:
            release_key()
            is_holding_key = False
            time.sleep(0.5)  # Small delay to prevent immediate re-triggering
        else:
            hold_key()
            is_holding_key = True
            time.sleep(0.5)  # Small delay to prevent immediate re-triggering
