# keylogger

# Compiled in WINDOWS
  pyinstaller --onefile --hidden-import pynput.keyboard._win32 --hidden-import pynput.mouse._win32 .\gmail.pyw
