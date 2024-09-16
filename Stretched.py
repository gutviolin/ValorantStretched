import ctypes
import pyuac

def main():
    window_title = "VALORANT  "

    # Search window
    window_handle = ctypes.windll.user32.FindWindowW(None, window_title)

    if window_handle == 0:
        ctypes.windll.user32.MessageBoxW(0, "Valorant not Running", "EZTS", 0)
    else:
        # Change window properties
        style = ctypes.windll.user32.GetWindowLongW(window_handle, ctypes.c_int(-16))
        style = style & ~0x00800000  # WS_DLGFRAME removal
        style = style & ~0x00040000  # WS_BORDER removal
        ctypes.windll.user32.SetWindowLongW(window_handle, ctypes.c_int(-16), style)

        # Maximize window
        ctypes.windll.user32.ShowWindow(window_handle, ctypes.c_int(3))  # SW_MAXIMIZE

        ctypes.windll.user32.MessageBoxW(0, "True Stretch Applied", "EZTS", 0)
    # The window will disappear as soon as the program exits!

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:        
        main()  # Already an admin here.
