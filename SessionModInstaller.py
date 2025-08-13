###########################################################################################################################################################
# The tools are completely safe. On the front page, ive made a spreadsheet explaining every tool and where it originate from.
# Please make sure you got this from GitHub, or any trusted source listed on the Front page spreadsheet.
# Enjoy this project and the updates that comes with it since its my first ever python project (sucks xD) and may look sloppy.
# - jc
###########################################################################################################################################################

# Imports
import keyboard # https://pypi.org/project/keyboard/
import os # comes with python
import time # comes with python
import art # https://pypi.org/project/art/
from art import * # https://pypi.org/project/art/
import requests
import shutil
import colorama
from colorama import Fore, Style, init
init() # for colorama
import subprocess
from os import system
import webbrowser
import auto_py_to_exe
import sys




# Beginning

#os.system("title SessionModInstaller") # title of program
#os.system("mode 150, 43") # pretty much only for windows 10 (i think.....)
#os.system("cls") # clearing screen
#tprint("Session Mod Installer") # makes cool art
#tprint("Created by jcxeq", font="small")
#print("\nThank you for support my program\nMany updates/improvements to come in my coding journey!")
#time.sleep(2)
#os.system("cls") # clearing screen # clearing screen


# Intro

os.system("cls") # clearing screen
tprint("Session Mod Installer") # makes cool art
#tprint("Created by jcxeq", font="small")
intro = print("\nIf your confused/don't know what to choose, please use help command!\n\nSelect an choice below")
sk8 = print(" ") # empty space 0u0
print(" ") # empty space 0u0
sk8 = print("_______________________________________________________________________________________________________")
sk8 = print(" ") # empty space 0u0
sk8 = print("    Installation Presets")
print(" ") # empty space 0u0
sk8 = print("_______________________________________________________________________________________________________")
print(" ") # empty space 0u0
sk8 = print("[S] -- Minimal Installation")
sk8 = print("[K] -- Recommended Installation                                                                                     [P2] -- Page 2")
sk8 = print("[A] -- [soon]                                                                                                       [?]  - Help")
sk8 = print("[T] -- [soon]                  ")
sk8 = print("[E] -- [soon]                  ")
sk8 = print(" ") # empty space 0u0
sk8 = print("_______________________________________________________________________________________________________")
picking = input(Fore.GREEN + "\n>: " + Style.RESET_ALL)

        # directorys    
UMI = "C:\\SessionModInstaller\\Tools\\Minimal\\UnrealModUnlocker\\Unreal Mod Unlocker Basic.exe" # program location (dont rename/change!)
SMM = "C:\\SessionModInstaller\\Tools\\Minimal\\Session Mod Manager\\SessionModManager.exe" # program location (dont rename/change!)
UMIR = "C:\\SessionModInstaller\\Tools\\Recommended\\UnrealModUnlocker\\Unreal Mod Unlocker Basic.exe" # program location (dont rename/change!)
SMMR = "C:\\SessionModInstaller\\Tools\\Recommended\\Session Mod Manager\\SessionModManager.exe" # program location (dont rename/change!)
RST = "C:\\SessionModInstaller\\RUN.bat"
SMP = "C:\\SessionModInstaller\\Tools\\SSMI.bat"

        # end of directorys

# Page 1

if picking == "?":
        helpme = "https://github.com/Jcxeq/SessionModInstaller/issues"
        RST = "C:\\SessionModInstaller\\RUN.bat"
        webbrowser.open(helpme)
        subprocess.run([RST])

if picking == "s": # minimal tools needed for session mods
            

                os.system("cls") # clearing screen # clearing screen
                tprint("Session Mod Installer") # makes cool art
                print(Fore.YELLOW + 'Searching for "Unreal Mod Unlocker"' + Style.RESET_ALL)
                time.sleep(10)
                os.system("cls") # clearing screen
                print("IGNORE LOG BELOW !")
                subprocess.run([UMI]) # runs unlocker

            # end of unlocker

                os.system("cls") # clearing screen
                tprint("Session Mod Installer") # makes cool art
                print(Fore.GREEN + "Unreal Mod Unlocker is completed!" + Style.RESET_ALL)
                time.sleep(5)
                os.system("cls") # clearing screen
                tprint("Session Mod Installer") # makes cool art
                print(Fore.YELLOW + 'Searching for "Session Mod Manager"' + Style.RESET_ALL)
                time.sleep(10)
                os.system("cls") # clearing screen
                tprint("Session Mod Installer") # makes cool art
                print(Fore.GREEN + "\n\nInstrutions:\n\nOpen Steam\nGo to library\nRight click Session Skate Sim, go to manage, and browse local files\nCopy directory into Session mod manager\nAfter, go to third icon, and one by one, drag each zip folder in the Minimal Mods folder, and import\n[ located: C:\\SessionModInstaller\\Tools\\Minimal\\Minimal Mods ]" + Style.RESET_ALL)
                subprocess.run([SMM]) # runs manager
                os.system("cls") # clearing screen
                print(Fore.GREEN + "Session Mod Manager is completed!" + Style.RESET_ALL)
                time.sleep(5)

            # end of manager

                os.system("cls") # clearing screen
                tprint("Session Mod Installer") # makes cool art
                print(Fore.GREEN + "\nFinished with minimal installation!" + Style.RESET_ALL)
                close = input("\nWould like to close the program or continue?: ")
                if close == "y":
                        sys.exit(0)
                elif close == "n":
                        subprocess.run([RST])

            # end of  minimal installation


if picking == "k": # recommended tools needed for session mods
                

                os.system("cls") # clearing screen # clearing screen
                tprint("Session Mod Installer") # makes cool art
                print(Fore.YELLOW + 'Searching for "Unreal Mod Unlocker"' + Style.RESET_ALL)
                time.sleep(10)
                os.system("cls") # clearing screen
                print("IGNORE LOG BELOW !")
                subprocess.run([UMIR]) # runs unlocker

            # end of unlocker

                os.system("cls") # clearing screen
                tprint("Session Mod Installer") # makes cool art
                print(Fore.GREEN + "Unreal Mod Unlocker is completed!" + Style.RESET_ALL)
                time.sleep(5)
                os.system("cls") # clearing screen
                tprint("Session Mod Installer") # makes cool art
                print(Fore.YELLOW + 'Searching for "Session Mod Manager"' + Style.RESET_ALL)
                time.sleep(10)
                os.system("cls") # clearing screen
                tprint("Session Mod Installer") # makes cool art
                print(Fore.GREEN + "\n\nInstrutions:\n\nOpen Steam\nGo to library\nRight click Session Skate Sim, go to manage, and browse local files\nCopy directory into Session mod manager\nAfter, go to third icon, and one by one, drag each zip folder in the Recommended Mods folder, and import\n[ located: C:\\SessionModInstaller\\Tools\\Recommended\\Recommended Mods ]" + Style.RESET_ALL)
                subprocess.run([SMMR]) # runs manager
                os.system("cls") # clearing screen
                tprint("Session Mod Installer") # makes cool art
                print(Fore.GREEN + "Session Mod Manager is completed!" + Style.RESET_ALL)
                time.sleep(5)

            # end of manager

                os.system("cls") # clearing screen
                tprint("Session Mod Installer") # makes cool art
                print(Fore.GREEN + "\nFinished with recommended installation!" + Style.RESET_ALL)
                close = input("\nWould like to close the program or continue?: ")
                if close == "y":
                        sys.exit(0)
                elif close == "n":
                        subprocess.run([RST])


# Page 2
        
if picking == "p2":
                os.system("cls") # clearing screen
                tprint("Session Mod Installer") # makes cool art
                #tprint("Created by jcxeq", font="small")
                intro = print("\nIf your confused/don't know what to choose, please use help command!\n\nSelect an choice below")
                sk8 = print(" ") # empty space 0u0
                print(" ") # empty space 0u0
                sk8 = print("_______________________________________________________________________________________________________")
                sk8 = print(" ") # empty space 0u0
                sk8 = print("    Page 2")
                print(" ") # empty space 0u0
                sk8 = print("_______________________________________________________________________________________________________")
                print(" ") # empty space 0u0
                sk8 = print("[LMP] -- Load SMP")
                sk8 = print("[L?] -- [soon]                                                                                                       [P1] -- Page 1")
                sk8 = print("[L?] -- [soon]                                                                                                       [?]  - Help")
                sk8 = print("[L?] -- [soon]                  ")
                sk8 = print("[L?] -- [soon]                  ")
                sk8 = print(" ") # empty space 0u0
                sk8 = print("_______________________________________________________________________________________________________")
                pickingg = input(Fore.GREEN + "\n>: " + Style.RESET_ALL)

if pickingg == "p1":
        subprocess.run([RST])


# end of pages



else:
                os.system("cls") # clearing screen
                tprint("Session Mod Installer") # makes cool art
                print(Fore.RED + "Error!, Restarting..." + Style.RESET_ALL)
                time.sleep(2)
                os.system("cls") # clearing screen # clearing screeN
                subprocess.run([RST])
