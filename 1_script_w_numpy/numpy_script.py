try:
    import numpy as np
    print('Successfully loaded numpy')
    a=np.array([1,2,3])
    print('Sample numpy array: ',a)
except:
    print('Could not load numpy. Check if it is properly installed')

