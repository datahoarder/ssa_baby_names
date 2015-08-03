"""
run:
    $ python -m scripts.compile.compile_states

creates:
    stash/compiled/states.csv
    (this is not included in the repo due to size)
"""
from scripts.settings import DOWNLOADED_STATES_DIR, COMPILED_STATES_PATH
from glob import glob
import os.path
import re


if __name__ == "__main__":
    # open up the file to write to
    c = open(COMPILED_STATES_PATH, 'w')
    c.write("state,sex,year,name,count\n")

    # glob up the downloaded individual files
    filespath = os.path.join(DOWNLOADED_STATES_DIR, '*.TXT')
    for fname in glob(filespath):
        print("Reading", fname)
        with open(fname, 'r') as f:
            c.writelines(f.readlines())
    # close the combined file
    c.close()
