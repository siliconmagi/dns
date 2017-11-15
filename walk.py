import os

# The top argument for walk
topdir = '.'

# The extension to search for
exten = '.txt'

for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten):
            print(os.path.join(dirpath, name))
