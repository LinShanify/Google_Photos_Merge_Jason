import os
import argparse
import shutil
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("folder", help="the folder that should be processed")
args = parser.parse_args()

for subdir, dirs, files in os.walk(args.folder):
    for filename in files:
        filepath = os.path.join(subdir,filename)
        if'.GIF' in filepath:
            # try:
            #     im = Image.open(filepath)
            # except:
            #     print(filepath)
            os.remove(filepath)
        # os.rename(filepath,filepath.strip())