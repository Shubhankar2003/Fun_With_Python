import os
from pathlib import Path
import re

p = Path('C:/Series/New Girl')

for folderName, subfolders, filenames in os.walk(p):
    match = re.search(r'Season\s+(\d+)', folderName)
    if match:
        season_number = match.group(1)
        new_folder_name = f"Season {season_number}"
        original_path = Path(folderName)
        parent_path = original_path.parent
        new_path = parent_path / new_folder_name
        os.rename(original_path, new_path)