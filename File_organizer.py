import shutil, os
from pathlib import Path
p = Path.home()
pdf_folder = p / 'Downloads' / 'PDF'
photo_folder = p / 'Downloads' / 'Photos'
music_folder = p / 'Downloads' / 'Music'
video_folder = p / 'Downloads' / 'Videos'
rand_folder = p / 'Downloads' / 'Random'

pdf_folder.mkdir(exist_ok=True)  # Ensure 'PDF' folder exists or create it if not
photo_folder.mkdir(exist_ok=True) # Ensure 'Photo' folder exists or create it if not
music_folder.mkdir(exist_ok=True) # Ensure 'Music' folder exists or create it if not
video_folder.mkdir(exist_ok=True) # Ensure 'Videos' folder exists or create it if not
rand_folder.mkdir(exist_ok=True) # Ensure 'Random' folder exists or create it if not


for folderName, subfolders, filenames in os.walk(p/'Downloads'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            src_path =  Path(folderName)/filename
            dest_path = pdf_folder/filename
            shutil.move(src_path, dest_path)
        elif filename.endswith(('.jpg', '.jpeg', '.png', '.webp', '.heic')):
            src_path =  Path(folderName)/filename
            dest_path = photo_folder/filename
            shutil.move(src_path, dest_path)
        elif filename.endswith(('.mp3', '.aac')):
            src_path =  Path(folderName)/filename
            dest_path = music_folder/filename
            shutil.move(src_path, dest_path)
        elif filename.endswith(('.mp4', '.mov')):
            src_path =  Path(folderName)/filename
            dest_path = video_folder/filename
            shutil.move(src_path, dest_path)
        else:
            src_path =  Path(folderName)/filename
            dest_path = rand_folder/filename
            shutil.move(src_path, dest_path)


print(''' Moved all files to designated folders ''')