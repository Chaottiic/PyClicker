# System Packages
import time

# Pynput
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller

# Delay in Seconds
DELAY = 0.005
# You can find the keys here:
# - https://pynput.readthedocs.io/en/latest/_modules/pynput/keyboard/_base.html#Key # noqa: E501
TOGGLE_KEY = Key.shift_r
END_KEY = Key.end

# Supported Mouse Buttons:
# - right ; left
MOUSE_BUTTON = Button.right


STOP = TOGGLE = False


def on_press(key):
    global STOP, TOGGLE
    if key == TOGGLE_KEY:
        if TOGGLE:
            TOGGLE = False
            print("[PyClicker] Toggled PyClicker - OFF")
        else:
            TOGGLE = True
            print("[PyClicker] Toggled PyClicker - ON")
    elif key == END_KEY:
        STOP = True
        print("[PyClicker] Exiting")


if __name__ == "__main__":
    listener = Listener(on_press=on_press)
    listener.start()
    mouse = Controller()

    print(f"[PyClicker] - Press {TOGGLE_KEY} to toggle PyClicker on or off.")
    print(f"[PyClicker] - Press {END_KEY} to stop PyClicker.")
    while not STOP:
        if TOGGLE:
            mouse.press(MOUSE_BUTTON)
            mouse.release(MOUSE_BUTTON)
            time.sleep(DELAY)
    listener.stop()
