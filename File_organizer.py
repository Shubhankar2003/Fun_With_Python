import shutil, os
from pathlib import Path
p = Path.home()
pdf_folder = p / 'Downloads' / 'pdf'
pdf_folder.mkdir(exist_ok=True)  # Ensure 'pdf' folder exists or create it if not

for folderName, subfolders, filenames in os.walk(p/'Downloads'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            src_path =  Path(folderName)/filename
            dest_path = pdf_folder/filename
            shutil.move(src_path, dest_path)
            print(f"Moved {filename} to {pdf_folder}")

print('''
        Moved all 'PDF' files
''')