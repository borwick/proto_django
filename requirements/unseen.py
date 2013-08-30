#!python
from glob import glob
import sys

SEEN_REQUIREMENTS = set()
def add_requirements(fh):
    for line in fh:
        SEEN_REQUIREMENTS.add(line.strip())


if __name__=='__main__':
    for req in glob('*.txt'):
        add_requirements(open(req))

    for line in sys.stdin:
        line = line.strip()
        if line not in SEEN_REQUIREMENTS:
            print line
