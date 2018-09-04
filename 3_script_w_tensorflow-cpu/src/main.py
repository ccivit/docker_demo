try:
    import tensorflow as tf
    print('Successfully installed Tensorflow',tf.__version__,"for CPU")
except:
    print("ERROR: Couldn't load Tensorflow")
##try:
##    import other_script
##except:
##    print("'Couldn't load 'other_script.py'")
##try:
##    import os
##    filename = "placeholder.txt"
##    directory = "data"
##    filepath = os.path.join(directory,filename)
##    f  = open(filepath, 'r')
##    print(f.read())
##except:
##    print("ERROR: Couldn't find the data folder")
