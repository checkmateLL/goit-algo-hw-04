from colorama import Fore
import sys
from pathlib import Path

path = sys.argv[1]
parent_folder_path = Path(path)

def parse_folder(path, level=0):
    try:
        for element in path.iterdir():
            indent = " " * 4 * level
            if element.is_dir():
                print(Fore.YELLOW + f"{indent}|--{element.name}")
                parse_folder(element, level + 1)
            if element.is_file():
                print(Fore.GREEN + f"{indent}|--{element.name}")
    except FileNotFoundError:
        print(Fore.RED + f"Directory {path} not found!")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")



parse_folder(parent_folder_path)
