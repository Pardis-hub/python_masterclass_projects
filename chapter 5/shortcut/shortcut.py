from pynput import keyboard
from pynput.keyboard import Key, KeyCode

pressed_keys = set()
triggered = False

def on_press(key):
    global triggered
    pressed_keys.add(key)

    shift_pressed = (
        Key.shift in pressed_keys or
        Key.shift_l in pressed_keys or
        Key.shift_r in pressed_keys
    )

    alt_pressed = (
        Key.alt in pressed_keys or
        Key.alt_l in pressed_keys or
        Key.alt_r in pressed_keys
    )

    d_pressed = any(
        isinstance(k, KeyCode) and k.char and k.char.lower() == 'd'
        for k in pressed_keys
    )

    if shift_pressed and alt_pressed and d_pressed and not triggered:
        triggered = True
        print("Shift + Alt + D pressed!")

def on_release(key):
    global triggered
    pressed_keys.discard(key)

    if key in (Key.shift, Key.shift_l, Key.shift_r,
               Key.alt, Key.alt_l, Key.alt_r) \
       or (isinstance(key, KeyCode) and key.char and key.char.lower() == 'd'):
        triggered = False

    if key == Key.esc:
        return False

with keyboard.Listener(
    on_press=on_press, on_release=on_release) as listener:
    listener.join()