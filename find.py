# script to read file and find text
# install preqs pipenv install mmap
import mmap

with open('3bd2ba.com.db', 'rb', 0) as file, \
     mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
    if s.find(b'www') != -1:
        print('true')
