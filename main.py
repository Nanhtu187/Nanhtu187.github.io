import os

files = os.listdir("src/img")
for file in files:
    print("\'" + file + "\',", end = '')