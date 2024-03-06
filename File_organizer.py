from os import walk, path
from shutil import move
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


for folderName, subfolders, filenames in walk(p/'Downloads'):
    for filename in filenames:
        src_path =  Path(folderName)/filename
        if path.isfile(src_path):
            if filename.endswith('.pdf'):
                dest_path = pdf_folder/filename
                move(src_path, dest_path)
            elif filename.endswith(('.jpg', '.jpeg', '.png', '.webp', '.heic')):
                dest_path = photo_folder/filename
                move(src_path, dest_path)
            elif filename.endswith(('.mp3', '.aac')):
                dest_path = music_folder/filename
                move(src_path, dest_path)
            elif filename.endswith(('.mp4', '.mov')):
                dest_path = video_folder/filename
                move(src_path, dest_path)
            else:
                dest_path = rand_folder/filename
                move(src_path, dest_path)
