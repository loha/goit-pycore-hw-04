import os
from colorama import init, Fore, Style # type: ignore

init(autoreset=True)  # Initialize colorama for colored output

def get_dir_structure(path, level=0):
  if not os.path.isdir(path):
    return

  files = get_sorted_file_structure(path)
  for entry in files:
    entry_path = os.path.join(path, entry)
    if os.path.isdir(entry_path):
      prefix = "├─" * level  # Use different mid-level connectors for readability
      print(f"{prefix}{Fore.BLUE}{entry}{Style.RESET_ALL} (dir)")
      get_dir_structure(entry_path, level + 1)  # Increase level for subdirectories
    else:
      prefix = "└─" * level  # Use different end connectors for readability
      print(f"{prefix}{Fore.GREEN}{entry}{Style.RESET_ALL} (file)")

def get_sorted_file_structure(path: str):
  dirs = []
  files = []
  for name in os.listdir(path):
    entry_path = os.path.join(path, name)
    if os.path.isdir(entry_path):
      dirs.append(name)
    else:
      files.append(name)
  
  return sorted(dirs) + sorted(files)

current_absolute_path = os.path.abspath(os.getcwd())

dir = str(input(f"Enter path to show dir structure\nFrom this path: {current_absolute_path}/"))

get_dir_structure(dir)