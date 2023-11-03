try:
    import yaml
    import os
    import runpy
    input("STATUS 1 (OK)\nEnter any key to continue\n")
except Exception as e:
    i = -1
    while i < 0 or i > 1:
        i = int(input("STATUS 2 (ERROR)\n[0] Error details\n[1] Exit\n"))
    if i == 0:
        input(f"{e} (Perhaps its not installed?)\nEnter any key to continue\n")
    else:
        exit()
i = -1
while i < 0 or i > 1:
    i = int(input("Choose your computer's operating system\n[0] Windows\n[1] Linux (Buggy)\n"))
sys = "win" if i == 0 else "gnu"
def clear():
    os.system("cls" if sys == "win" else "clear")
clear()
language = "en"
options = []
modss = os.listdir(os.path.join(os.getcwd(), "Modifications"))
def initialopt():
    global language
    global options
    options = [
        {
        "Name": "Change Language (not working)" if language == "en" else "Cambiar Idioma" if language == "es" else "Sprache ändern",
        "Func": changelang
        },
        {
        "Name": "View Modifications",
        "Func": mods
        }
    ]
def mods():
    clear()
    global modss
    if len(modss) < 1:
        input("You don't have any modifications.\nPress any key to continue\n")
    clear()
def changelang():
    global language
    global options
    i = -1
    while i < 0 or i > 2:
        clear()
        i = int(input("Select Language:\n[0] English\n[1] Spanish\n[2] German\n"))
    language = "en" if i == 0 else "es" if i == 1 else "de"
    input(f"It will be in {language} from now on until user changes it. Press any key to continue\n")
    initialopt()
    clear()
string = "Options:\n"
i = 0
initialopt()
for option in options:
    string += f"[{i}] " + option["Name"] + "\n"
    i += 1
string += f"[{i}] " + "Exit"
opt = -1
while True:
    opt = int(input(string + "\n"))
    if opt < 0 or opt > len(options):
        break
    else: 
        options[opt]["Func"]()
