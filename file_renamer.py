import os
import sys

""" 
Finds and replaces pattern in file names.
Usage:
python file_renamer.py ODY_XFS PRO_XFS
"""

def rename_files(input_pattern, output_pattern):
    path =  os.getcwd()
    filenames = os.listdir(path)
    for filename in filenames:
        new_name = filename.replace(input_pattern, output_pattern)
        if(new_name != filename):
            print("Renaming " + filename + " to " + new_name)
            os.rename(filename, new_name)

if(len(sys.argv) < 2):
    print("Please call this script from command line passing input pattern and output pattern as parameters")
    print("Example: python file_renamer.py ODY_XFS PRO_XFS")
else:
    rename_files(sys.argv[1], sys.argv[2])


