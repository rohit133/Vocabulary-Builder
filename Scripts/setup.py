from cx_Freeze import setup, Executable

base = None    

executables = [Executable("Word_Notifier.py", base = "Win32GUI", icon="app_icon.ico")]

packages = ["requests","PyDictionary","win10toast","schedule"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Vocabulary Builder",
    options = options,
    version = "1.0",
    description = "",
    executables = executables
)