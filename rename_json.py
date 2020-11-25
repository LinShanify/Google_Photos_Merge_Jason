import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("folder", help="the folder that should be processed")
args = parser.parse_args()

for subdir, dirs, files in os.walk(args.folder):
    for filename in files:
        filepath = os.path.join(subdir,filename)
        if '..json' in filepath and filename[:2] != '._':
            new_filepath = filepath.replace('..json','.json')
            os.rename(filepath,new_filepath)
            print(new_filepath)
        elif '.JPG.json' in filepath and filename[:2] != '._':
            new_filepath = filepath.replace('.JPG.json','.json')
            os.rename(filepath,new_filepath)
            print(new_filepath)
        elif '.jpg.json' in filepath and filename[:2] != '._':
            new_filepath = filepath.replace('.jpg.json','.json')
            os.rename(filepath,new_filepath)
            print(new_filepath)
        elif '.jpeg.json' in filepath and filename[:2] != '._':
            new_filepath = filepath.replace('.jpeg.json','.json')
            os.rename(filepath,new_filepath)
            print(new_filepath)
        elif '.j.json' in filepath and filename[:2] != '._':
            new_filepath = filepath.replace('.j.json','.json')
            os.rename(filepath,new_filepath)
            print(new_filepath)
        elif '.jp.json' in filepath and filename[:2] != '._':
            new_filepath = filepath.replace('.jp.json','.json')
            os.rename(filepath,new_filepath)
            print(new_filepath)
        elif '_.json' in filepath and filename[:2] != '._':
            new_filepath = filepath.replace('_.json','.json')
            os.rename(filepath,new_filepath)
            print(new_filepath)
        elif '_n.json' in filepath and filename[:2] != '._':
            new_filepath = filepath.replace('_n.json','.json')
            os.rename(filepath,new_filepath)
            print(new_filepath)
        elif '_n.jpg' in filepath and filename[:2] != '._':
            new_filepath = filepath.replace('_n.jpg','.jpg')
            os.rename(filepath,new_filepath)
            print(new_filepath)
        elif '_n.jepg' in filepath and filename[:2] != '._':
            new_filepath = filepath.replace('_n.jepg','.jepg')
            os.rename(filepath,new_filepath)
            print(new_filepath)
        elif '_n.JPG' in filepath and filename[:2] != '._':
            new_filepath = filepath.replace('_n.JPG','.JPG')
            os.rename(filepath,new_filepath)
            print(new_filepath)
        else:
            pass

        # os.rename(filepath,filepath.strip())