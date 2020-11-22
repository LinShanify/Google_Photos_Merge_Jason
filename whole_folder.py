import os
import os
import argparse
import shutil
import time

parser = argparse.ArgumentParser()
parser.add_argument("folder", help="whole folder that should be processed")
args = parser.parse_args()

for subdir, dirs, files in os.walk(args.folder):
    print(subdir)
    os.system('python json_merge.py ' + subdir)
    time.sleep(5)
