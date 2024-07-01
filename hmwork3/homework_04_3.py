from colorama import Fore
import sys
from pathlib import Path

path = sys.argv[1]
parent_folder_path = Path(path)

def parse_folder(path):
    for element in path.iterdir():
        if element.is_dir():
            print(Fore.YELLOW + f"Parsed data: This is folder - {element.name}")
            parse_folder(element)
        if element.is_file():
            print(Fore.GREEN + f"Parsed data: This is file - {element.name}")

parse_folder(parent_folder_path)
