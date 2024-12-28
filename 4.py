import os
import re
import numpy as np
os.chdir('C:/Users/matej/OneDrive/Desktop/Statistical methods/AOC')
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)
filename = "data.txt"
# filename = "startdata.txt"
u = 0
with open(filename) as f:
    cont = "".join(f.readlines())
with open(filename) as f:
    for line in f:
        u+=1
cont = re.sub(r'\n', r';', cont)
rows = cont.split(';')

# Convert each row into a list of characters
matrix = [list(row) for row in rows]

for row in matrix:
    strung = "".join(row)
    print(re.findall("XMAS", strung), strung)
    print(re.findall("SAMX", strung), strung)


        
        