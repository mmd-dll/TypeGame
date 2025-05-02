from time import time, sleep
from os import system, get_terminal_size, name as os_name
from colorama import Fore, Style, init, Back
from lorem import sentence
import sys

init(autoreset=True)

text = f"{sentence()} {sentence()} {sentence()} {sentence()}"

# Platform-specific imports
if os_name == "nt":
    import msvcrt
else:
    import tty
    import termios


def get_char():
    if os_name == "nt":
        return msvcrt.getwch()
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            return ch
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def clear_screen():
    system("cls" if os_name == "nt" else "clear")


def StartMenu():
    clear_screen()
    name = """
       ████████╗██╗   ██╗██████╗ ███████╗      ████████╗███████╗ ██████╗████████╗
      ╚══██╔══╝╚██╗ ██╔╝██╔══██╗██╔════╝      ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
       ██║    ╚████╔╝ ██████╔╝█████╗  █████╗   ██║   █████╗  ╚█████╗    ██║
       ██║     ╚██╔╝  ██╔═══╝ ██╔══╝  ╚════╝   ██║   ██╔══╝   ╚═══██╗   ██║
       ██║      ██║   ██║     ███████╗         ██║   ███████╗██████╔╝   ██║
       ╚═╝      ╚═╝   ╚═╝     ╚══════╝         ╚═╝   ╚══════╝╚═════╝    ╚═╝
    """
    or_name = "TG : RedSnows"

    cols = get_terminal_size().columns

    for line in name.splitlines():
        padding = (cols - len(line)) // 2
        print(Fore.CYAN + " " * max(padding, 0) + line)
        sleep(0.05)

    padding = (cols - len(or_name)) // 2
    print(Fore.GREEN + " " * max(padding, 0) + or_name)

    print(Fore.LIGHTRED_EX + "Telegram:", Fore.LIGHTWHITE_EX + "https://t.me/RedSnows")
    print(
        Fore.LIGHTRED_EX + "GitHub:", Fore.LIGHTWHITE_EX + "https://github.com/mmd-dll"
    )
    print()
    print(Fore.BLUE + "[1]" + Fore.WHITE, "Start game")
    print(Fore.BLUE + "[2]" + Fore.WHITE, "Exit")

    while True:
        user_Choice = input("\n\nEnter option number: ")
        try:
            user_Choice = int(user_Choice)
        except:
            print("Enter a number, not a string!")
            continue

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
        char = get_char()

        if char == text[index]:
            user_input += Fore.GREEN + char
        else:
            user_input += Fore.RED + text[index]

        index += 1

        clear_screen()

        remaining_text = text[index:]
        if remaining_text:
            next_char = (
                Back.MAGENTA + Fore.BLACK + remaining_text[0] + Fore.RESET + Back.RESET
            )
            rest_chars = remaining_text[1:]
            colored_input = user_input + next_char + rest_chars
        else:
            colored_input = user_input

        print(colored_input)

    end_time = time()
    duration = end_time - start_time
    words = len(text.split())
    wpm = (words / duration) * 60

    print()
    print(Fore.GREEN + f"🎉 Completed in {duration:.2f} seconds!")
    print(Fore.GREEN + f"🕒 Typing speed: {wpm:.2f} words per minute")


typing_game()
