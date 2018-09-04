try:
    import other_script
except:
    print("'Couldn't load 'other_script.py'")
try:
    import numpy
    print("Successfully imported downloaded numpy library")
except:
    print("ERROR: Couldn't load downloaded numpy library")
try:
    import os
    filename = "placeholder.txt"
    directory = "data"
    filepath = os.path.join(directory,filename)
    f  = open(filepath, 'r')
    print(f.read())
except:
    print("ERROR: Couldn't find the data folder")
