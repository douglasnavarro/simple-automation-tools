import os
import sys

""" 
Finds and replaces pattern in file contents.
Usage:
python find_and_replace_all.py ODY_XFS PRO_XFS
"""

def inplace_change(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print(old_string + " not found in " + filename)
            return
        
        else:
            with open(filename, 'w') as f:
                print("Replacing " + old_string +  " to " + new_string + " in " + filename)
                s = s.replace(old_string, new_string)
                f.write(s)
                f.close()

def main():
    if(len(sys.argv) < 3):
        print("Please call this script from command line passing input pattern and output pattern as parameters")
        print("Example: python find_and_replace_all.py ODY_XFS PRO_XFS")
        return
    else:
        path =  os.getcwd()
        filenames = os.listdir(path)
        for filename in filenames:
            if(".xml" not in filename):
                continue
            else:
                print("Running inplace_change({}, {}, {}\n", filename, sys.argv[1], sys.argv[2])
                inplace_change(filename, sys.argv[1], sys.argv[2])
main()
