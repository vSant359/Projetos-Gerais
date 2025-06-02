import os
import shutil

def move_items(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    files = os.listdir(source_dir)
    
    for file in files:
        if file.endswith('.pdf'):
            source_file = os.path.join(source_dir, file)
            target_file = os.path.join(target_dir, file)
            
            shutil.move(source_file, target_file)
            print(f'Movido: {source_file} -> {target_file}')

source_directory = 'C:\\Users\\despachatur\\Documents\\pdf'
target_directory = 'C:\\Users\\despachatur\\Documents\\pdfs'
move_items(source_directory, target_directory)
