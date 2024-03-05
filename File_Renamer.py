import os
from pathlib import Path
import re

root_folder = Path('C:/Series/New Girl')

renamed = False

for folder_name, sub_folder, file_name in os.walk(root_folder):
    folder_path = Path(folder_name)
    match = re.search(r'Season\s+(\d+)', folder_name)
    if match:
        season_number = match.group(1)
        new_folder_name = f"Season {season_number}"
        new_folder_path = folder_path.parent / new_folder_name
        if folder_path != new_folder_path:
            folder_path.rename(new_folder_path)
            renamed = True

if renamed:
    print('Renaming process completed.')
else:
    print('Folders are already renamed.')