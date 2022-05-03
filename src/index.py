from tkinter import Tk
from ui.ui import UI


def main():
    """Function that launches user interface using ui.py

    """
    window = Tk()
    window.title("Work Shift App")

    ui_window = UI(window)
    ui_window.start()

    window.mainloop()


if __name__ == "__main__":
    main()
