from pynput.keyboard import Key, Listener, KeyCode

MY_HOT_KEYS = [
    {"function1": {Key.ctrl, Key.alt, KeyCode(char="n")}}
]

current_keys = set()


def key_pressed(key):
    print("Pressed {}".format(key))
    for data in MY_HOT_KEYS:
        FUNCTION = list(data.keys())[0]
        KEYS = list(data.values())[0]

        if key in KEYS:
            current_keys.add(key)

            # checker = True
            # for k in KEYS:
            #     if k not in current_keys:
            #         checker = False
            #         break
            # if checker:
            #     function = eval(FUNCTION)
            #     function()
            if all(k in current_keys for k in KEYS):
                function = eval(FUNCTION)
                function()


def function1():
    print("function1")


def key_released(key):
    print("Released {}".format(key))

    if key in current_keys:
        current_keys.remove(key)
    if key == Key.esc:
        return False


with Listener(on_press=key_pressed, on_release=key_released) as listener:
    listener.join()