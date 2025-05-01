from time import time
from os import system, get_terminal_size
from colorama import Fore, Style, init
from lorem import sentence
from time import sleep
import os
import msvcrt

init(autoreset=True)

text = f"{sentence()} {sentence()} {sentence()} {sentence()}"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def StartMenu():
    clear_screen()
    name = '''
       ████████╗██╗   ██╗██████╗ ███████╗      ████████╗███████╗ ██████╗████████╗
      ╚══██╔══╝╚██╗ ██╔╝██╔══██╗██╔════╝      ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
       ██║    ╚████╔╝ ██████╔╝█████╗  █████╗   ██║   █████╗  ╚█████╗    ██║
       ██║     ╚██╔╝  ██╔═══╝ ██╔══╝  ╚════╝   ██║   ██╔══╝   ╚═══██╗   ██║
       ██║      ██║   ██║     ███████╗         ██║   ███████╗██████╔╝   ██║
       ╚═╝      ╚═╝   ╚═╝     ╚══════╝         ╚═╝   ╚══════╝╚═════╝    ╚═╝
    '''
    or_name = """TG : RedSnows"""

    cols = get_terminal_size().columns

    for text in name.splitlines():
        padding = (cols - len(text)) // 2
        print(Fore.CYAN + " " * max(padding, 0) + text)
        sleep(0.05)

    padding = (cols - len(or_name)) // 2
    print(Fore.GREEN + " " * max(padding, 0) + or_name)

    print(Fore.LIGHTRED_EX + "Telegram:", Fore.LIGHTWHITE_EX + "https://t.me/RedSnows")
    print(Fore.LIGHTRED_EX + "GitHub:", Fore.LIGHTWHITE_EX + "https://github.com/mmd-dll")
    print('')
    print(Fore.BLUE +'[1]' + Fore.WHITE,'Start game')
    print(Fore.BLUE +'[2]' + Fore.WHITE,'Exit')
    while True:
        user_Choice = input('\n\nEnter option number: ')
        try:
            user_Choice = int(user_Choice)
        except:
            print("Enter an number not Str!")
        
        if user_Choice == 1:
            break
        elif user_Choice == 2:
            exit()

def typing_game():

    StartMenu()
    clear_screen()

    cols = get_terminal_size().columns
    padding = (cols - len("Ok, ready...")) // 2
    print(Fore.GREEN + " " * max(padding, 0) + "Ok, ready...")
    sleep(1)
    clear_screen()
    print(Fore.WHITE + Style.BRIGHT + text + "\n")
    
    user_input = ""
    index = 0
    start_time = time()

    while index < len(text):
        char = msvcrt.getwch()

        if char == text[index]:
            user_input += char
            index += 1
        else:
            pass

        clear_screen()
        print(Fore.WHITE + Style.BRIGHT + text + "\n")
        
        colored_input = (Fore.GREEN + user_input +
                         Fore.RESET + text[index:])
        
        clear_screen()
        print(colored_input)

    end_time = time()
    duration = end_time - start_time
    words = len(text.split())
    wpm = (words / duration) * 60

    print()
    print(Fore.GREEN + f"🎉 Completed in {duration:.2f} seconds!")
    print(Fore.GREEN + f"🕒 Typing speed: {wpm:.2f} words per minute")

typing_game()
