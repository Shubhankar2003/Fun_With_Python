import os
from pathlib import Path
import re

root_folder = Path('C:/Series/New Girl')

for folder_name, _ , _ in os.walk(root_folder):
    folder_path = Path(folder_name)
    match = re.search(r'Season\s+(\d+)', folder_name)
    if match:
        season_number = match.group(1)
        new_folder_name = f"Season {season_number}"
        new_folder_path = folder_path.parent / new_folder_name
        folder_path.rename(new_folder_path)
    
print ('Renaming Process Completed')